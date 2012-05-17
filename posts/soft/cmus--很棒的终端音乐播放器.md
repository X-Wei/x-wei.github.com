Title: cmus: 很棒的终端音乐播放器
Date: 2012-01-23
Slug: cmus: 很棒的终端音乐播放器

最近发现一个终端下超好用的音乐播放器: [CMUS](http://en.wikipedia.org/wiki/Cmus). 界面简洁, vi的按键绑定, 由于最近越来越感觉键盘和快捷键的方便, 对这个迷你的播放器爱不释手.

关于它的用法可以参考[这里](http://www.tuxarena.com/static/cmus_guide.php), 另外[这里](http://roylez.heroku.com/2010/01/26/replay-gain.html)还介绍了怎么设置replay gain(大概是不同音乐播放的音量相同), 但我没有设置.

网站上的文档不多, 我觉得最好的教程还是man:
man cmus
man cmus-tutorial
把tutorial看完就基本上会用了~

这里列一下我觉得常用的几点吧:


1. 1~7共7种view, 用数字键就可以切换;
2. 使用命令要想vi一样加':', 常见命令有:

:cd xx_dir
:add xx_dir

3. c--暂停, hl/<>--快进快退, x--播放, v--停止
4. 右下角显示播放模式: R表示重复, S随机, C连续(播完一曲后不停)

