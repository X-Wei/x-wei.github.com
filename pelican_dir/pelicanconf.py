#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import getenv

AUTHOR = 'mx'
SITENAME = "mx's blog"

SITEURL = '//' + getenv("SITEURL", default='localhost:8000')

OUTPUT_PATH = 'output/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'zh'

LOCALE = 'zh_CN.utf8'

DATE_FORMATS = {
    'zh': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
}


DISQUS_SITENAME = 'xweisblog'
DISQUS_DISPLAY_COUNTS = False
GOOGLE_ANALYTICS = 'UA-30756331-1'



LINKS_SITE = (
    ('farseerfc', "http://farseerfc.github.com/"),
    ('H.Y.', "http://hyhx2008.github.com/"),
    ('reginald1787', 'http://reginald1787.github.io/'),
    ('dofine', 'http://log.dofine.me/'),
)

TAG_FEED_ATOM = None
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['pages',
                'static',
                'images',
                'images/favicon.ico',
                'static/CNAME']

EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'static/CNAME': {'path': 'CNAME'},
    'static/robots.txt': {'path': 'robots.txt'},
    'static/manifest.json': {'path': 'manifest.json'},
}

PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
PAGE_PATHS = ['pages']


# -------theme settings, see https://github.com/DandyDev/pelican-bootstrap3/wiki/Variables
THEME = "pelican-themes/pelican-bootstrap3"
DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
#~ SHOW_ARTICLE_CATEGORY = True

TYPOGRIFY = False
PYGMENTS_STYLE = 'native'
GITHUB_USER = 'x-wei'
GITHUB_SHOW_USER_LINK = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
CC_LICENSE = "CC-BY-NC-SA"
OUTPUT_SOURCES = False

DIRECT_TEMPLATES = (('search', 'index', 'categories', 'authors', 'archives','tags'))
AVATAR = 'images/mx.jpg'
ABOUT_PAGE = "about.html"
#~ SIDEBAR_IMAGES = ['_images/ssss.jpg', '_images/x-logo.png']
ABOUT_ME = ur"""
<h3 style="text-align:center">
<a href="https://github.com/x-wei" target="_blank">
<i class="fa fa-github" style="text-align:center"></i></a>
<a href="http://weibo.com/u/1817154611" target="_blank">
<i class="fa fa-weibo" style="text-align:center"></i></a>
<a href="mailto:xwei.mx@gmail.com" target="_blank">
<i class="mdi-communication-email" style="text-align:center"></i></a>
</h3>

<h4 class="widget-title">推荐文章</h4>
<div class="textwidget">
<li class="widget-container widget_text">
<a href="http://x-wei.github.io/%E8%BF%90%E7%AD%B9%E7%9A%84%E5%8A%9B%E9%87%8F:%20%E7%94%A8%E7%BA%BF%E6%80%A7%E8%A7%84%E5%88%92%E8%A7%A3%E5%86%B3Google%202014%20HashCode%E9%97%AE%E9%A2%98.html">运筹的力量: 用线性规划解决Google 2014 HashCode问题</a><br></li>
<li class="widget-container widget_text">
<a href="http://x-wei.github.io/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%85%A5%E9%97%A8%E7%AE%80%E4%BB%8B.html">正则表达式入门简介</a><br></li>
<li class="widget-container widget_text">
<a href="http://x-wei.github.io/%E6%88%91%E7%9A%84ubuntu10.04%E9%85%8D%E7%BD%AE%E6%80%BB%E7%BB%93.html">我的ubuntu10.04配置总结</a><br></li>
<li class="widget-container widget_text">
<a href="http://x-wei.github.io/PT-summery.html">2011巴黎高科(ParisTech)申请总结</a><br></li>
<li class="widget-container widget_text">
<a href="http://x-wei.github.io/GT-summery.html">用尽量少的时间考一个够用的分数--一点Tofel/GRE备考经验</a><br></li>
<li class="widget-container widget_text">
<a href="http://x-wei.github.io/pelican_github_blog.html">用pelican在github上创建自己的博客!</a><br></li>
</div>

<br><a href="https://www.polytechnique.edu/" target="_blank">
<img src="images/x-logo.png" alt="X" width="180" border="0" />
</a><br/>

<br><a href="http://www.sjtu.edu.cn/">
<img src="images/ssss.jpg" width="180" border="0" alt="上海西南某高校">
</a><br/>

<br>
<h4 class="widget-title">Who are visiting</h4>
<div class="textwidget" >
<script type="text/javascript" src="http://jf.revolvermaps.com/2/1.js?i=59olkba9w7e&amp;
s=180&amp;z=11&amp;m=3&amp;v=false&amp;r=false&amp;b=000000&amp;n=false&amp;c=ff0000" async="async">
</script></div>

<!-- hitwebcounter Code START -->
<a href="http://www.hitwebcounter.com/how-to/how-to-what-is-free-blog-counter.php" target="_blank">
<img src="http://hitwebcounter.com/counter/counter.php?page=5954927&style=0036&nbdigits=5&type=ip&initCount=0" title="web counter" Alt="web counter"   border="0" ></a>
<br/>
"""

# ------- end theme settings -------


# ------- plugin settings ----------
PLUGIN_PATHS = ['pelican-plugins']

MD_EXTENSIONS = ['admonition',
                 'toc',
                 'codehilite(css_class=highlight,linenums=False)',
                 'extra']

PLUGINS = [#"i18n_subsites",
           "better_codeblock_line_numbering",
           'tipue_search',
           'neighbors',
           'series',
           'bootstrapify',
           "render_math",
           'extract_toc',
           'tag_cloud',
           'sitemap',
           'summary']

SITEMAP = {
    'format': 'xml',
}

USE_LESS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
CHECK_MODIFIED_METHOD = "md5"
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True



