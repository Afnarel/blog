Title: SSHMaster : contrôler un cluster de machines via SSH
Date: 2013-06-07 21:47
Tags: SSH, paramiko
Author: François Chapuis

Cela fait maintenant un moment que j'avais envie d'avoir un moyen simple de distribuer des commandes sur un grand nombre de machines différentes, par exemple pour distribuer des calculs puis récupérer les résultats.

Je viens de publier mon premier projet public sur Bitbucket : [SSHMaster](https://bitbucket.org/Afnarel/sshmaster/overview). Le code essentiel qui permet d'exécuter une commande sur une machine sur SSH n'est pas de moi : je l'ai récupéré [ici](http://media.commandline.org.uk/code/ssh.txt) et il utilise lui-même le module python [paramiko](http://www.lag.net/paramiko/). Je me suis contenté d'une part de développer une surcouche objet et d'aute part de gérer plusieurs machines à la fois.

Le code est organisé en 3 fichiers principaux :

  * Connection.py contient le code que j'ai récupéré, qui permet d'exécuter une commande, d'envoyer un fichier ou de récupérer un fichier.
  * Machine.py fait exactement la même chose mais en orienté objet :

~~~python
machine = Machine('some.host.com', '~/.ssh/id_rsa', 'john') # IP, Clé SSH, login (default login is 'root')
machine.connect()
if machine.is_alive():
    print machine.get_ip()
    print machine.execute('ls -l | grep *.txt') # Une seule commande
    print machine.execute(['date', 'pwd']) # Plusieurs commandes l'une après l'autre
    machine.get('some/remote/file.txt', '/some/local/path/') # Le chemin local peut être omis
    machine.put('some/local/file.txt', '/some/remote/path/') # Le chemin distant peut être omis
    machine.end_connection()
~~~

   * Cluster.py s'occupe de gérer plusieurs machines :

~~~python
ips = ['some.host1.com', 'some.host2.com']
cluster = Cluster(ips, '~/.ssh/id_rsa', 'john')
cluster.show_state()
       
machine = Machine('some.host.com', '~/.ssh/id_rsa', 'john')
cluster.add_machine(machine) # La connexion avec la machine est établie si ce n'était pas le cas
               
print cluster.execute('ls') # Une seule commande
print cluster.execute(['date', 'pwd']) # Plusieurs commandes l'une après l'autre
                       
cluster.get('some/remote/file.txt', '/some/local/path/') # Le chemin local peut être omis
cluster.put('some/local/file.txt', '/some/remote/path/') # Le chemin distant peut être omis
                               
machines = cluster.get_machines() # Récupère toutes les Machines du cluster
alive_machines = cluster.get_alive_machines() # Récupère les Machines du cluster avec lesquelles une connexion est ouverte
dead_machines = cluster.get_dead_machines() # Récupère les Machines du cluster avec lesquelles aucune connexion n'est ouverte
                                           
# Dès qu'une machine est ajoutée au cluster, une connexion est établie avec elle. La méthode connect() de Cluster
# ne devrait donc jamais être utilisée. Elle reconnecte toutes les machines qui font partie du cluster mais avec
# lesquelles aucune connexion n'est établie.
cluster.connect()
       
cluster.end_connections()
~~~

Ce script peut bien sûr être amélioré :

  * Il serait pratique de créer un réel script *main.py* avec des paramètres tels que les commandes à lancer et les triplets machine/login/clé ssh permettant de savoir sur quelles machines lancer les commandes.
  * Pouvoir ajuster les commandes lancées en fonction de chaque machine serait aussi utile : on pourrait par exemple donner des paramètres tels que 1-30 à la première machine pour qu'elle traite les 30 premières données et 31-60 à la seconde pour qu'elle traite les 30 suivantes.

Je m'occuperai peut-être de rajouter ces fonctionnalités si j'en ai besoin. En attendant, si vous avez envie de le faire, n'hésitez pas et partagez ;). Si vous avez d'autres idées d'améliorations, ça m'intéresse aussi :)
