Title: 修改host去除优酷奇艺网站广告
Date: 2012-04-19
Slug: host_youkuqiyi
Tags: host


优酷现在的广告已经是半分钟长了?? 所以屏蔽这些广告还是很有必要滴~

之前, 马阳同学给我一个修改host的方式, 用了几个月之后, 发现不好使了: 虽然不会显示广告, 但是不会直接跳过去, 而是显示"广告不能正常播放..." 然后还是要等待半分钟才能看... 

后来, 看了[奶牛的博客](http://www.nenew.net/youku-qiyi-hosts-windows-win7-windows7-vista-ubuntu-linux-archlinux-firefox-chrome.html), 终于找到了解决办法, 至少到目前还是好使的~

首先, 关于host的修改, 直接参考[这篇博客](http://x-wei.github.com/google_host.html), 把里面host的全部内容粘贴进对应的文件中.

然后, 按照奶牛的办法:

#linux用户
找到: `~/.macromedia/Flash_Player/#SharedObjects/某某名字文件夹/` 这里, 可能会有两个文件夹: `www.iqiyi.com`以及`static.youku.com`, 删除之, 然后新建两个空白文件, 名字就取这两个文件夹的名字(要是没有这俩文件夹, 则直接新建这两个空白文件).

#windows用户
和linux用户一样, 只是那个文件夹在: 

    (xp) C:\Documents and Settings\Administrator\Application Data\Macromedia\Flash Player\#SharedObjects\某某名字文件夹 (呵呵, 略长略长...)
    (win7) C:\Users\用户名\AppData\Roaming\Macromedia\Flash Player\#SharedObjects\某某名字文件夹

 注意啊, 新建的空白文件就是叫`www.iqiyi.com`和`static.youku.com`, 我的意思是...别加上.txt的后缀之类的...

这样做好之后, 看优酷奇艺的视频就没有广告了, enjoy~

另外, 我的host文件里好像提供了土豆的屏蔽规则, 但是貌似不大好使...
