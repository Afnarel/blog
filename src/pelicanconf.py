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

TWITTER_USERNAME = 'Afnarel'
GITHUB_URL = 'https://github.com/Afnarel'

DISQUS_SITENAME = 'afnarelsblog'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'resources']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

###########
# Theming #
###########
THEME = "../themes/pelican-elegant"
RECENT_ARTICLES_COUNT=15

COMMENTS_INTRO="""Feel free to comment  below."""

#############
# To see... #
#############
#DEFAULT_DATE_FORMAT = '%Y-%m-%d'
#DEFAULT_DATE = 'fs'
#MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
#DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
#TAG_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''
#AUTHOR_SAVE_AS = ''

LANDING_PAGE_ABOUT={
    'title' : 'Question everything, Learn something, Answer nothing',
    'details' : """My name is François CHAPUIS. I recently got a Master's degree in Computer Science from Polytech Nice-Sophia in France. I am mostly interested in the Python programming language and in low-level C development. I've been using the GNU/Linux operating system since 2001. I love everything that makes me think, therefore I often take part in programming challenges, online or offline. I'm also very keen on learning new technologies and keeping up to date with the latest evolutions."""
}

PROJECTS=[
    {
        'name': 'Some project 1 (coming...)',
        'url' :'',
        'description' : """Project description"""
    },
    {
        'name': 'Some project 2 (coming...)',
        'url' : '',
        'description' : """Project description"""
    }
]

# Appears before the licence and after site name
SITESUBTITLE=""
SITE_LICENSE = """<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>."""
