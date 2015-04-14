#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'hnusr'
SITENAME = '人生如梦的博客'
SITEURL = ''
KEYWORD = 'android, java, web'

PATH = 'content'
STATIC_PATHS = [u"images"]

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'zh'

THEME = "F://python/pelican-themes/gum"

USE_FOLDER_AS_CATEGORY = True
FILENAME_METADATA = '(?P<slug>.*)'
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/index.html'
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu 
# MENUITEMS = (('首页', SITEURL),('分类', SITEURL),)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_PAGINATION = 13

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Github 
GITHUB_USER = 'xdays' 
GITHUB_REPO_COUNT = 5
