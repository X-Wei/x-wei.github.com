Title: 在bolg页面上加入ubuntu发布倒计时图标
Date: 2012-04-25
Tags: pelican
Slug: 在bolg页面上加入ubuntu发布倒计时图标

明天ubuntu12.04**LTS**就要发布了! 然后今天下课回来在各种网站上闲逛, 突然发现了这个页面: [给网页添加ubuntu发布倒计时](http://www.ubuntu.com/community/countdown). 很厉害的样子, 介绍说只要把那一段代码加入网页的html文件就可以了. 我试了一下, 直接加在index.html上面--还真的可以唉~~

不过, pelican每次都是自动生成和更新index.html的啊, 难道每次都要手动加入这一行代码?? 难道还要自己修改pelican的代码??......

此时我想到了farseerfc学长的配置文件, 其中我把他的微博秀那几行注释掉了:

    #~ SIDEBAR_CUSTOM = r"""
    #~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
    #~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
    #~ src="<http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1>">
    #~ </iframe>
    #~ """

今天仔细一看, 我靠, `SIDEBAR_CUSTOM`不就是可以自定义的侧边栏么??!! 赶紧, 写上这样一行:

    SIDEBAR_CUSTOM=r"""
    <a href="<http://www.ubuntu.com/>"><img src="<http://www.ubuntu.com/countdown/banner1.png>" border="0" width="180" height="150" alt="The next version of Ubuntu is coming soon"></a>
    """
    
运行一下, 果然好了!!~~ 需要注意的是, 这个设置只有使用farseerfc制作的bootstrap2主题时才有用(再次感谢farseerfc!)~

那么怎么添加多个小工具呢? 很简单, 只要在字符串SIDEBAR_CUSTOM里面罗列copy来的代码就可以啦!~(比如, 还可以[添加gtalk](http://www.google.com/talk/service/badge/New)的小工具.) 所以, google自定义搜索引擎其实也可以这样添加的~



