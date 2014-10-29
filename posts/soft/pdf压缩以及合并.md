Title Linux下pdf文件的压缩与合并
Date: 2014-10-29
Slug: Linux下pdf文件的压缩与合并
Tags: linux


压缩pdf
-----
用``convert`` 好像不太好使: 
``convert -resize 50% input.pdf out.pdf``

用``gs``:
``gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output0.pdf input.pdf`` 

<http://blog.sciencenet.cn/blog-467089-773990.html>

后来发现老是compress以后的结果不好, 看到这篇帖子发现**convert有好多选项**: 
<http://superuser.com/questions/427851/batch-resize-and-compress-pdf-files>

这样convert的效果很好...
``convert -density 200 -compress jpeg transcript-LIU\ Chongmo.pdf trans.pdf``

合并pdf
-----
之前[博客](http://x-wei.github.io/%E5%9B%BE%E7%89%87%E5%90%88%E5%B9%B6%E4%B8%BApdf,%20%E5%90%88%E5%B9%B6mp3,%20%E6%89%B9%E9%87%8F%E5%8E%8B%E7%BC%A9%E5%9B%BE%E7%89%87.html)写过, 用pdfjoin: 

``pdfjoin $(ls *.pdf|sort -n) --outfile xx.pdf``



