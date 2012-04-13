Title: tex插入程序代码--so easy~
Date: 2012-03-03
Slug: tex_insert_code
Tags: tex

这个问题... 我本来想用python解决的...

但是显然应该先搜一下吧... 果然, 早就有人解决了(其实是tex的常用命令里就有的), 比如[这里](http://hi.baidu.com/xuelicheng/blog/item/194c844a22d2452a09f7ef8a.html)...


    \usepackage{listings}
    \lstset{language=C++}%这条命令可以让LaTeX排版时将C++键字突出显示
    \lstset{breaklines}%这条命令可以让LaTeX自动将长的代码行换行排版
    \lstset{extendedchars=false}%这一条命令可以解决代码跨页时，章节标题，页眉等汉字不显示的问题
    \begin{lstlisting}
    %paste your C++ code here
    \end{lstlisting}


很简单的... 不过比较长的代码换行显示不是很爽(貌似不换行也不是办法啊)... 另外没有颜色高亮哎...


嗯, 貌似[这里](http://bbs.chinatex.org/forum.php?mod=viewthread&tid=3692)的介绍更详细...
还有这个人的[博客](http://aifreedom.com/technology/170)...
[这篇文章](http://blog.sina.com.cn/s/blog_5e16f1770100o9ef.html)是针对python的高亮...

总结一下, 这样比较好:


    \documentclass{article}
    \usepackage{listings}
    \usepackage{xcolor}
    \usepackage{xeCJK}  %必须加xeCJK包
    \setCJKmainfont{WenQuanYi Micro Hei}
    \begin{document}
    \lstset{numbers=left,
    numberstyle=\tiny,
    keywordstyle=\color{blue!70}, commentstyle=\color{red!50!green!50!blue!50},
    frame=shadowbox,
    rulesepcolor=\color{red!20!green!20!blue!20},
    breaklines=true,
    extendedchars=true
    }
    \begin{lstlisting}[language={Python}]
    %这里插入代码~
    \end{lstlisting}
    \end{document}


附件: 我做的一个简单实例
[./insertcode2.tex](./tex_insert_code/insertcode2.tex) 

**imported from zim**



