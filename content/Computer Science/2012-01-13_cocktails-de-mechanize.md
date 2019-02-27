Title: Cocktails de mechanize, webbrowser et PIL
Date: 2012-01-13 19:51
Tags: pelican, publishing
Author: François Chapuis

 Aujourd'hui, j'avais besoin de récupérer une liste de cocktails. J'en ai trouvé une assez jolie sur ce site mais avec un cocktail par page. Du coup, comme j'avais du temps à perdre (:p), j'ai décidé d'écrire un petit script pour les récupérer sous forme d'images de même taille. Comme je pense que c'est un script intéressant qui utilise 3 modules différents (mechanize pour récupérer les liens des différentes pages, webbrowser pour les ouvrir dans un navigateur et le module ImageGrab de la Python Imaging Library pour faire les captures d'écran) de manière plutôt compacte, je le publie. Je suis sûr qu'il y a des méthodes plus simples et plus propres de faire ça et je serais intéressé de les connaître. J'ai seulement pris la première solution qui m'est venue à l'esprit.

~~~python
# -*- coding:utf-8 -*-
 
from PIL import ImageGrab
import time
from mechanize import mechanize
import webbrowser
 
def grab_screen(filename):
  image = ImageGrab.grab((20,210,600,500))
  image.save(filename + '.png')
 
def get_cocktails():
  BASE = 'http://www.iba-world.com'
  LIKE = '/index.php?option=com_content&id='
  url = 'http://www.iba-world.com/index.php?option=com_content&view=article&id=88&Itemid=532#'
  browser = mechanize.Browser()
  page = browser.open(url)
  #print page.read()
  print dir(browser)
  for l in browser.links():
    if l.url.startswith(LIKE):
      page_url = BASE + l.url
      num = l.url[len(LIKE):]
      num = num[:num.index('&')]
      print num, page_url
      webbrowser.open_new_tab(page_url)
      time.sleep(5)
      grab_screen(num)
 
if __name__ == '__main__':
  get_cocktails()
~~~

Pour l'utiliser, il faut adapter les coordonnées de la zone à capturer en fonction de votre navigateur.

Le code est [ici]({static}/resources/120113/grabcocktails.py) et les [images]({static}/resources/120113/cocktails.zip) récupérées sont là.