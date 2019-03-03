#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Afnarel'
SITENAME = "Afnarel's blog"
SITEURL = 'http://192.168.1.78:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

ARTICLE_URL = '{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}-{date:%m}-{date:%d}-{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Catwell\'s journal', 'http://blog.separateconcerns.com/'),
         ('Arnaud\'s blog', 'http://geenux.wordpress.com/'),)

# Social widget
SOCIAL = (('LinkedIn', 'http://fr.linkedin.com/in/afnarel'),
          ('Twitter', 'http://twitter.com/#!/Afnarel'),
          ('Github', 'https://github.com/Afnarel/'),
          ('Bitbucket', 'https://bitbucket.org/Afnarel'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'resources', 'extra']
EXTRA_PATH_METADATA = {
    # Move the .htaccess file to the root
    'extra/.htaccess': {'path': '.htaccess'},
    'extra/canalplus.php': {'path': 'canalplus.php'},
}

###########
# Plugins #
###########
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'neighbors']

# A bit useless since it is the default settings but Pelican raises
# warnings if the SITEMAP variable is not set...
SITEMAP = {
  'format': 'xml',
  'priorities': {
    'articles': 0.5,
    'indexes': 0.5,
    'pages': 0.5
  },
  'changefreqs': {
    'articles': 'monthly',
    'indexes': 'daily',
    'pages': 'monthly'
  }
}

#######################
# Markdown extensions #
#######################
# http://pythonhosted.org/Markdown/extensions/
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': True
        },
        'markdown.extensions.toc' :{
            'permalink' : 'true'
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # 'markdown.extensions.headerid': {},
        # 'markdown.extensions.toc': {},
    }
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

###########
# Theming #
###########
THEME = "./themes/elegant"
RECENT_ARTICLES_COUNT = 15
DIRECT_TEMPLATES = (('index', 'tags', 'categories',
                     'archives', 'search', '404'))
COMMENTS_INTRO = """Feel free to comment  below."""

# TAG_SAVE_AS = ''
# CATEGORY_SAVE_AS = ''
# AUTHOR_SAVE_AS = ''

LANDING_PAGE_ABOUT = {
    'title': 'Question everything, Learn something, Answer nothing',
    'details': """
Hi! My name is François CHAPUIS but I live on the internet under the very mysterious pseudonyme <b>Afnarel</b>.
In what some call real life and others <em>The Matrix</em>, I live in Antibes, on the French Riviera, next to Sophia Antipolis.
I am a former <a href="http://www.polytech.unice.fr/">Polytech Nice Sophia</a> student and <a href="https://www.ignilife.com/">Ignilife</a> employee.
I currently work remotely for <a href="http://www.nextmotion.net/">Nextmotion</a> and do some freelancing.
Forever GNU/Linux, Open Source and Python lover, I also greedily learn every new tech I come across.
I love everything that makes me think, therefore I often take part in programming challenges, online and offline.
"""
}

# PROJECTS = [
#     {
#         'name': 'Some project 1 (coming...)',
#         'url': '',
#         'description': """Project description"""
#     },
#     {
#         'name': 'Some project 2 (coming...)',
#         'url': '',
#         'description': """Project description"""
#     }
# ]

# Appears before the licence and after site name
SITESUBTITLE = ""
SITE_LICENSE = """<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>."""
