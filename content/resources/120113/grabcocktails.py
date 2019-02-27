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
