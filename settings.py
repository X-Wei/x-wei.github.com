# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Shanghai'

#~ DATE_FORMATS = {
    #~ 'en' : u'%a, %d %b %Y',
    #~ 'zh' : u'%Y-%m-%d',
    #~ 'zhs': u'%Y-%m-%d',
#~ }
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
#~ LOCALE = ['usa', 'cht', 'chs', 'jpn',        # windows
          #~ 'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
DEFAULT_LANG = 'zhs'

SITENAME = "X. Wei's Blog"
AUTHOR = 'X.Wei'

DISQUS_SITENAME = 'xweisblog'
GITHUB_URL = 'https://github.com/X-Wei'
SITEURL = 'http://x-wei.github.com'
GOOGLE_ANALYTICS = 'UA-30756331-1'
TAG_FEED  = 'feeds/%s.atom.xml'
#DEFAULT_ORPHANS=3
DEFAULT_PAGINATION = 4

DEFAULT_CATEGORY ='MISC'
OUTPUT_PATH = '.'
PATH = 'posts'
#~ THEME_STATIC_PATHS=['pelican-themes']
THEME='./pelican-themes/bs4'
#~ CSS_FILE = "font-awesome.css"

LINKS = (('dofine', 'http://www.dofine.me'),
         ('farseerfc', "http://farseerfc.github.com/"),
         )

SOCIAL = (
          ('github', 'https://github.com/x-wei'),
          )
          #('twitter', 'http://twitter.com/farseerfc'),
          #~ ('facebook', 'http://www.facebook.com/farseerfc'),
          #~ ('weibo', 'http://weibo.com/farseerfc'),
          #~ ('renren', 'http://www.renren.com/farseer'),
          
GOOGLE_CUSTOM_SEARCH_SIDEBAR = "010017366155264590731:njcqykcxuly"#终于被google收录了!~          
#把各种网页小工具(比如倒计时, 微博展示......)的html代码放在这里~ 不过要使用farseerfc同学制作的bootsrtap2主题(太赞啦!!)
SIDEBAR_CUSTOM=r"""
<a href="http://www.ubuntu.com/"><img src="http://www.ubuntu.com/countdown/banner1.png" border="0" width="180" height="150" alt="The next version of Ubuntu is coming soon"></a>

"""
#gtalk
#<iframe src="http://www.google.com/talk/service/badge/Show?tk=z01q6amlq8n8dcqb7mphiivq299uh917bh2sph4lo7rip701jaltqve59eica9opvmhfq5h7hm6i7jkdql1kqntt3h8mnto6ns9lt5960d4dhrvdo3963kv040g9344v6q2nslh6sgqnjp5l2oqspe7p29858omr5qthnm8lc&amp;w=200&amp;h=60" frameborder="0" allowtransparency="true" width="200" height="60"></iframe>
#~ TWITTER_USERNAME = 'farseerfc'
#~ SIDEBAR_CUSTOM = r"""
#~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
#~ src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1">
#~ </iframe>
#~ """

#~ GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"


#~ THEME='notmyidea'


#~ PDF_GENERATOR = True

