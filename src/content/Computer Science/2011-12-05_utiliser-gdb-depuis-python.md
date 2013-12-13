Title: Utiliser GDB depuis Python
Date: 2011-12-05 20:14
Tags: GDB, Python
Author: François Chapuis

Il y a quelques temps, j'ai voulu pouvoir utiliser le debugger [GDB](http://www.gnu.org/s/gdb/) depuis un script Python en utilisant le module subprocess. J'ai longtemps essayé de résoudre un problème de pipe avant de trouver [ce thread](http://forum.hardware.fr/hfr/Programmation/Python/automatisation-application-externe-sujet_125890_1.htm) qui m'a donné la solution. J'ai donc réutilisé ce code pour en faire une classe simple :

~~~python
from subprocess import *
 
class GDB:
 
  def __init__(self, pathToGdb):
    self.GDB_PROMPT = '(gdb) '
    self.GDB_CMDLINE = pathToGdb
    self.gdbProcess = Popen(self.GDB_CMDLINE , 0, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    self.read_until_prompt()
   
  def read_until_prompt(self):
    buf = ''
    while(True):
      ch = self.gdbProcess.stdout.read(1)
      if not ch:
        return buf
      buf += ch
      if len(buf) < len(self.GDB_PROMPT):
        continue
      if buf.endswith(self.GDB_PROMPT):
        outlen = len(buf) - len(self.GDB_PROMPT)
        return buf[:outlen]
   
  def send(self, cmd):
    self.gdbProcess.stdin.write(cmd + 'n')
    output = self.read_until_prompt()
    return output
   
  def quit(self):
    self.send('quit')
~~~

Cette classe s'utilise très simplement de la manière suivante :

  * On créé un objet GDB auquel on passe le chemin vers l'exécutable de GDB en paramètre ;
  * On utilise la méthode **send()** de cet objet pour exécuter une commande et en obtenir éventuellement le retour ;
  * On ferme GDB en utilisant la méthode **quit()**.

Par exemple :

~~~python
from GDB import GDB
 
if __name__ == '__main__':
  exe = 'crackme.exe'
  gdb = GDB('gdb.exe')
 
  # Ouverture du fichier a debugger
  gdb.send('file ' + exe)
   
  gdb.send('b strcmp')
  gdb.send('r toto')
   
  print gdb.send('info registers')
  print gdb.send('p/x $eax')
   
  out = gdb.send('x 0x28ff04')
  print out
   
  # On quitte GDB
  gdb.quit()
~~~

Je partage ce code parce que j'ai eu beaucoup de mal à réussir à faire cela et je pense qu'il peut être utile à beaucoup de développeurs... Vous pouvez télécharger [une archive]({filename}/resources/111205/python_gdb.zip) qui contient un exécutable de GDB pour Windows, la classe GDB, un programme crackme.exe sur lequel sont réalisés des tests et le fichier main.py qui contient ces tests...