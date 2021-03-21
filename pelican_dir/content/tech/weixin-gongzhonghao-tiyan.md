Title: 微信公众号上手体验
Slug: weixin-gongzhonghao-tiyan
Tags: 微信公众号
Date: 2021-03-21 19:30

>**写公众号最好的时机是五年前, 其次是现在.**

==> 所以我俩月前注册了个微信公众号🐱:

![](../images/weixin-gongzhonghao-tiyan/Pasted%20image%2020210321193829.png)

而拖延两个月以后, 这周末体验了撰写和发布公众号的流程, 感觉还是和通过github发布blog有点区别的, 这里记录一下.

### 将markdown转换为公众号文章

微信公众号的编辑界面类似word, 我从markdown导过去的话需要借用第三方工具. 其实这种工具还挺多的, 我找到了三个:

- <https://md.qikqiak.com/>
- <https://md.openwrite.cn/>
- <https://www.mdnice.com/>

我最推荐的是最后一个网站"mdnice", 和另外两个相比有不少优点:

1. 支持各种[排版主题](https://product.mdnice.com/themes/)
2. 登录帐号以后可以保存多个最近编辑的文件 -- 虽说理论上只要直接复制粘贴markdown就好, 但是说不定就要针对公众号进行调整, 所以能保存一个针对公众号的
3. 支持把外链转换为脚注(见下文)
4. 支持不少代码块主题
5. 代码块太长时可以横向滚动
6. 还支持Mac风格的代码块, 看上去很高级:  
   ![](../images/weixin-gongzhonghao-tiyan/Pasted%20image%2020210321191737.png)

### 嵌入视频

普通markdown里可以添加youtube或者B站的iframe html代码嵌入视频. 但是微信公众号不支持这个功能.

似乎只支持嵌入腾讯视频上的内容, 或者把视频手动上传到素材中然后嵌入.

### 不支持外链

> 微信公众号仅支持公众号文章链接，即域名为`https://mp.weixin.qq.com/`的合法链接.

也就是说微信公众号的链接只能指向另一篇公众号文章, 不能指向公众号之外的内容...  
这个比视频的问题还蛋疼... markdown里好多的链接, 转换以后直接没了.

不过好在mdnice支持把所有的链接变成脚注, 这样也可以凑合:

![](../images/weixin-gongzhonghao-tiyan/Pasted%20image%2020210321192409.png)

### 自定义菜单/自动回复

![](../images/weixin-gongzhonghao-tiyan/Pasted%20image%2020210321193340.png)

我目前只加了一个"历史文章"的菜单, cf. <https://www.jianshu.com/p/1bca96d3c76f>

另外看上去设置自动回复也挺容易的:  
![](../images/weixin-gongzhonghao-tiyan/Pasted%20image%2020210321193439.png)
