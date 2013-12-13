Title: Bootstrap : dropdown scrollable dans la navbar avec lionbars
Date: 2012-09-14 13:21
Tags: Bootstrap, LionBars
Author: François Chapuis

Hier, j'ai voulu mettre une jolie barre de scroll sur un menu déroulant (dropdown) dans la barre des menus (navbar) de [Bootstrap](http://twitter.github.com/bootstrap/). Je suis donc parti à la recherche de plugins jQuery et je suis tombé sur [LionBars](https://github.com/Charuru/lionbars) dont le style (qui imite celui de OS X Lion) m'a pas mal plu. Il permet de rendre facilement un élément jQuery scrollable en appelant la fonction **lionbars()** dessus.

1er problème
============

Le premier problème est que si on l'appelle sur une dropdown de Bootstrap, LionBars ne fonctionnera pas car le menu n'est pas visible. Il faut donc, pour régler ce problème, appeler la méthode lionbars() lors d'un clic sur l'élément qui déclenche l'apparition du menu et uniquement lorsque la div englobant la dropdown (qui a la classe "btn-group") possède la classe "*open*" (afin qu'elle ne soit pas appelée lorsqu'on referme le menu déroulant). C'est ce que fait ce script (*your-menu* est une classe rajoutée à la div englobant la dropdown afin d'identifier les dropdowns sur lesquelles LionBars est utilisé) :

~~~javascript
$(document).ready(function() {
    $('.your-menu a.dropdown-toggle').on('click', function() {
        var menu = $(this).parent();
        if(menu.hasClass('open')) {
            var menuContent = menu.find('ul.dropdown-menu');
            menuContent.lionbars();
        }
    });
});
~~~

2nd problème
============

Maintenant, LionBars fonctionne mais il y a un second problème : LionBars redéfinit le style CSS des listes non-ordonnées (ul), ce qui donne un résultat assez laid :

<center>![La liste déroulante mal alignée]({filename}/images/120914/lionbars_relative.png)</center>

Cela arrive car LionBars applique une position relative aux listes non-ordonnées tandis que Bootstrap leur applique un positionnement absolu. On peut régler simplement ce problème en rajoutant la ligne suivante après l'appel à la fonction lionbars() dans le script précédent :

~~~javascript
menuContent.css('position', 'absolute');
~~~

On se retrouve maintenant avec un menu qui ressemble à ça, ce qui n'est déjà pas si mal :

<center>![La liste déroulante bien alignée mais sans flêche]({filename}/images/120914/lionbars.png)</center>

3ème problème
=============

La barre de défilement s'affiche donc bien mais on remarque que la petite flèche qui est censée apparaître en haut du menu n'apparait plus. La raison de cette disparition est expliquée [sur cette page](http://www.eichefam.net/?p=4395) ainsi que le moyen de le régler : on va simplement recréer les styles appliqués aux éléments *before* et *after* des listes non-ordonnées :

~~~css
.your-menu ul.dropdown-menu {
    z-index: 0;
    height: 200px; /* You can change this value */
}
     
.your-menu.open > a.dropdown-toggle::before,
.your-menu.open > a.dropdown-toggle::after {
    content: '';
    display: inline-block;
    position: absolute;
    bottom: -9px; /* You can change this value */
}
     
.your-menu.open > a.dropdown-toggle::before {
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-bottom: 7px solid #CCC;
    border-bottom-color: rgba(0, 0, 0, 0.2);
    right: 7px;
}
.your-menu.open > a.dropdown-toggle::after {
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-bottom: 6px solid white;
    right: 8px;
    z-index: 1001;
}
~~~

Ces styles sont à peu de choses près les mêmes que ceux donnés dans la page mentionnée un peu plus haut. J'ai rassemblé les styles communs à *before* et *after* et j'ai fait en sorte que leur portée (scope) soit limitée aux dropdowns sur lesquelles est appliqué LionBars afin que les autres listes du site ne soient pas affectées. Il se peut que vous deviez modifier la propriété *bottom* qui définit la position verticale de la flêche pour l'adapter à la hauteur de votre barre de menus. La propriété *height* définit la hauteur maximale du menu déroulant. Pour éviter que les sous-menus mis en surbrillance lorsqu'ils sont survolés avec la souris débordent sur la barre de défilement, il suffit de rajouter une propriété *padding-right* (de 15px, par exemple) à la règle *.lb-content* dans lionbars.css

Le résultat obtenu est le suivant :

<center>![Le résultat final]({filename}/images/120914/lionbars_good.png)</center>

Code
====

J'ai créé un petit code de démonstration téléchargeable [ici]({filename}/resources/120914/scrollable_dropdown.zip).

Une démo du résultat est visible [ici]({filename}/resources/120914/scrollable_dropdown/index.html).
