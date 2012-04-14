Title: 用pelican在github上创建自己的博客!
Date: 2012-04-13
Slug: pelican_github_blog
Tags: pelican, git

折腾了许久, 终于把[我的博客](http://x-wei.github.com)搞得差不多了, 在此写一个总结, 以免自己以后忘了, 并且给和我一样菜的人提供一点参考....

先扯点别的
-----
其实啊, 很早就想要建立自己的博客, 把值得分享的东西拿出来放到网上, 但是又不屑于使用网易, 百度等提供的现成服务, 技术又很菜... 于是一直拖着. zim的出现让我很欣喜--zim可以写类似于博客的东西(不过是给自己看的~), 记录有价值的内容. 但是怎么把我的一些总结放到网上?? 我先后考虑了这些东西:

googlesite-->wordpress-->jekyll+github-->pelican+github

googlesite是个很好的工具, **很容易上手**(google好赞...), 我曾经用它做过一个个人页面. 但是这种傻瓜工具的缺点就是: 没法自己定制... 当我发现googlesite的bolg页面不支持标签云的时候, 就决定不用它了... 况且googlesite在国内需要修改一下host才能访问... 

然后是wordpress, 这个似乎目前也是最流行的网页制作工具, 我看到了很多很多大牛小牛使用WP搭建的自己的网站, 而且都是自己的顶级域名, 看上去就灰常霸气~ 当我终于有空折腾, 兴冲冲地研究WP时, 却发现**顶级域名注册都是要交钱的**, 还要弄什么vpn...这... 大概不适合我...

在我纠结的时候, 请教了[dofine](http://www.dofine.me/)同学, 他推荐我使用[github pages](http://help.github.com/pages/)(后来证明这是非常正确的~). 早就听说git大名, 只是我太菜了... 不知能不能搞定啊... 还好可以随时询问dofine同学(有时我的问题很弱智, 他还是很耐心的回答, 真好~). github page弄好后, 要按装jekyll作为**静态页面**的生成工具. 在使用zim的时候, 我就对轻量级标记语言非常喜欢, jekyll可以使用Markdown格式(比zim的wiki语法还要简洁), 所以说应该是非常好的选择. **但是我在jekyll的安装这一步卡住了**... 由于我用的是ubuntu10.04, 安装各种报错... 更新了rubygem之后以为成功了, 但是运行jekyll还是不行... 折腾了两天后, 我决定暂时放弃了...

就在纠结之时, 报着试一试的态度, 在[yssy](https://bbs.sjtu.edu.cn/file/bbs/index/index.htm) 的gnu/linux版上问了一下, 得到了 [farseerfc](http://farseerfc.github.com/) 学长非常热情耐心的回答. 他建议我[采用pelican](http://farseerfc.github.com/try-pelican-zhs.html)来生成静态页面, 这是一个法国人用python写的程序. 我很容易就安装好了, 然后又折腾了许久, 现在终于基本搞定...... 感觉pelican还是相当不错的选择, 配置好了之后就可以安心写文章了...

第一步: 生成github page
------------------
第一步要做的就是注册github, 生成一个自己的二级域名(比如我的x-wei.github.com). 注册和配置SSH密钥过程[help page](http://help.github.com/linux-set-up-git/)写得很清楚, 虽然我连SSH是什么都搞不清, 按它说的一步一步做, 很容易就搞定了.

然后要新建一个repo(中文翻译成"依赖"?), 注意**这个repo需要命名成: your_id.github.com**, 所以一个id只能生成一个啦... 生成这个repo后会有提示, 运行一下mkdir, git init什么的就OK了.

这样, 建立好了your_id.github.com的repo之后, 只要把一个index.html文件上传到master分支, 就可以访问your_id.github.com看到那个index.html文件了~

第二步: 安装和使用pelican
-----------------
pelican的安装需要用到pip:

`$sudo apt-get install python-pip`

然后再用pip安装pelican:

`$sudo pip install pelican`

这样, 安装就完成了~

pelican的使用很简单, 这是帮助信息:


    $ pelican -h
    usage: pelican [-h] [-t THEME] [-o OUTPUT] [-m MARKUP] [-s SETTINGS] [-d] [-v]
                   [-q] [-D] [--version] [-r]
                   [path]

    A tool to generate a static blog, with restructured text input files.

    positional arguments:
      path                  Path where to find the content files

    optional arguments:
      -h, --help            show this help message and exit
      -t THEME, --theme-path THEME
                            Path where to find the theme templates. If not
                            specified, itwill use the default one included with
                            pelican.
      -o OUTPUT, --output OUTPUT
                            Where to output the generated files. If not specified,
                            a directory will be created, named "output" in the
                            current path.
      -m MARKUP, --markup MARKUP
                            the list of markup language to use (rst or md). Please
                            indicate them separated by commas
      -s SETTINGS, --settings SETTINGS
                            the settings of the application. Default to False.
      -d, --delete-output-directory
                            Delete the output directory.
      -v, --verbose         Show all messages
      -q, --quiet           Show only critical errors
      -D, --debug           Show all message, including debug messages
      --version             Print the pelican version and exit
      -r, --autoreload      Relaunch pelican each time a modification occurs on
                            the contentfiles


额, 其实那些参数可以先无视(直接用默认参数)... 那么用法就很简单了: **$pelican [path]**, 其中, path是放置markdown或rst文件的目录. 如果手头有几篇.md文件或.rst文件, 那么只要:

`$pelican [.md/.rst文件所在目录]`

就会看到效果了... 大概会在一个'output'目录里, 打开index.html就可以看到生成的页面, 只要把这些生成的文件push到github的master分支, 你的博客就建好了~~

另外, 把.md文件分别放在几个子目录, 那么生成的页面显示属于不同分类的文章了~

关于pelican的配置, 待会再说, 先说说git的上传...

第三步: 编辑.md/.rst文件
-----------------
markdown和rst都是非常优秀的轻量级标记语言, 可以很方便的写出整洁漂亮的笔记, 编写博客文章只要写成一个一个的.md或.rst文件然后交给pelican就OK了.

关于这两种格式的语法, 其实我自己还不太熟悉呢... 网上有不少教程, 比如这个[markdown的教程](http://wowubuntu.com/markdown/)和[这个ReST教程](http://readthedocs.org/docs/beinggeekbook/en/latest/rst.html)...

需要注意的是, 在文章的开头要指定一下博客的信息: 博客标题, 时间, 标签... pelican的帮助页面各提供了一个示例(我稍微修改了一下):

**.rst示例**

    My super title
    ##############

    :date: 2010-10-03 10:20
    :tags: tag1, tag2
    :category: yeah //如果把这个rst文件放在posts/下的子目录的话, 那么这一行可以省略, 默认把子文件夹名作为分类
    :author: Alexis Metaireau //由于settings文件已经指定了作者. 这一行可以省略
    :slug: test-blog //这个是指定生成页面的名称, 比如这个是指定生成的页面名字是"test-blog.html"

    这里写博客内容...

**.md示例**

    Date: 2010-12-03
    Title: My super title
    Slug: test-blog
    Tags: tag1, tag2

    这里写博客内容...

**另: 关于编辑器**
编辑这类文件时最好能够预览效果, linux下用[ReText](http://wowubuntu.com/retext.html)即可~ 

第四步: 把生成的文件上传到github
--------------------
以前没用过git, 所以这个让我困惑了很长时间... 

首先, 应该在your_id.github.com页面下有一个.git文件夹(大概是git init生成的吧), 然后, 把生成好了的那些文件(比如上一步的output文件夹里的东西)放在这个目录下, 依次运行一下三个命令:
    $git add .
    $git commit -am "your commit message"
    $git push
额 是的, 需要三条命令才能完成上传... 另外, 貌似这样会覆盖掉原先的那些文件, 不必担心, github有history功能(我的理解 可能跟快照有点类似吧), 原先的东西应该可以找回来...

push完成后, 你的注册邮箱会收到邮件"page built successful", 如果是第一次生成的话, 最多等10分钟, 你就可以访问your_id.github.com看到效果啦~~

第五步: pelican的进一步配置
------------------
如果按照默认的参数, 直接$pelican path的话, 估计不会得到让你满意的页面--至少网站名字要改一下吧!! 还有, 默认的主题没有标签云, 反正我比较想要这个功能... 

farseerfc给了一个[settings.py](https://github.com/farseerfc/farseerfc.github.com/blob/master/settings.py)配置文件, 各个变量的名字含义应该比较清楚, 或者看pelican的[帮助页面](http://readthedocs.org/docs/pelican/en/2.8/settings.html), 这个页面也提供了一个示例配置文件. 可以在这俩配置文件基础上进行修改... 修改完成了之后, 运行pelican时加上-s参数指定settings.py作为配置文件:

`$pelican -s settings.py [.md/.rst文件所在目录]`

我是从farseerfc的配置文件改的, 大概是这个样子:

    # -*- coding: utf-8 -*-
    import sys

    TIMEZONE = 'Asia/Shanghai'

    DEFAULT_LANG = 'zhs'

    SITENAME = "X. Wei's Blog"
    AUTHOR = 'X.Wei'

    DISQUS_SITENAME = 'xweisblog'
    GITHUB_URL = '<https://github.com/X-Wei>'#github链接
    SITEURL = '<http://x-wei.github.com>'
    GOOGLE_ANALYTICS = 'UA-30756331-1'#谷歌站点分析
    TAG_FEED  = 'feeds/%s.atom.xml'

    DEFAULT_PAGINATION = 4#默认每一页有多少篇文章

    DEFAULT_CATEGORY ='misc'
    OUTPUT_PATH = '.'#需要把输出路径从默认的'output'改成根目录(your_id.github.com目录), 因为githubpage需要把vaindex.html上传到repo的master分支的根目录才可以!
    PATH = 'posts'#这个是指定放置.md/.rst文件的目录

    LINKS = (('dofine', '<http://www.dofine.me>'),
             ('farseerfc', "<http://farseerfc.github.com/>"),
             )#友情链接~

    SOCIAL = (
              ('github', '<https://github.com/x-wei>'),
              )#社交网络链接
              #~ ('twitter', '<http://twitter.com/farseerfc>'),
              #~ ('facebook', '<http://www.facebook.com/farseerfc>'),
              #~ ('weibo', '<http://weibo.com/farseerfc>'),
              #~ ('renren', '<http://www.renren.com/farseer>'),
              
              
    #这个是farseerfc同学自己加的, 可以显示他的新浪微博内容, 有微博的话可以把这些加上~
    #~ TWITTER_USERNAME = 'farseerfc'
    #~ SIDEBAR_CUSTOM = r"""
    #~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
    #~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
    #~ src="<http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1>">
    #~ </iframe>
    #~ """

    #google自定义搜索(大概是站内搜索吧)
    #~ GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
    #~ GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"

由于配置文件里已经包含了PATH和OUTPUT_PATH什么的, 所以运行只要:`$pelican -s settings.py`即可~

然后, 关于主题模板, 可以使用-t参数指定主题. pelican目前主题在[github](https://github.com/farseerfc/pelican-themes)上, 可以用$git clone <https://github.com/farseerfc/pelican-themes> 下载, 然后使用主题的话就是:

`$pelican -s settings.py -t [主题所在目录] [.md/.rst文件所在目录]`

如果想生成后就预览一下, 那就写:

`$pelican -s settings.py -t [主题所在目录] [.md/.rst文件所在目录] | xdg-open index.html `

个人感觉还是bootstrap2主题比较好... 目前由于pelican使用的人不多, 所以主题也就那十几个... 


再罗嗦一下: 关于一些问题的解决方法
------------------
这几天折腾pelican很久很久, 发现以下几个问题:

+ 不支持多层分类?

--这个目前没法解决, 不过既然有标签功能, 分类不能多层也无所谓啦...


+ 安装后不支持Markdown语法?

这个是因为Markdown没有与pelican包一起安装(pelican默认的还是支持rst格式), 安装上Markdown包就行了:

`$sudo pip install Markdown`


+ 如何插图?

这里不是讨论markdown语法如何插图, 而是怎么让生成的网页有图片. 其实很简单, 把.md文件里引用的图片复制一份到static目录即可~ (其实剪切也是可以的, 只不过那样的话编辑预览时就看不见图片了...)


+ 中文tag不支持?(事后证明其实是支持的, 是我搞得不支持了...)

pelican2.8(当前版本)是支持中文tag的! 我一开始直接git clone了3.0的源码, 然后不支持了... 需要重装pelican:

    $sudo pip uninstall pelican
    $sudo pip install pelican 


+ 不支持中文文件名

这个我没解决, 无所谓, 起一个英文文件名(.md文件以及Slug最好都用英文吧)好了, 毕竟博客标题(Title)是可以用中文的~

**OK, 就写这些吧... (累死了...)**

(我发现几乎所有文章都是从zim里搬来的, so, 以后就不在文章最后标注"imported from zim"了...)





