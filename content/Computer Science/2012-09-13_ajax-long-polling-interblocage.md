Title: Ajax Long Polling - problème de chargement des pages avec les sessions PHP (interblocage)
Date: 2012-09-13 22:12
Tags: Ajax, Long Polling
Author: François Chapuis

Ces derniers jours, j'ai développé, entre autres, un système de notifications tel que celui présent sur Facebook. J'ai décidé d'utiliser la fonction [$.ajax()](http://api.jquery.com/jQuery.ajax/) de jQuery (et ses dérivés : $.get(), $.getJSON()...) pour faire du [long polling](http://en.wikipedia.org/wiki/Push_technology#Long_polling) (voir aussi [Comet](http://en.wikipedia.org/wiki/Comet_%28programming%29#XMLHttpRequest_long_polling)). Cette fonction utilise l'objet [XMLHttpRequest](http://fr.wikipedia.org/wiki/XMLHttpRequest) (ou plus précisément [jqXHR](http://api.jquery.com/types/#jqXHR) depuis jQuery 1.5) pour maintenir une connexion HTTP au serveur active pendant un long moment.

Bref aperçu du long polling
===========================

Avec le protocole HTTP, la communication entre un serveur et ses clients est déséquilibrée : le serveur ne peut envoyer des données aux clients qu'en réponse à une demande explicite de leur part. Le long polling est une méthode qui permet de remédier à ce "problème", au prix d'une consommation CPU plus importante sur le serveur, puisque celui-ci doit réaliser une [attente active](http://fr.wikipedia.org/wiki/Attente_active#Des_alternatives_.C3.A0_l.27attente_active) (en PHP en tout cas).

Je ne vais pas détailler ici le fonctionnement du long polling puisque d'autres l'ont déjà fait de nombreuses fois. **Si vous recherchez un bon exemple de code en PHP, je vous conseille [cette vidéo](http://www.screenr.com/SNH)** qui explique en 5 minutes un exemple de base. Je me contenterai de préciser qu'avec ce code, si le serveur n'envoie aucune donnée pendant la durée définie par *max_execution_time* dans le fichier *php.ini* (30 secondes par défaut), le code s'arrêtera tout simplement en renvoyant une erreur "* **Fatal error**: Maximum execution time of 30 seconds exceeded*" (visible dans une console d'erreur Javascript telle que celle de Firebug). Pour que la fonction callback d'erreur définie dans $.ajax() soit appelée et relance le script, il faut définir un timeout ainsi:

~~~javascript
$.ajax({
    ...
    timeout: 40000, // -- Abort after [40] seconds.
    ...
});
~~~

Il faut que ce timeout soit inférieur à la valeur de *max_execution_time*, sinon il n'aura aucun effet. Si vous voulez changer la durée maximale d'exécution d'un script PHP spécifique, vous pouvez utiliser la fonction *set_time_limit($nb_seconds)* dans ce script.

Bref, je n'ai pas décidé d'écrire cet article pour expliquer le long polling mais pour garder une trace d'un problème que j'ai rencontré en l'implémentant et de sa solution...


Le problème
===========

Imaginons qu'on a un code tel que celui-ci sur le serveur :

~~~php
<?php
set_time_limit(50); // Script will stop after running for [50] seconds
   
session_start(); // <===== Cette ligne est importante
     
     
$lastupdate = isset($_GET['timestamp']) ? $_GET['timestamp'] : 0;
     
$lastmodif = lastModification();
     
// =====> Cette boucle aussi est importante <=====
while($lastmodif <= $lastupdate) {
    usleep(10000);
    $lastmodif = lastModification();
}
     
// The event occured => send the response
$response = array();
$response['timestamp'] = $lastmodif;
     
update($response, $lastupdate);
     
echo json_encode($response);
     
function lastModification() {
    return myQuery('SELECT COUNT(*) FROM `notifications` WHERE `read`=0 AND `user_id`=' . $_SESSION['user_id']);
}
     
function update(&$response, $lastupdate) {
    ...
}
?>
~~~

Dans ce code, on veut avoir accès à la variable $_SESSION. On utilise donc un session_start(). Cependant **les sessions PHP sont bloquantes !** Puisque l'appel à $.ajax() est réalisé dans un $(document).ready(), il n'y a pas de problème tant que l'utilisateur n'utilise le site que sur une page ou onglet à la fois :

  * Une session est ouverte par le script principal
  * Le script principal de termine
  * L'appel à notre script via Ajax est réalisé => le script Ajax ouvre une session
  * Les données sont reçues ou le timeout expire => la session ouverte est fermée

Par contre, si l'utilisateur décide d'ouvrir une deuxième page, il y a un **interblocage** (deadlock) :

  * Une session est ouverte par le script principal
  * Le script principal de termine
  * L'appel à notre script via Ajax est réalisé => le script Ajax ouvre une session
  * **L'utilisateur ouvre une nouvelle page (alors que le script est en attente active de données dans la boucle while)**
  * Le script PHP qui va se charger de l'affichage de la nouvelle page fait un appel à session_start()
  * Le chargement de la page est mis en attente jusqu'à ce que le script appelé via Ajax se termine et libère la session. L'utilisateur ne voit qu'une page blanche...

<p></p>
La solution
===========

C'est un commentaire sur [cette page](http://be.php.net/session_write_close) qui m'a fourni la solution : *If the ajax function doesn't do session_write_close(), then your outer page will appear to hang, and opening other pages in new tabs will also stall.*

Pour résoudre ce problème, **il suffit donc de faire un appel à session_write_close() juste après l'appel à session_start()**. Ainsi, la variable $_SESSION sera initialisée puis la session sera immédiatement fermée pour libérer les autres pages.

Notes
=====

  * Il existe d'autres moyens de permettre au serveur d'envoyer des données à un client sans que celui-ci les demande. Les [WebSockets](http://fr.wikipedia.org/wiki/Websocket) (avec notamment [socket.io](http://socket.io/#how-to-use)) sont certainement l'avenir...
  * PHP n'est certainement pas le langage le plus adapté pour réaliser une communication du serveur vers le client de manière performante.
