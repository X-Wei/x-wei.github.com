Title: pelican3建立github博客&主题配置 
Date: 2016-10-12 
Slug: pelican3_blog_and_theme 
Tags: pelican 
 
  
 
上次捣鼓pelican博客系统还是在2012年, 那时[farseerfc](https://farseerfc.me/)学长就提供了无私的帮助, 当时非常兴奋写了这么一篇简单的[教程](http://x-wei.github.io/pelican_github_blog.html).  
 
这两天捣鼓了好久 终于把博客升级到了pelican3... 

新的pelican貌似希望使用者把写作的内容和生成的网页分成两个repo管理, 我嫌麻烦还是把它们都放在了一个repo下面: <https://github.com/X-Wei/x-wei.github.com> 这个repo包含了生成的网页以及我写作的内容(在pelican_dir目录下面).  
 
换了超赞的新皮肤, 这个是[farseerfc](https://farseerfc.me/)学长定制的bootstrap3[主题](https://github.com/farseerfc/pelican-bootstrap3), 非常精美. 学长的版本包含了繁简英日翻译以及导出pdf/png什么的按钮, 功能非常全, 不过直接拿来用不太合适, 比如我就不需要博客的日语版... 我实际是用的[silverchard](http://silverchard.me/)对farseerfc学长主题的[修改版](https://github.com/SilverChard/material-bootstrap-pelican). 再稍微修改了一下配色什么的...  
 
如果想要做一个类似的博客, 下面是一些步骤:  
 
### 1. 安装软件 
 
首先安装pelican3以及其他一些python module (另外个人建议新建一个virtualenv在里面搞):  
 
``pip install pelican jinja2 py3babel babel beautifulsoup4 markdown`` 
 
其实安装了这些以后, 如果不用这个主题的话别的东西也不用安装了, 可以参考[这篇文章](https://www.notionsandnotes.org/tech/web-development/pelican-static-blog-setup.html)...


不过说实话, 我看了一圈, 还只有学长这个主题既好看(meterial design)又实用(有标签云/搜索/自定义侧栏等功能).  
 
为了安装接下来一些依赖, 需要有root权限, 这里可以参考silverchard的[文章](http://silverchard.me/yi-ge-fei-chang-mei-de-pelicanmo-ban.html)(ubuntu把``yum``改成``apt``就可以), 注意opencc需要用他提到的那种方法用github上的版本, 否则会报错...  
 
上面的博客链接失效了, 把安装的命令写在此处:  

	sudo apt-add-repository ppa:chris-lea/node.js -y
	sudo apt-get update
	sudo apt-get install nodejs ditaa doxygen parallel
	sudo pip install pelican jinja2 py3babel babel beautifulsoup4 markdown
	sudo npm install -g less
	wget "http://downloads.sourceforge.net/project/plantuml/plantuml.jar?r=&ts=1424308684&use_mirror=jaist" -O plantuml.jar
	sudo mkdir -p /opt/plantuml
	sudo cp plantuml.jar /opt/plantuml
	echo "#! /bin/sh" > plantuml
	echo 'exec java -jar /opt/plantuml/plantuml.jar "$@"' >> plantuml
	sudo install -m 755 -D plantuml /usr/bin/plantuml
	wget https://bintray.com/artifact/download/byvoid/opencc/opencc-1.0.2.tar.gz
	tar xf opencc-1.0.2.tar.gz
	cd opencc-1.0.2 && make && sudo make install && cd ..
	sudo locale-gen zh_CN.UTF-8
	sudo locale-gen zh_HK.UTF-8
	sudo locale-gen en_US.UTF-8
	sudo locale-gen ja_JP.UTF-8
 
### 2. clone repo 
 
第二步可以直接克隆我的git repo到本地:  
 
``git clone https://github.com/X-Wei/x-wei.github.com.git`` 
 
然后在下载下来的文件夹里, 删除除了``pelican_dir``以外的所有文件/文件夹, 进入``pelican_dir``, 这里面有个content文件夹, 里面就是我的博客的markdown源文件, 每个文件夹为一个category分类(``images``, ``static``, ``pages``目录除外), 想要写自己的博客只要把这里的markdown文件替换掉即可. 另外注意, 如果写的markdown文件里面有引用图片的话, 需要把图片放在``images``目录下面, 然后在md文件里图片地址写成 ``../images/XXX.jpg``  
 
### 3. 更多配置 
 
然后可以修改一下pelicanconf.py文件, 比如修改一下博客名字/作者名字/disqusid之类的... 
 
关于一些config变量的用法, 可以参考pelican的文档: <http://docs.getpelican.com/en/3.6.3/settings.html>, 以及bootstrape3主题的文档: <https://github.com/DandyDev/pelican-bootstrap3/wiki/Variables>. 
 
 
###4. 本地预览 
 
 
 
写好博客内容以及配置好pelican以后, 可以首先在本地预览一下. 在``pelican_dir``目录下, 输入:  
 
``make html`` 
 
这会在``pelican_dir/outpt``下生成(预览版的)网站的所有文件. 想要查看效果, 只要继续在``pelican_dir``下输入:  
 
``make serve`` 
 
然后浏览器打开<http://localhost:8000/>即可看到预览的效果.  
 
 
###5. push到github 
 
 
如果想要像我一样建立一个github.io域名的博客, 需要首先有一个github账号, 然后新建一个名字为``your_github_id.github.io``的git repo, 然后在本地把刚才那个``pelican_dir``文件夹复制到这个repo的根目录.  
 
之后在``pelican_dir``下运行: ``make publish``, 这会在``your_github_id.github.io``的根目录(也就是``pelican_dir``的上级目录)下生成网站的所有文件.  
 
这些文件生成以后, 只需要push到github即可(pelican的makefile本来有push到github page的选项, 不过没弄明白, 于是还是这么搞好了): 
 
	git add -A .  
	git commit -m 'your commit message' 
	git push 
 
 
push成功以后, 等几分钟, 就可以在``your_github_id.github.io``看到你自己博客了 !  
