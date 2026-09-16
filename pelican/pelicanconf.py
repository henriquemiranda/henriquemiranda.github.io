#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Henrique Miranda'
SITENAME = 'Henrique Miranda'
SITESUBTITLE = 'Physics, Materials science... with python, C, Fortran and Javascript'
SITEURL = 'https://henriquemiranda.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

DEFAULT_CATEGORY = 'About Me'

OUTPUT_PATH = 'output'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_PAGES_ON_MENU = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'))

SOCIAL = (
    ('GitHub', 'https://github.com/henriquemiranda'),
    ('LinkedIn', 'https://www.linkedin.com/in/mirandahenrique/'),
    ('Google Scholar', 'https://scholar.google.com/citations?user=S9EaNyYAAAAJ&hl=en'),
    ('ORCID', 'https://orcid.org/my-orcid?orcid=0000-0002-2843-0876'),
)

STATIC_EXCLUDE_SOURCES = False
PAGE_PATHS = ['pages']
#STATIC_PATHS = ['images']
#MENUITEMS = [('About Me','../index.html')]

LOAD_CONTENT_CACHE = False
THEME='miranda'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
READERS = {'html': None}
