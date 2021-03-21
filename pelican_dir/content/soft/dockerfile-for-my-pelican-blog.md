Title: 用Dockerfile免配置生成pelican博客
Date: 2020-10-17
Slug: dockerfile-for-my-pelican-blog 
Tags: pelican


我的这个pelican博客已经有八年多了, 从[最开始](https://x-wei.github.io/pelican_github_blog.html)使用pelican2.x+bootstrap2主题到现在[使用pelican3](https://x-wei.github.io/soft/pelican3_blog_and_theme.html), 断断续续经过了各种折腾.

现在的blog虽然文件内容还很乱, 但是网页样式我基本满意. 问题就是pelican3加上我自定义的主题/插件, 配置起来实在太繁琐, 每次换电脑都要折腾半天...

所以之前我做了一个Dockerfile和GithubAction, 自动从markdown/rst文件生成静态网站的html文件: <https://github.com/X-Wei/pelican-gh-actions-xwei>

这个repo可以作为github action上运行, 比如每当commit到markdown文件夹的时候, 让github actor生成html文件然后commit —— 可以参考我的blog的[github workflow配置](https://github.com/X-Wei/x-wei.github.com/blob/master/.github/workflows/main.yml).

今天又修改了一下, 让它也能在本地用docker跑, 免去了换电脑重新折腾配置的痛苦(这也是我这几个月没更新博客的原因, 之一). **这篇文章主要记录一下如何用Dockerfile在本地机器上预览或者生成静态网站.**

build Docker image
-----------
首先需要使用Dockerfile来build一个docker image.  
顺便给它加个tag叫"my-pelican-blog:latest" (``-t my-pelican-blog:latest``):

	$ docker build -t my-pelican-blog:latest \
	    github.com/x-wei/pelican-gh-actions-xwei

(我准备以后把这个docker image[发布到Github Container Registry上](https://github.com/X-Wei/pelican-gh-actions-xwei/issues/2) 这样就不用自己的机器build image了)

如果想自己修改什么内容, 可以在本地的repo里修改Dockerfile/entrypoint.sh, 然后重新build image:

	$ docker build -t my-pelican-blog:latest .


运行容器生成html预览
--------------------------------------
本地直接run这个image的话, 是生成html文件到``output/``文件夹以供预览(也就是makefile里的"[make html](https://github.com/X-Wei/x-wei.github.com/blob/6bb137a68149665e8da713e75b75d986ee73814c/pelican_dir/Makefile#L17)"命令).

注意需要把实际的本地blog repo位置(我是"*~/Documents/x-wei.github.com*")映射到container里的"/*home/blog*"文件夹(``-v ~/Documents/x-wei.github.com:/home/blog``)

另外最好加上`--rm`, 这样container运行完以后立刻就被删掉了, 不留垃圾(只是删掉container, 上一步build的image还在).

	$ docker run --rm \
	    -v ~/Documents/x-wei.github.com:/home/blog \
	    my-pelican-blog:latest


SSH到容器中运行命令
----------------------
像上面直接run的话只能跑``make html``, 跑完后就退出容器了. 而其实在容器中还可以运行``make serve``和``make publish``命令(cf. 我之前介绍pelican3的[文章](https://x-wei.github.io/soft/pelican3_blog_and_theme.html#4-ben-di-yu-lan)), 这样本地预览起来会更方便一些.

要SSH进在容器中运行各种命令, 只需要用"bash"代替默认的entrypoint.sh(``-it --entrypoint bash``), 同时为了本地预览需要开启port forwarding(``-p 8000:8000``):

	$ docker run --rm --name pelican \
	  -w  /home/blog/pelican_dir/ \
	  -v ~/Documents/x-wei.github.com:/home/blog \
	  -p 8000:8000 \
	  -it --entrypoint bash \
	  my-pelican-blog:latest
	
	root@fea99c54aea1:/home/blog/pelican_dir# make html && make serve # or `make publish`
	# (Preview the website at http://localhost:8000/)
