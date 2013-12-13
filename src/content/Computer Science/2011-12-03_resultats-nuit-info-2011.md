Title: Résultats de la Nuit de l'Info 2011
Date: 2011-12-03 13:17
Tags: Nuit de l'Info, challenge
Author: François Chapuis

 Mon équipe, les [Fruits du Chêne](http://www.nuitdelinfo.com/nuitinfo11/teams:les_fruits_du_cheene:start), a finie :

  * 1ère au défi Google Cloud (Google App Engine), grâce à [Alexis Daboville](https://plus.google.com/109687268386376441170/posts) qui a réalisé ce défi depuis l'Irlande !
  * 1ère au défi Zenika (Méthodes Agiles), grâce à son excellent manager, Jérémie Fabre !
  * 2ème au défi W3C (accessibilité du site).
  * 3ème au défi FLOSS ARDUINO INRIA (développement collaboratif Open Source).

Le site réalisé est visible [ici](http://leslapinous.unevu.com/), et son code source [là](https://github.com/Afnarel/Nuit-de-l-Info-2011/). Il a été développé en utilisant un framework PHP minimaliste utilisant le pattern MVC créé par Antoine ([yellowiscool](http://www.blogjaune.fr/)). Pour le CSS, nous avons utilisé [bootstrap](http://twitter.github.com/bootstrap/). On a utilisé l'[API Facebook](http://developers.facebook.com/docs/reference/api/) pour la connexion et la récupération des données, cause des deux problèmes importants auxquels on s'est heurtés :

  1. il semble impossible d'utiliser un formulaire de connexion personnalisé : on est forcément redirigés sur une page de Facebook et, une fois connectés, redirigés sur une page de notre site.
  2. lorsque l'on souhaite récupérer des informations telles que les anniversaires de nos amis, la récupération prend un temps extrêmement long (alors que la récupération des amis est relativement rapide).

De plus, je trouve l'API limitée. Par exemple, pour récupérer les noms de mes amis, je m'attendais à pouvoir écrire [https://graph.facebook.com/me/friends/name](https://graph.facebook.com/me/friends/name) (comme on pourrait le faire avec une syntaxe [XPath](http://www.w3schools.com/xpath/xpath_examples.asp)). Ce n'est malheureusement pas le cas. Pour faire cela, on est obligé de récupérer nos amis ([https://graph.facebook.com/me/friends](https://graph.facebook.com/me/friends)) puis de faire une boucle pour récupérer le nom de chaque ami... Si vous voulez tester cela, vous pouvez utiliser le [Graph API Explorer](https://developers.facebook.com/tools/explorer), un outil bien pratique.

Cette nuit m'a quand même permis d'apprendre à utiliser cette API, chose que je voulais faire depuis longtemps, donc ça n'a pas été une perte de temps. Ça m'a aussi donné envie de découvrir les API d'autres services comme Google et Amazone.

Les rendus pour chacun des défis auxquels nous avons participé sont ici :

  * [FOSS INRIA](http://www.nuitdelinfo.com/nuitinfo11/defis:inria) : [Rapport]({filename}/resources/111203/Inria_FOSS_Arduino_-_Les_Fruits_du_Chêne.pdf)
  * [Logica (Sophia)](http://www.nuitdelinfo.com/nuitinfo11/defis:logica-sophia) : [Rapport]({filename}/resources/111203/logica.pdf)
  * [Super Twitter](http://www.nuitdelinfo.com/nuitinfo11/defis:super-twitter) : [Rapport]({filename}/resources/111203/super_twitter.pdf)
  * [Zenika](http://www.nuitdelinfo.com/nuitinfo11/defis:zenika) : [Rapport]({filename}/resources/111203/Zenika.zip)
  * [Google Cloud](http://www.nuitdelinfo.com/nuitinfo11/defis:google-cloud) : [Rapport]({filename}/resources/111203/GiftIdeas.pdf) et [code](https://github.com/Afnarel/Nuit-de-l-Info-2011/tree/master/gae2)
  * [AKKA](http://www.nuitdelinfo.com/nuitinfo11/defis:akka) : [Rapport]({filename}/resources/111203/Akka.zip)
  * [W3C](http://www.nuitdelinfo.com/nuitinfo11/defis:w3c) : [Rapport]({filename}/resources/111203/W3C_-_Les_Fruits_du_Chêne.pdf)
  * [ABASE](http://www.nuitdelinfo.com/nuitinfo11/defis:abase) : [Rapport]({filename}/resources/111203/ABASE.pdf)