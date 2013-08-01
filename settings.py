# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'zhs'

SITENAME = "mx's Blog"
AUTHOR = 'mx'

DISQUS_SITENAME = 'xweisblog'
GITHUB_URL = 'https://github.com/X-Wei'
#~ SITEURL = 'http://x-wei.github.com'
GOOGLE_ANALYTICS = 'UA-30756331-1'
TAG_FEED_ATOM  = 'feeds/%s.atom.xml'
TAG_CLOUD_STEPS = 4
FEED_RSS = 'feeds/all.rss.xml'
DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY ='MISC'
OUTPUT_PATH = '.'
#~ RELATIVE_PATH='true'
RELATIVE_URLS=1
STATIC_PATHS = ["static", ]
PATH = 'posts'
THEME='./pelican-themes/bs6'

#~ REVERSE_ARCHIVE_ORDER=0

LINKS = (('dofine', 'http://log.dofine.me/'),
         ('farseerfc', "http://farseerfc.github.com/"),
         ('H.Y.', "http://hyhx2008.github.com/"),
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
SIDEBAR_CUSTOM=ur"""
<br>
<Script Language="JavaScript"> 
var timedate= new Date("June 22,2013"); 
var now = new ate(); 
var date = now.getTime() - timedate.getTime(); 
var time = Math.floor(date / (1000 * 60 * 60 * 24)); 
if (time >= 0) ;
document.write("<p style='text-align: center'><strong><font style='color:black;font-size:36px;'>"+time +"</font></strong> days<br/><strong>since GRADUATION from<br/> Shanghai Jiao Tong University</strong></p>");
</Script>

<br>
<a href="http://www.ubuntu.com/"><img src="http://www.ubuntu.com/countdown/banner1.png" border="0" width="180" height="150" alt="The next version of Ubuntu is coming soon"></a><br/>

<br>
<a href="http://www.sjtu.edu.cn/"><img src="http://x-wei.github.com/static/ssss.jpg" border="0"alt="上海西南某高校"></a><br/>

<br>
<li class="widget-container widget_text">
<h3 class="widget-title">About me</h3>
<div class="textwidget">
上海西南某高校电院学生, Linux桌面低端用户.<br/>
</div></li>

<br>
<li class="widget-container widget_text">
<h3 class="widget-title">推荐文章</h3>
<div class="textwidget">
<a href="http://x-wei.github.com/PT-summery.html">2011巴黎高科(ParisTech)申请总结</a><br>
<a href="http://x-wei.github.com/GT-summery.html">用尽量少的时间考一个够用的分数--一点Tofel/GRE备考经验</a><br>
<a href="http://x-wei.github.com/google_youku_host_20120706.html">[更新]访问google服务和优酷去广告功能的host列表</a><br>
<a href="http://x-wei.github.com/chrome-background.html">chrome护眼设置--把背景设置为绿豆沙</a><br>
<a href="http://x-wei.github.com/xelatex_zh.html">xelatex--linux下tex中文的完全解决!</a><br>
<a href="http://x-wei.github.com/google_doc_form.html">使用google doc建立在线调查表!~</a><br>
<a href="http://x-wei.github.com/pelican_github_blog.html">用pelican在github上创建自己的博客!</a><br>
</div></li>

"""

#~ <br>
#~ <object type="application/x-shockwave-flash" style="outline:none;" data="http://hosting.gmodules.com/ig/gadgets/file/112581010116074801021/hamster.swf?" width="300" height="225"><param name="movie" value="http://hosting.gmodules.com/ig/gadgets/file/112581010116074801021/hamster.swf?"></param><param name="AllowScriptAccess" value="always"></param><param name="wmode" value="opaque"></param></object>
#~ <br>

#gtalk
#<iframe src="http://www.google.com/talk/service/badge/Show?tk=z01q6amlq8n8dcqb7mphiivq299uh917bh2sph4lo7rip701jaltqve59eica9opvmhfq5h7hm6i7jkdql1kqntt3h8mnto6ns9lt5960d4dhrvdo3963kv040g9344v6q2nslh6sgqnjp5l2oqspe7p29858omr5qthnm8lc&amp;w=200&amp;h=60" frameborder="0" allowtransparency="true" width="200" height="60"></iframe>
#~ TWITTER_USERNAME = 'farseerfc'

#~ PDF_GENERATOR = True

