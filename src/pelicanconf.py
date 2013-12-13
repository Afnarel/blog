#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Afnarel'
SITENAME = u"Afnarel's blog"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

ARTICLE_URL = '{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}-{date:%m}-{date:%d}-{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Catwell\'s journal', 'http://blog.separateconcerns.com/'),
          ('Arnaud\'s blog', 'http://geenux.wordpress.com/'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://fr.linkedin.com/in/afnarel'),
          ('Twitter', 'http://twitter.com/#!/Afnarel'),
          ('Google+', 'https://plus.google.com/+FrançoisCHAPUIS'),
          ('Delicious', 'http://delicious.com/afnarel'),
          ('Github', 'https://github.com/Afnarel/'),
          ('Bitbucket', 'https://bitbucket.org/Afnarel'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'resources']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
