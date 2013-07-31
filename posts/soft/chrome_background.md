Title: chrome护眼设置--把背景设置为绿豆沙
Slug: chrome-background
Tags: tips, google,外观
Date: 2012-02-23


直接把[这里](http://hi.baidu.com/laolao18k/blog/item/3a268016cd4c4907c83d6d46.html)的贴上吧...
(以下为copy)

 首先，下载安装chrome的[stylist插件](https://chrome.google.com/extensions/detail/pabfempgigicdjjlccdgnbmeggkbjdhd)
然后，打开"扩展设置"，点击chrome stylist的选项，点击demo进行修改。 

把网页背景修改为豆沙绿的参数设置: 
输入框1：demo 选项框2：regexp 输入框3：(ftp|http|https)://\D 输入框4： * { background: #C7EDCC !important; } 修改后保存即可 (url和style text可根据自己喜好配置) 
附：豆沙绿的参数 RGB颜色 199；237；204 十六位颜色代码 #C7EDCC 色调：85；饱和度：123；亮度：205 

不会的话直接用[这个扩展](https://chrome.google.com/extensions/detail/hnjebfhieiaohnhafcolehbbcfkkkhje#%E5%AE%83%E9%99%A4%E4%BA%86%E6%8A%8AGoogle%E7%9A%84%E8%83%8C%E6%99%AF%E6%94%B9%E4%B8%BA%E4%BF%9D%E6%8A%A4%E7%9C%BC%E7%9D%9B%E7%9A%84%E7%BB%BF%E8%89%B2%EF%BC%8C%E4%BB%96%E6%B2%A1%E6%9C%89%E5%88%AB%E7%9A%84%E5%8A%9F%E8%83%BD)。
![](./chrome-background/pasted_image.png)

**04/24/2012续**

关于那个正则表达式, 如果写成 `*{ background: #C7EDCC !important;}`, 虽然一片绿豆色很护眼, 但是不少网页显示会有问题. 比如校内上新鲜事显示不了照片预览, gmail的加星标签看不见等... 最坑爹的是有的网页文字是浅色的, 那样的话几乎看不清楚了... 我现在使用的这样的规则: 

    body { background: #C7EDCC !important;} 
    body {color:black}

第一行, 指定只是网页的body部分为绿豆沙色(大部分网页的背景都是body); 第二行, 指定body里的文字都使用黑色.

这样弄下来比原先要好不少(关于上面提到的显示校内网和gmail的问题都解决了), 虽然网页不是全部绿豆沙了...


**--imported from zim**




