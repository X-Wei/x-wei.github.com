Title: python pickle 的一个小问题
date: 2014-07-15
Slug: python pickle 的一个小问题
Tags: python

python的pickle/unpickle机制可以非常方便的保存一些计算的中间结果, 这一点java虽然也可以做到, 但是java里面的包的名字实在是长的让人记不住...

不过今天在使用pickle的时候遇到了一个很奇怪的问题. 

是这样的, 原本写了一个程序``main.py``, 这个程序里进行了一些计算并且pickle下了这些内容, 后来我觉得一个程序main.py写这么多实在太长了, 于是就把那些辅助函数以及class的定义通通放进了一个``util.py``文件里. 并且在main.py的第一行写上: 

``from util import *``

按理说这应该没有问题, 和一个main文件时运行的效果相同的, 但是当我运行的时候却显示util.py里面这行unpickle的语句有错误:

```python
	airport_info = pk.load(file('airport_info.dict', 'rb')) 
	>>AttributeError: 'module' object has no attribute 'Airport'
```

其中``Airport``是我定义的一个类, 本来在main.py里面, 后来被我移动到了util.py里面...

感觉很奇怪, 于是去[水源](https://bbs.sjtu.edu.cn/frame2.html)求助, 果然fcfarseer学长就很快给了[回复](https://bbs.sjtu.edu.cn/bbscon,board,Script,file,M.1405431916.A.html):

>
在pickle一個對象的時候，pickle會記住這個對象的class是定義在哪個python
源文件裏，然後再unpickle的時候，pickle會自動import那個源文件以獲得class的定義。
>
所以如果定義class的文件在這期間改過的話，就會拋出類似的錯誤。


所以问题出在这里(我的理解): 原先我把数据pickle进文件的时候, ``Airport这个class是定义在了main.py里面, 所以当我在util.py里面load数据的时候, pickle发现原来的main.py里面已经没有了 Airport这个class, 于是就出现了Error...``

解决办法也不难, 只需要在``util.py``里面再生成一下那些要load的数据文件, 之后再次unpickle的时候就会去``util.py``而不是``main.py``里找class的定义, 也就没有问题了!

今天碰到的这个问题不是那么evident, 所以特地记一下.



