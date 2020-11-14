Title: 多张图片合并为pdf, 合并mp3, 批量压缩图片
Date: 2012-11-16 19:47
Tags: linux
Slug: 图片合并为pdf, 合并mp3, 批量压缩图片

前一阵遇到的三个小功能, linux下有简单的命令可以实现...

多张图片合并为pdf
--------
这个在网上搜一般找到的结果是:
    
    convert *.jpg xx.pdf

但是这么做的问题是, 运行起来超级慢, 电脑直接卡死!!!

**[2020-update]**

pdfjoin已经没有了, 现在发现用`img2pdf`非常方便:

```bash
$ sudo apt install img2pdf
$ img2pdf $(ls . | sort -n) -o out.pdf
```

**[以下为原始内容]**

后来看了[这里](http://pityonline.info/2009/12/%E7%BB%88%E4%BA%8E%E6%90%9E%E5%AE%9A%E4%BA%86%E5%A4%9A%E5%BC%A0%E5%9B%BE%E7%89%87%E5%90%88%E6%88%90%E4%B8%80%E4%BB%BDpdf%E6%96%87%E6%A1%A3%EF%BC%81/), 知道了可以用pdfjam来做. 先要安装pdfjam, 然后:

先将所有jpg文件重命名为pdf：

    rename 's/\.jpg$/\.pdf/' *.jpg

合成刚重命名的pdf文件为一份：

    pdfjoin $(ls *.pdf|sort -n) --outfile xx.pdf

后来看到pdfjam其实是在用latex, 想到其实也可以先自动生成一个tex文件然后再调用tex生成pdf... 不过既然有现成的软件就直接用吧!!

合并mp3
-----
超级简单的一条命令:

    cat *.mp3 > output.mp3

只要预先把文件按照想要的顺序编号即可
这个操作只是把这些文件前后连接起来, 可能是由于mp3文件格式的原因吧, 只要这么做了就和并完成了!! 而且速度快得惊人!!!

不过有一点问题: 合并出来的mp3文件的信息(歌名, 艺术家之类)会是最后一个文件的信息... 当然这基本不影响使用~

批量压缩图片
------
使用convert命令, 好像是在ImageMagick里面.
参考[这里](http://www.360doc.com/content/11/0704/16/2104556_131439876.shtml):

    #!/bin/bash
    images=`ls *.JPG`
    echo "resize images begining..."
    for image in $images
    do
    convert $image -resize 50% $image;
    echo "resize $image to %50";
    done
    exit

然后就OK了... 顺便吐槽下gmail的附件大小限制!!...
