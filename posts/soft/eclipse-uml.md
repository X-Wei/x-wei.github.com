title: 使用Eclipse的UML插件生成类图
Date: 2014-05-31
Slug: 使用Eclipse的UML插件生成类图
Tags: java, eclipse

Created samedi 31 mai 2014UML就是可以把程序的结构用图的形式表达出来的东西(好像叫类图), 虽然写程序的时候不大会用到这种东西来搞, 但是写报告的时候如果能够加上一张图的话, 就可以少费些口舌来解释代码了, 而且还有一种高大上的赶脚... 所以写完程序写报告的时候可以用一下. 

废话不多说, 看看我最后生成的UML图:

![](./eclipse的UML插件/pasted_image.png)

这张图表示一个抽象类``Operration``有三个子类, 然后他们之间的关系... 如果用文字的话要解释半天吧...

这张图是用[Green UML](http://green.sourceforge.net/)做出来的, 这是一个eclipse插件, 安装方法为:

* 在eclipse里, ``Help->Install New Software`` 然后Add这个URL: <http://www.cse.buffalo.edu/faculty/alphonce/green>
* 然后一路Next安装就可以了...
* 如果老师显示pending, 可能是代理的问题(在X非常不爽的一点...哎...), 不过没事, 代理的设置在: ``window → preference → General → Network Connections``, 填上就应该好了...


![](./eclipse的UML插件/pasted_image001.png)


* 用Green UML生成类图的时候, 在java文件上点击右键, 选项里有Green UML的选项:

![](./eclipse的UML插件/pasted_image002.png)


* 然后就OK了...


另外还在网上找到了[model goon](http://www.modelgoon.org/), 不过它生成的类图貌似没有把所有信息都标上, 而且不太好看...

