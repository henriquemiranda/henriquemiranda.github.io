#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Henrique Miranda'
SITENAME = 'Henrique Miranda'
SITESUBTITLE = 'Programming, Materials science... with python, C and Javascript'

#SITEURL = 'http://henriquemiranda.github.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Luxembourg'

DEFAULT_LANG = 'en'

GITHUB_URL = 'https://github.com/henriquemiranda'
DEFAULT_CATEGORY = 'About Me'


OUTPUT_PATH = '../'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'))

# Social
SOCIAL = (
    ('Github', 'https://github.com/henriquemiranda/'),
    ('Last.fm', 'http://www.last.fm/user/mirandahenrique'),
    ('linkedin', 'https://www.linkedin.com/in/mirandahenrique'))
#)

STATIC_PATHS = ['images']

LOAD_CONTENT_CACHE = False
THEME='miranda'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
READERS = {'html': None}
