Title: 关于用pelican写博客的两点tips
Date: 2012-05-27
Slug: 关于用pelican写博客的两点tips
Tags: pelican


#1.插入视频

效果就像校内网日志那样, 可以内嵌的视频.

其实很简单, 只需要把html代码放进markdown源文件就行了! 而视频的html代码在视频网站上一般都会提供:

![](./关于用pelican写博客的两点tips/pasted_image.png)

复制下来放进源文件即可


#2.删除线

markdown不支持删除线? 反正我没有在教程里找到... 但是删除线确实是个有用的功能, 在zim里记笔记的时候我就经常使用.
但是好像听说markdown是支持html内容的, 那么, 是不是直接加html的删除线代码就行了呢? 果然~!

    <s>文本</s>
    or
    <strike>文本</strike>

嗯, 更复杂的html样式如果markdown没有的话也可以用这种方法弄~

#3.给博客加入分享按钮
这个也是用网上找的html代码, 然后修改了一下主题(pelican-themes/bs5)中的一个html文件, 不过我水平太菜, 改了好久也没能让分享按钮处于标题下方...