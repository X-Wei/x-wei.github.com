#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bruno Adele'
#AUTHOR_LINK = "http://bruno.adele.im"
#AUTHOR_IMG = "http://bruno.adele.im/static/bruno.jpg"
SITENAME = u'Pelicanthemes'
SITEURL = 'http://localhost:8000'
#SITESUBTITLE = 'Une famille complètement 633<'
#GITHUB_BLOG_SITE = 'https://github.com/badele/blog.jesuislibre.org'
#DISQUS_SITENAME = 'blogdejesuislibreorg'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'fr'


# URL
#ARTICLE_URL = '{date:%Y}/{date:%-m}/{date:%-d}/{slug}'
#ARTICLE_SAVE_AS = '{date:%Y}/{date:%-m}/{date:%-d}/{slug}/index.html'
#TAG_URL = 'tags/{slug}/'
#TAG_SAVE_AS = 'tags/{slug}/index.html'
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
DEFAULT_PAGINATION = 5
RELATIVE_URLS = True

# Feed generation is usually not desired when developing
#FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = 'feed.atom'
#TAG_FEED_ATOM = 'tags/%s/feed.atom'
#FEED_MAX_ITEMS = 10

# Links
LINKS = (('Home', '/'), ('archives', '/archives.html'), ('tags', '/tags.html'), ('A propos', 'http://bruno.adele.im'))

#Social widget
SOCIAL = (
    ('adele', 'http://adele.im'),
    ('feed', 'http://feeds.feedburner.com/FamilleDeGeek'),
    ('twitter', 'http://twitter.com/jesuislibre.org'),
    ('google+', 'https://plus.google.com/100723270029692582967'),
    ('blog', 'http://blog.jesuislibre.org'),
    ('facebook', 'http://www.facebook.com/bruno.adele'),
    ('flickr', 'http://www.flickr.com/photos/b_adele'),
    ('linkedin', 'http://fr.linkedin.com/in/brunoadele'),
)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
# static paths will be copied without parsing their contents
STATIC_PATHS = [
     'static',
 ]

#Piwik
# PIWIK_SERVER = 'analytics.cendreo.com'
# PIWIK_ID = 4
