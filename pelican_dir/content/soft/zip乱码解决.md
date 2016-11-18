Title: zip乱码解决
Date: 2012-01-12
Slug: zip乱码解决
Tags: 中文乱码

这个问题困扰了很久, 以前的方法参考了[这里](http://thiger.blog.hexun.com/46569055_d.html), 使用一条命令:
`unzip -O CP936 xxx.zip`
但是谁tm记得住? 所以每次都要上网现查...

今天看到了ubuntu论坛上的[帖子](http://forum.ubuntu.org.cn/viewtopic.php?f=122&t=301951), 六楼给出了终极的解决方案. 

见附件: [zip乱码解决.zip](../images/zip%E4%B9%B1%E7%A0%81%E8%A7%A3%E5%86%B3/zip%E4%B9%B1%E7%A0%81%E8%A7%A3%E5%86%B3.zip) 
这个压缩包中的5个 7z* 文件拷贝覆盖到/usr/lib/p7zip/

代码:
`sudo cp 7z* /usr/lib/p7zip/`

注意以后不要升级p7zip

一切就正常了! 而且打开时也没有乱码! so good!

