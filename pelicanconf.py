#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR =u'Adriano Albert' 
SITENAME =u'Adriano Albert Muniz' 
TAGLINE =u'Computer Networking and More'
SITEURL = 'https://adrianomuniz.com'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

#DATE_FORMATS={'en': '%a, %d %b %Y',
#    'jp': '%Y-%m-%d(%a)',
#}

#LOCALE = (
#   'en_US', 'ja_JP')     


DEFAULT_LANG = u'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#MENUITEMS = [('Archive', '/archives.html'),]

MENUITEMS = [('Posts', ''), ('About', '/pages/about.html'), ('Publications', '/pages/publications.html'),]

STATIC_PATHS = ['images', 'pdfs']


COVER_IMG_URL = '/images/cover-image.jpg'
#COVER_IMG_URL = './images/IMG_6992.jpg'
#PROFILE_IMAGE_URL = './images/IMG_0636.jpg'

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/adrianoalbert'),
          ('github', 'https://github.com/adrianoalbert'),)

#     ('linkedin', 'https://www.linkedin.com/pub/adil-moujahid/65/51/83a'),
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

#Set Disqus sitename
DISQUS_SITENAME = "adrianomuniz"
GOOGLE_ANALYTICS = "UA-127399943-1"
#ADDTHIS_PROFILE = "ra-54c667f5423e719f"
# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"


# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'extra']

# Ipython setting
NOTEBOOK_DIR = 'notebooks'
#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output'))]


# Shift the installed location of a file
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

DEFAULT_PAGINATION = 10

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = False

# Specify theme
THEME = "theme/pure"


# Plugins
#PLUGINS = ['liquid_tags.youtube', 'liquid_tags.img', 'liquid_tags.notebook']
#PLUGIN_PATHS = ['./plugins']
#PLUGINS = ['gravatar', 'liquid_tags.youtube', 'liquid_tags.img', 'liquid_tags.notebook']

PLUGIN_PATHS = ['./plugins']

MARKUP = ('md', 'ipynb')


PLUGINS = ['gravatar', 'liquid_tags.youtube', 'liquid_tags.img', 'pelican_gist', 'ipynb.liquid', 'pelican_javascript']


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
