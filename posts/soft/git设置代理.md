Title: git push使用代理
Date: 2012-09-21 11:22
Slug: git push使用代理
Tags: git


来到X之后, 上外网全部要用代理的, 非常不爽... 而且ubuntu的所谓的全局代理设置(首选项-->网络代理)好像并不管用... 设置了之后apt-get命令可以用, 但是常用软件(最常用莫过于chrome了)都要单独设置才可以...

然而极为不爽的是git, 这边可以clone, 但是一到push的时候就报错:

    $ git push 
    ssh: connect to host github.com port 22: Network is unreachable
    fatal: The remote end hung up unexpectedly

前一篇帖子把"Toefl"写成了"Tofel"...... 囧大了, 然后想改过来发现没法push...

不过今天终于弄好了, 虽然不太明白是怎么弄好了的... 这里记一下.

参考了[这篇文章](http://blog.csdn.net/itstarting/article/details/7305384), 不过好像又不大一样(我实在是不懂这个东西是什么原理, 只要求能用就好...).

首先, 设置代理地址和端口:

    $ git config --global http.proxy=yourproxyserver:theport

然后好象就好了...... 不过push的时候要指定用户名和https的地址, 根据提示输入github密码才能使用.

    $ git push https://x-wei@github.com/X-Wei/x-wei.github.com/
    Password: 
    Counting objects: 234, done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (153/153), done.
    Writing objects: 100% (153/153), 28.73 KiB, done.
    Total 153 (delta 141), reused 0 (delta 0)
    To <https://x-wei@github.com/X-Wei/x-wei.github.com/>
       7ec6f3f..957ede7  master -> master

好吧暂时就这样用吧, 虽然原理是什么我完全不知道......
