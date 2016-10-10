Title: putty使用备忘
Date: 2014-07-28
Slug: putty使用备忘
Tags: ssh

最近要用SSH连接服务器, Windows下面当然就是用putty了, 遇到的问题总结一下. 

保存session
---------
打开putty.exe以后, 输入服务器ip, 之后先别点击登录, 先保存一下session下一次就不用再输入了: 

![](_images/putty使用备忘/pasted_image.png)

之后点击登录就好了. 

本地和服务器之间传输文件
------------
传输的时候貌似不能用linux里的scp命令, 而需要使用另一个putty的工具: ``psftp``

下载的时候那个putty.zip压缩包里有一个``psftp.exe``, 点击它就打开了. psftp也是一个命令行的工具, 和ssh类似, 用``pwd/ls/cd``等在**服务器的**文件系统里进行移动. 

而在**本地的**文件系统里移动的话, 用``lpwd/lcd/lls.``

移动到了想要传输文件的目录以后(本地和服务器都移动好了以后), 使用``put filename``上传本地文件到服务器, 使用 ``get filename`` 下载服务器文件到本地. 

<http://www.lellansin.com/putty%E4%B8%8A%E4%BC%A0%E6%96%87%E4%BB%B6.html>

然后这个put和get的命令在文件传输比较慢的时候也没有什么进度提示, 不过可以再开一个putty登录进服务器, 然后用 ``ls -lh`` 看看已经传输了多少了...
