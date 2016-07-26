# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'zhs'

DATE_FORMATS = {
    'zhs': ((u'en_US', 'utf8'), u'%a, %d %b %Y',),
    #~ 'zhs': ((u'zh_CN', 'utf8'), u'%Y年%m月%d日(周%a)',),
}

SITENAME = "mx's Blog"
AUTHOR = 'mx'

DISQUS_SITENAME = 'xweisblog'
GITHUB_URL = 'https://github.com/X-Wei'
SITEURL = 'http://x-wei.github.io'
GOOGLE_ANALYTICS = 'UA-30756331-1'
TAG_FEED_ATOM  = 'feeds/%s.atom.xml'
TAG_CLOUD_STEPS = 4
FEED_RSS = 'feeds/all.rss.xml'
DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY ='MISC'
OUTPUT_PATH = '.'
#~ RELATIVE_PATH='true'
RELATIVE_URLS=1
STATIC_PATHS = ["static"]
PATH = 'posts'
THEME='./pelican-themes/bs6'

REVERSE_ARCHIVE_ORDER=True

LINKS = (('dofine', 'http://log.dofine.me/'),
         ('farseerfc', "http://farseerfc.github.com/"),
         ('H.Y.', "http://hyhx2008.github.com/"),
         ('reginald1787', 'http://reginald1787.github.io/')
         )

SOCIAL = (
          ('github', 'https://github.com/x-wei'),
          )
          #('twitter', 'http://twitter.com/farseerfc'),
          #~ ('facebook', 'http://www.facebook.com/farseerfc'),
          #~ ('weibo', 'http://weibo.com/farseerfc'),
          #~ ('renren', 'http://www.renren.com/farseer'),
          
GOOGLE_CUSTOM_SEARCH_SIDEBAR = "010017366155264590731:njcqykcxuly"
       
#把各种网页小工具(比如倒计时, 微博展示......)的html代码放在这里 不过要使用farseerfc同学制作的bootsrtap2主题(太赞啦!!)
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
<li class="widget-container widget_text">
<h3 class="widget-title">推荐文章</h3>
<div class="textwidget">

<a href="http://x-wei.github.io/%E8%BF%90%E7%AD%B9%E7%9A%84%E5%8A%9B%E9%87%8F:%20%E7%94%A8%E7%BA%BF%E6%80%A7%E8%A7%84%E5%88%92%E8%A7%A3%E5%86%B3Google%202014%20HashCode%E9%97%AE%E9%A2%98.html">运筹的力量: 用线性规划解决Google 2014 HashCode问题</a><br>
<a href="http://x-wei.github.io/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E5%85%A5%E9%97%A8%E7%AE%80%E4%BB%8B.html">正则表达式入门简介</a><br>
<a href="http://x-wei.github.io/%E6%88%91%E7%9A%84ubuntu10.04%E9%85%8D%E7%BD%AE%E6%80%BB%E7%BB%93.html">我的ubuntu10.04配置总结</a><br>
<a href="http://x-wei.github.com/PT-summery.html">2011巴黎高科(ParisTech)申请总结</a><br>
<a href="http://x-wei.github.com/GT-summery.html">用尽量少的时间考一个够用的分数--一点Tofel/GRE备考经验</a><br>
<a href="http://x-wei.github.com/pelican_github_blog.html">用pelican在github上创建自己的博客!</a><br>
</div></li>

<br>
<li class="widget-container widget_text">
<h3 class="widget-title">About me</h3>
<div class="textwidget">
上海西南某高校电院毕业生, X2012.<br/>
</div></li>

<br>
<a href="https://www.polytechnique.edu/" target="_blank"><img src="http://x-wei.github.com/static/x-logo.png" alt="X" width="160" border="0" /></a><br/>

<br>
<a href="http://www.sjtu.edu.cn/"><img src="http://x-wei.github.com/static/ssss.jpg" border="0"alt="上海西南某高校"></a><br/>


<br>
<li class="widget-container widget_text">
<h3 class="widget-title">Who are Visiting</h3>
<div class="textwidget">
<script type="text/javascript" src="http://jf.revolvermaps.com/2/1.js?i=59olkba9w7e&amp;s=220&amp;m=3&amp;v=false&amp;r=false&amp;b=000000&amp;n=false&amp;c=ff0000" async="async"></script>
</div></li>

<!-- hitwebcounter Code START -->
<a href="http://www.hitwebcounter.com/how-to/how-to-what-is-free-blog-counter.php" target="_blank">
<img src="http://hitwebcounter.com/counter/counter.php?page=5954927&style=0036&nbdigits=5&type=ip&initCount=0" title="web counter" Alt="web counter"   border="0" >
</a><br/>



"""


