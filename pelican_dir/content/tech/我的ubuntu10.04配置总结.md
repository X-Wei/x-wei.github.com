Title: 我的ubuntu10.04配置总结
Tags: ubuntu, 外观, 快捷键
Date: 2013-07-20
Slug: 我的ubuntu10.04配置总结
 
 

ubuntu已经出到了13.04, 我之所以坚持使用ubuntu10.04的版本(到现在已经三年了, 现在10.04已经过了支持周期而我还在继续用它), 主要是因为ubuntu出的unity界面以及gnome3的界面实在是用起来不爽(吐槽不已!!)... 

目前我的lucid(ubuntu 10.04)经过我的配置, 在我用来已经十分顺手了.. 不过长久这么下去也不是办法...... 在换新的主力系统之前, 把我目前这个系统的配置写下来.

安装的软件
-----
写一下用起来特别爽的一些软件: 


* geany

**万能IDE**, java/python/Cpp/matlab(octave)... 甚至tex都是用它写的, 轻巧强大. 


* zim桌面维基

**神器**, 用来写笔记整理思路, 这篇就是在zim下写的. 自从2012年发现zim这个东西以后, 到现在写了上百条笔记了, 确实方便.


* GNU octave

matlab的开源替代, 语法和matlab完全兼容, 毕设就是用它做的, 如果不用matlab工具箱的话, 这个是很好的选择, 而且比较小巧, 启动很快.
......不过法国人貌似比较喜欢他们自己搞出来的scilab.


* 音乐播放器audacious

界面和简洁, 用起来蛮好, 不过可能其他播放器也差不到哪里去...


* 词典goldendict

这个还不是最新的版本(我用的是0.9.0), 已经相当顺手了. 可以自己加stardict的词典文件, 从网上可以找到很多(包括法语的词典), 用起来比stardict方便, 屏幕取词什么的也很好用.


* GNOME Mplayer

感觉这个界面简洁些, 可能其他播放器(VLC之类)也差不到哪里去.


* QQ: wine-TM2009

地址在[这里](http://www.mintos.org/network/wineqq.html), 根据我的经验, 别再折腾了, 这个就是最好的解决方案...

配置
--

* zip乱码解决

之前[介绍过](http://x-wei.github.io/zip%E4%B9%B1%E7%A0%81%E8%A7%A3%E5%86%B3.html).

### 外观

* globalmenu+windowbuttons

安装这两个插件以后, 可以真的**最大化**利用屏幕空间, 很科学...(貌似是跟苹果学的?)


* 自定义的主题

Faenza图标主题; elementary窗口主题; ComixCursors鼠标主题; clearlooks控件...
总之这大概就是我觉得最舒服的外观主题了...


* 边缘触发动作

compiz的设置, 把鼠标移动到左下角会显示桌面, 很方便...(貌似是跟苹果学的?)


* compiz特效

立方体特效, 开四个桌面(这个其实很实用, 尤其是开十个以上窗口时......);
动画特效, "对所有事件使用随机动画"(这个开了以后效果惊艳, 而且即使老电脑开了这个一点也不会卡, 完爆win...);
其他特效还没全开...... 


* 护眼背景色(gnome+chrome)

[gnome的设置](http://x-wei.github.io/gnome-background.html);
[chrome的设置](http://x-wei.github.io/gnome-background.html);

### 快捷键
总结一下配置的快捷键: 

* 显示桌面

win+D

* 打开浏览器

win+B (取"**B**rowser"之意)
关联的命令是``google-chrome``

* 打开文件管理器

win+F (取"**F**ile"之意)
命令: ``nautilus --browser /home/your_username``

* 打开goldendict

ctrl+alt+D

* 截图

win+S
命令是: ``gnome-screenshot -ia``
这个之前也[写过](http://x-wei.github.io/scrshot-shortcut.html).

