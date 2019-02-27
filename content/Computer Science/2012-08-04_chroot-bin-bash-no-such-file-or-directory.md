Title: chroot: cannot execute /bin/bash: no such file or directory
Date: 2012-08-04 20:12
Tags: chroot
Author: François Chapuis

Lors d'une mise à jour d'Archlinux il y a quelques jours, je me suis retrouvé avec un kernel panic au démarrage. Sur le coup, je me suis dit "aucun problème, un petit coup de chroot à partir d'un liveCD devrait faire l'affaire". Le problème, c'est que quand j'ai essayé de chrooter, j'ai obtenu l'erreur suivante :

> chroot: cannot execute /bin/bash: no such file or directory

ou, en français :

> chroot: impossible dexécuter la commande /bin/bash: Aucun fichier ou dossier de ce type

Heureusement, [ce post](http://forums.archlinux.fr/topic11377.html) de tuxce (que je remercie au passage pour toutes les excellentes solutions qu'il donne, car ce n'est pas la première fois qu'un de ses posts m'aide à résoudre un problème) explique que **/lib/ est maintenant un simple lien symbolique vers /usr/lib/**.

Pour que le chroot fonctionne, **il faut supprimer** (ou renommer) **le dossier lib** de la partition sur laquelle se trouve la racine du système défectueux (jail) **et créer le lien symbolique de usr/lib vers lib** :

  * mv lib lib.old
  * ln -sf usr/lib/ lib

<u>Note 1</u> : si par contre l'erreur que vous rencontrez est *chroot: cannot run command '/bin/bash': Exec format error*, alors c'est que vous essayez de chrooter dans un système 64bits depuis une distribution 32bits, comme expliqué sur le [wiki d'ArchLinux](https://wiki.archlinux.org/index.php/Change_Root)...

<u>Note 2</u> : apparemment, certaines personnes ont dû faire un **mkinitcpio -p linux** (voir [ici](http://www.archlinux.org/news/systemd-tools-replaces-udev/)) après cette mise à jour. Dans mon cas, d'après ce que j'ai vu dans les logs, pacman l'a fait tout seul.
