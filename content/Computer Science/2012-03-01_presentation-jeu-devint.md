Title: Présentation du jeu DeViNT « Songe »
Date: 2012-03-01 16:15
Tags: Java, DeViNT, Accessibility
Author: François Chapuis

L'année dernière, dans le cadre de mes études à Polytech'Nice Sophia, j'ai développé avec deux amis (Roman Mkrtchian et Guy Champollion) un jeu vidéo destiné aux déficients visuels. Une version du jeu (avec quelques bugs) est visible [ici, sous forme de Java Web Start]({static}/resources/120301/songe.jnlp).

À propos du projet
==================

Nous avons développé « Songe » dans le langage Java et l’avons présenté deux fois à des enfants malvoyants :

  * Une première fois à l’[Institut d’Éducation Sensorielle « Clément Ader »](http://goo.gl/fGgyI) à Nice pour obtenir des critiques de la part des enfants concernés.
  * Une seconde fois lors des [journées DeViNt](http://devint.polytech.unice.fr/), le 26 mai 2011 (un mois plus tard), pour présenter une version corrigée du jeu.

Le jeu est actuellement sous licence libre GPLv3. Notre souhait est qu’il rassemble une communauté de personnes issues de différents domaines (développeurs, graphistes, musiciens, enseignants, chercheurs…) autour de la problématique de l’accessibilité à des personnes malvoyantes ou non-voyantes.

Dans cette optique, nous avons lancé des appels à contribution [sur le Site du Zéro](http://www.siteduzero.com/forum-83-619162-p1-jeu-2d-jeu-de-plateforme-rpg-pourmalvoyants.html) et sur le site [http://www.jeuxvideo.com/](http://www.jeuxvideo.com/). Nous avons également créé un [site](http://songe.project.free.fr/) et un [forum](http://songe.project.free.fr/forum). Cette communication a porté ses fruits car nous avons obtenu la participation d’un scénariste et d’un musicien. Nous aimerions obtenir l’aide d’un graphiste, de préférence familier avec les problématiques liées à la déficience visuelle, mais nous avons pour l’instant dû nous débrouiller par nos propres moyens.

Principe du jeu
===============

Songe est un jeu d’aventure ludique. Le joueur peut choisir d’incarner différents personnages. En fonction du personnage sélectionné et des choix qu’il fera au cours du jeu, le scénario sera différent.

Au cours de son aventure, le joueur peut rencontrer d’autres personnages, bons ou mauvais, et interagir avec eux. Ces personnages lui poseront des questions et ses réponses orienteront le scénario dans différentes directions. Les personnages rencontrés pourront aussi aider le joueur à réussir sa quête.

Les personnages peuvent également poser des questions ou des devinettes au joueur. Celles-ci lui permettent de remporter des points afin d’établir plus tard un classement de tous les joueurs.

Dans l’univers, il y a aussi des ennemis que le joueur doit combattre. Ces ennemis peuvent blesser le joueur et lui faire perdre des points.

Songe est avant tout un jeu de plateformes : le joueur devra donc franchir des obstacles en sautant des murs, en poussant des caisses, etc.

Pourquoi « Songe » est-il adapté aux déficients visuels ?
=========================================================

Le jeu propose de commencer par un tutoriel pour prendre en main la navigation dans le monde de « Songe ». Le joueur est guidé par une voix qui lui explique chaque étape en détails.

Les touches utilisées sont limitées au strict minimum et correspondent à l’utilisation qui est attendue d’elles : la touche droite permet d’avancer (la situation du personnage étant expliquée au début du jeu), la touche « échap » permet de quitter, etc.

Nous avons combiné l’utilisation d’une bibliothèque de synthèse vocale à des voix enregistrées par nous-mêmes afin de guider au mieux le joueur. S’il se trouve en difficulté, le joueur a toujours la possibilité d’obtenir une aide.

L’utilisation de la bibliothèque Java [Slick](http://slick.ninjacave.com/) qui permet de faire des jeux 2D, et de la bibliothèque [Phys2D](http://www.cokeandcode.com/phys2d/) ([@Google Code](http://code.google.com/p/phys2d/)) qui permet de simuler la physique en 2D (gravité, collisions), alliée à l’utilisation de la bibliothèque [OpenAL](http://kcat.strangesoft.net/openal.html) pour la gestion du son permet par exemple :

  * De faire varier le volume ou la hauteur d’un son lorsque le joueur se rapproche d’un obstacle ou d’un personnage : il est possible de positionner la source du son de façon à entendre les bruits comme si l’on se trouvait dans un environnement 3D ;
  * De jouer un son lorsqu’un joueur heurte un obstacle (un mur par exemple) ;
  * De jouer des musiques adaptées au contexte : nous avons par exemple décidé d’utiliser des musiques récurrentes pour différencier le menu, le jeu principal, les questions de scénario, les devinettes et les mini-jeux.

Les graphismes sont adaptés : couleurs vives et contrastés, grande taille.
