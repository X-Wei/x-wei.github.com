Title: 效率反思 - 博客和微信公众号发布过程的阻力
Date: 2022-03-27
Tags: 效率, 写作
Slug: blog-pub-frictions


又是很久没更新博客和公众号, 昨天想更新一篇关于瑞士驾照的内容, 写作本身其实挺流畅, 但是在发布到博客和微信公众号的过程中费了不少时间和功夫... 

其实我过去一年多在私人笔记(zim/obsidian/foam)里写了不少内容, 但是都没有发布. 一部分原因也是这些发布过程中的阻力(friction)造成的, 尤其是很长时间不碰又会忘记, 需要重新摸索着发布.

这里记录一下我目前文章的写作和发布流程(包括每一步的预估耗时), 反思一下哪些环节可以优化(甚至自动化).


I-文章写作
----
博客写作主要在zimwiki编辑器里进行. 十年过去了, 现在虽然也开始用obsidian和foam, 我感觉zim依然是专注编辑内容的最佳工具, 编辑体验非常流畅. 

(关于这些笔记软件以后有机会再聊).

II-发布到[个人github博客](https://x-wei.github.io/)
-----------------------------------------


1. **把zim里的文章导出为markdown **: **__5~10min__**
   * zimwiki导出markdown文章源码 — zim里右键菜单
   * VSCode打开博客目录, 新建一个markdown文件并粘贴内容 
     * 我用pelican生成静态博客, 需要在markdown开头加上一些metadata(标题/标签/日期等)
     * 用VSCode的markdown预览查看和修复排版问题(因为zim的导出不是100%完美)
   * 纯文字的内容还好, 如果附带了图片, 还需要手动在``images/<slug>/``新建文件夹, 把zim里的图片放进去
2. **pelican本地生成静态html并预览** : **__~5min__**
   * 其实这一步并非必要 — 我现在有一个[GithubAction](https://github.com/X-Wei/pelican-gh-actions-xwei) 可以在提交新markdown的时候自动生成html, 不过很多时候为了检查我还是要自己看一看.
   * 我本地安装了我博客的[专属Docker镜像](https://github.com/X-Wei/pelican-gh-actions-xwei/blob/master/Dockerfile), 需要运行一个容器并且ssh进去:
     ```sh
     # 看看本地有哪些docker镜像
     $ docker images 
     REPOSITORY              TAG        IMAGE ID       CREATED         SIZE
     ...
     my-pelican-blog         latest     cf58777756fa   12 months ago   1.3GB 👈
     # 运行并进入docker容器
     $ docker run --rm -it -p 8000:8000 --name pelican \
       -v ~/path/to/my/blog:/home/blog -w /home/blog/pelican_dir/ \
       --entrypoint bash \
       my-pelican-blog:latest
     # 进入容器以后, 生成html并预览
     root@4c3059d9dc4a:/home/blog/pelican_dir$ make html && make serve
     # ==> 然后就可以在本地 http://localhost:8000 预览博客内容了
     ```
   * 如果预览过程发现一些排版的问题, 可能还会重复几次... 另外现在的pelican主题确实有点老旧了, 不咋好看...


3. **新文章发布到github**: **__~5min__**  
  其实git push很快, 但是GithubAction处理新文章需要一些时间, 所以要反复刷新浏览器, 等新文章出现在博客上才算OK...
  
III-发布到微信公众号
--------


1. **markdown源码导出为微信公众号内容**: **__10~15min__**
   * 微信公众号不支持markdown渲染的, 所以要用第三方工具导出
   * 用<https://mdnice.com/> 可以把markdown源码转为微信或者知乎文章的内容
   * 需要重新上传一次图片到mdnice的图床("右键->图片")
   * 另外微信公众号还*不支持外部链接*, 在mdnice里可以"右键->微信外链转脚注", 把所有参考链接放到文章末尾
   * mdnice还支持各种主题, *不过微调主题的过程很可能一不小心就又浪费十几分钟*...
2. **新建公众号图文消息**: **__~10min__**
   * 在mdnice的文章页面, 点击右上角的绿色图标("复制到公众号")
   * 扫码登录微信公众号页面, 新建"图文消息", 然后粘贴内容进去
   * 添加封面图片和摘要
   * 添加原创声明 — 我一般先发布到博客, 再发公众号, 这样
   * 再次检查一下排版, 修改错别字
3. **预览公众号文章**: **__10~30min__**
   * 在正式发布以前, 还可以发送给部分用户(主要是自己),做一个"teamfood". 在手机上看看文章效果.
   * 微信公众号发布后只能修改一次, 而且最多不能超过十个字, 所以造成文章草稿写好以后要反复看几次还不敢发
   * 另外吐槽一下, 公众号的网页界面有时候速度很慢, 点了等半天才刷新... =_=
   * 确定没问题以后, 点击"发布"或者"群发", 就会向所有关注的用户推送消息了


IV-总结/反思
-----

这么写一下总结下来, 实际进行格式转换("zimwiki => markdown => html/公众号内容")的时间并不是大头. 相反有很大部分时间是在校验排版和微调主题上.

🤔有没有一种可能... 你的文章并没有很多读者🤡

突然想到一句话: 

>"差生文具多" 

(在我纠结IDE的主题/样式/插件的时候, 大佬们已经用vim,nano甚至notepad写下一行行牛逼的代码了...)

🤔🤔没有必要追求完美主义, 相比于内容本身, 文章样式和错别字啥的并不重要...

**⇒ 所以还是专注内容本身, 保持不断输出就完事了!**
