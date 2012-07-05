Title: [更新]访问google服务和优酷去广告功能的host列表
Date: 2012-07-06 00:08
Slug: google_youku_host_20120706
Tags: google, host


之前两篇帖子介绍了如何通过修改host文件达到无鸭梨[访问google服务](http://x-wei.github.com/google_host.html)以及[屏蔽优酷土豆广告](http://x-wei.github.com/host_youkuqiyi.html)的目的, 虽然不明白这东西到底是啥原理, 但一直用得很爽......

在学校里使用那一个hosts文件一直很顺利, 没啥毛病, 有人抱怨说那个方法不给力, 我也没管...

后来回家发现原来的host确实不给力了, 优酷广告可以屏蔽, 但gmail的附件预览不能...... 今晚决定搞一搞这个问题... 原先的文件在学校管用的原因, 我猜测是google的host有不少是ipv6的, 回家后这些行都不行了...... 于是上网搜索, 想改改新的host.

搜了一大堆都是2011年贴出来的, 不知能不能用... 边搜边想, 这样每隔一段时间去搜host的方法貌似有点笨......

**然后我发现了两个比较给力的host项目......**

smarthosts
----------
一个是[smarthosts](http://code.google.com/p/smarthosts/)项目, 在云端不断更新(最近一次是07.03, 两天前)host文件, 而且也提供了各种客户端~ for linux的其实就是[一个python文件](https://smarthosts.googlecode.com/svn/trunk/osx_linux.py), 功能就是把云端的文件(地址: <https://smarthosts.googlecode.com/svn/trunk/hosts>)copy到本地覆盖原先的文件... 所以(对我来说)也用不着什么客户端, 需要时去copy那个云端文件来本地就是了.

把那个文件中的host行copy到我本地的hosts文件里, 顺便把原先的那些行删了, 然后google就可以顺利访问了~ gmail附件预览木问题, googlesites啥的也能上了~

hostx
-----
之前用的host加上那个修改host屏蔽视频网站的的方法, 只是对优酷有效, 对土豆/奇异貌似都无效, 我猜是因为host的原因. 所以继续搜屏蔽广告的host. 然后我就搜到了hostx这个项目(网址是: <http://orztech.com/softwares/hostsx> 这个值得吐槽的域名==), 和smarthosts项目类似... 

它提供给linux的是shell代码, 很短: 

    #!/bin/bash
    sudo mv /etc/hosts /etc/hosts.bak
    wget <http://hostsx.googlecode.com/svn/trunk/HostsX.orzhosts>
    sudo mv hosts /etc/hosts
    sudo gedit /etc/hosts
    sudo /etc/init.d/networking restart

啊... 原来这个也是个googlecode上的项目, 和smarthosts很类似... (使用googlecode/github来共享文件确实是不错的办法唉) 不过它的特点是可以提供屏蔽视频网站广告的host, 我把这些host加入本地的hosts文件之后, 果然土豆/奇艺的广告也去除了(当然之前要按[这个帖子](http://x-wei.github.com/host_youkuqiyi.html)设置一下), 给力啊!~ 

总结
-----
本来使用hozstx也有关于google的行, 只是实测貌似不给力...... 于是我现在把这俩host内容都放在我本地的hosts文件里(看来host这东西还是多多益善...), 另外, 这两个都提供了youtube等网站的host, 但是实测都不给力...... 不过反正一般也不上什么youtube/twitter(想上的同学自己折腾下"goagent"......), 目前的效果(**访问google所有服务, 上优酷/土豆/奇艺没广告**)已经很满意了~~

最后贴上[我的host文件](./[更新]访问google和优酷去广告功能的host/hosts)... 

我已经把最开头locoalhost那两行删了(否则可能有问题), 下载下来后把这些内容添加到本地的host文件中即可~ 本地的hosts文件位于:

    linux: /ect/hosts
    windows: c:/windows/system32/drivers/etc/hosts


如果又不能用了, 可以自己去把 <https://smarthosts.googlecode.com/svn/trunk/hosts> 和 <http://hostsx.googlecode.com/svn/trunk/HostsX.orzhosts> 这俩文件的内容粘贴进本地的hosts文件里就可以了. 我估计换一次host能撑很长时间吧... 当然如果真的很懒的话也可以用他们提供的小软件来搞~
 
P.S. 码字+修改花了好长的时间啊啊... 大概是因为昨天看了篇文章, ["为什么你应该（从现在开始就）写博客"](http://mindhacks.cn/2009/02/15/why-you-should-start-blogging-now/)......