Title: Correction des checksums UDP et TCP avec libpcap 
Date: 2011-11-28 14:03
Tags: libpcap, checksums
Author: François Chapuis

 J'ai terminé hier soir un projet de réseau qui consistait à analyser les paquets récupérés avec Wireshark ou tcpdump dans un fichier .pcap, à récupérer les paquets UDP et TCP, calculer leurs checksums, les comparer aux checksums des paquet, les corriger s'ils étaient incorrects, et sauvegarder les paquets corrigés dans un nouveau fichier .pcap. Pous pouvez aller voir [le sujet détaillé](http://www.i3s.unice.fr/~lopezpac/cours/2011/IntRes/projet.html) pour plus d'information (changez l'encodage de la page pour UTF-8).

Vous pouvez [télécharger]({filename}/resources/111128/pcap_reader.tgz) une archive contenant le code accompagné d'un README et de fichiers pcap d'exemple. Le code est également disponible sur [Github](https://github.com/Afnarel/pcap_reader).

Voilà quelques liens vers des pages utiles :

  * [FrameIP](http://www.frameip.com/entete-udp/#3.4_-_Checksum)
  * [Le code de tcpreplay](http://tcpreplay.synfin.net/browser/trunk/src/) (voir les fichiers tcpedit/checksum.c, tcpedit/tcpedit.c et tcprewrite.c
  * [Le blog de Stéphane Bortzmeyer](http://www.bortzmeyer.org/search?pattern=pcap)
  * [La page de pcap sur le site de tcpdump](http://www.tcpdump.org/pcap.html) (et particulièrement le code de [sniffex.c](http://www.tcpdump.org/sniffex.c))
