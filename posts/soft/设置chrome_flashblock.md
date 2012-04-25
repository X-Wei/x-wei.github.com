Title: 不用安装插件, 设置chrome点击播放flash
Date: 2012-04-24
Slug: chrome_flashblock
Tags: google

以前搜索怎么加速打开网页的速度, 有人会推荐flashblock插件. 安装之后, 所有的flash(视频也好, 广告也好)都不会自动播放, 只有自己去点击一下才会播放. 当时觉得这样挺好啊, 因为flash肯定占用了不少带宽以及cpu嘛~

后来, 发现cbl同学没有安装插件也实现了这样的效果, 如下图:

![](./chrome_flashblock/pasted_image.png)

 cbl教我把chrome设置成插件点击播放, 个人感觉这样挺有用的~
大概是两步:

**第一步**, 扳手菜单-->首选项-->高级选项-->隐私设置-->内容设置

![](./chrome_flashblock/pasted_image001.png)

然后找到"插件"这一项, 选择"点后运行"
![](./chrome_flashblock/pasted_image002.png)
这样设置之后, chrome就不会自动播放flash, 然后再设置点击运行flash.

**第二步**, 在地址栏输入: <chrome://flags/>, 找到"点后运行"一行, 选择"启用".

OK, 到此为止, 就可以不装插件实现flashblock效果了~~
