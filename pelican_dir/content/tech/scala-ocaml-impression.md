Title: Scala/OCaml初体验  
Date: 2016-12-31  
Slug:  scala-ocaml-impression  
Tags: scala, OCaml  
   
[TOC]  
  
  
2016年的最后几小时, 随便写写关于Scala和OCaml的一些入门体验好了.   
  
今年对FP语言特别感兴趣, 上了两门Scala的公开课([here](https://www.coursera.org/learn/progfun1/home/welcome) and [here](https://www.coursera.org/learn/progfun2/home/welcome))和一门OCaml的公开课([here](https://www.fun-mooc.fr/courses/parisdiderot/56002S02/session02/info)), 在博客中写了一系列的笔记, 课后作业也都认真做完了. 斗胆说这两门语言都算入门了吧... 这里就随便写一下使用这两门语言的感受, 想到哪里写到哪里...   
  
FP语言和之前接触的语言确实不大一样, 比如之前我都有种错觉, 学什么语言只要知道循环/条件/基本类型运算怎么写, 就差不多可以上手了...... 然后遇到了FP, 发现循环语句其实是不必要的... 记得看到过一篇文章, 类比学FP就好像开了很多种车的老司机突然开始学开宇宙飞船, 肯定各种WTF不适应了~   
  
以前谈到FP我只能联想到一些Python里的FP特性: lambda表达式, 高阶函数之类的, 顶多还想到个闭包... 不过Python里面的FP特性和Scala/OCaml里的比起来还是差了不少: i.e. 现在非常希望Python里可以支持pattern matching...   
  
Scala  
=====  
Scala算是比较亲民的FP语言了(和Java有点像...), 也是我最早接触的FP语言. EPFL的那两门公开课质量很棒, 毕竟是Scala的作者亲自来上的...   
  
  
* *immutable types*: 习惯了就好, 就像java里所有东西都是final的, 要修改什么东西的时候改成新建一个, immutable数据的优点就是并行方便啊...   
* *一切皆为表达式*, specifically, ``if``语句也是表达式(expression)而不是语句(statement)  
* 尽量不用``return``, 返回值就是最后一句expression  
* 类型推导: 就不用写麻烦的类型标记了(有时又必须写, 比如必须要告诉Scala递归函数的返回类型)... 不过有时不标记类型又容易出错(心里以为的类型和实际的类型不一样). 另外Scala的类型是写在冒号后面的, 习惯了就好...   
* **for expression**: (和"for循环"不是一回事) 非常好用, 可以说是一大亮点, 比较复杂的``filter/map``组成的表达式, 用for expr写出来非常容易理解, 超棒... 后来学OCaml的时候非常期待OCaml里也有类似的东西(不过好像没有...)  
* pattern matching: 用constructor来switch! 没什么好说的 非常好用的东西...  
* [lazy evaluation和Stream](http://x-wei.github.io/progfun2_lec2_lazyeval.html#lecture-22-streams): 非常有用的东西, 学到这里时很受启发...   
* intellij真好用, 还有Scala worksheet...   
* **尾递归优化**: 把递归函数做到和iterative的一样快, tailrec算是工具之一吧.   
    一开始对tailrec有点不太会写, 其实后来大概明白了怎么回事: 尾递归要求``f(n)``最后的return语句里应该直接是递归调用``f(n-1)``, 不要加别的什么带``f(n-1)``的表达式.   
    一般的递归函数大概是: ``f(n) = some_expr_of f(n-1)``, 而tailrec的版本里, 加入了``acc``这样一个参数, 保存累加结果. *可以把acc看做f(n-1)的代替品*, 这时, 把那个f(n-1)的expr作用在``acc``上, 就是尾递归了! f(n, acc)最后一句就成了``f(n-1, some_expr_of acc)`` — 简简单单一个递归调用~  
    举个最简单的例子: 阶乘运算  
    非尾递归的写法是:   
  
```scala  
def factorial(n:Int): Int =    
  if(n==0) 1 else n*factorial(n-1)  
```    
改成尾递归以后:   
```scala  
def factorialTR(n:Int):Int = {    
  @tailrec    
  def fact(n:Int, acc:Int):Int = {    
    if(n==0) acc    
    else fact(n-1, n*acc)    
  }    
  fact(n, 1)    
}  
```  
  
* 简单的匿名函数有几种写法:   
	* 用``=>``: ``param  => ret ``  
	* 用pattern matching(这时要用花括号): ``{case(param list)  => ret }``  
	* 下划线就表示参数: ``_*2`` — 相比之下 简直受够了Python里面写lambda.......  
* 一些概念和Java对应一下:   
	* ``Unit``对应Java里的``void``  
	* ``Option``对应Java里的Object(有指针的对象), Java里的``null``对应Scala里``None``, Java里的某个对象(非null)``A``对应Scala里的``Some[A]``, Scala里和``Option``类似的还有``Try``  
	* ``trait``大概可以看做Java里的``Interface``, 不过Scala的trait是可以包含函数实现的...   
	* Scala的``object``和Java里可不是一个意思, Scala里object是单例对象(*Singleton*), 类似于java里的``static final``的对象  
* 有人说Scala被过度设计了, 感觉有点道理: 快学完第二门Scala公开课的时候看看别人代码, 又发现了好多没见过的关键字... @@  
* 并不太喜欢省略点号 省略括号/分号之类的语法糖...  
* Scala的collection有点多: ``Seq/List/Array/IndexedSeq/Vector``傻傻分不清楚....  
  
![](../images/scala-ocaml-impression/pasted_image.png)  
  
  
  
OCaml  
=====  
OCaml也是工业界比较成功的语言了, 而且据说速度和Cpp不相上下, 我对它可以说是向往已久, 看到FUN平台上有公开课就赶紧报名了...   
  
OCaml算是比较"正宗"的FP语言(或许还不够"纯"?), 风味和别的语言差了好多, 但是写着写着就喜欢上了...   
  
  
* 函数参数不用括号! 这是第一个冲击...  
* 不过总是把函数放在最前面, 还是不大习惯, 比如``List.map``, 更希望可以写成 ``a_list map a_fun``这样...  
* 运算符完全分隔: 整数加法是``+``, 浮点数加法要显示写成``+.``, 这样做的好处就是可以做异常强大的类型推导, 比Scala不知高到哪里去了~  
* 各种错误都可以在编译时找到, 安全感倍增...   
* **let-in binding**: 理解了这个概念以后, 大脑有了一种开窍的感觉! 这个就非常接近数学推导了, 比如在数学上证明什么东西的时候, 令x y z等于什么什么, 其实最终都是为了在最后一个表达式里面体现. 只是起一个名字而已, 并不是改变了这些"identifier"的数值. Scala里面的"最后一个表达式即为返回值"这一点, 我当时有点不太习惯, 不过在OCaml里面用let-in绑定这么一写, 这不是显然的么?! ...总之这个写法理解了以后, 感觉非常美妙...   
* 函数的类型为``para1_type -> para2_type -> ... -> ret_type``, 这样写了以后对于理解partial function之类的就有很大帮助, 另外OCaml并不区分数值和函数了: 都是用let声明, 一个数值可以看做是接收0个参数的函数.   
* ``try-with``处理异常: 除了处理异常以外, 由于没发现break对应的写法, 现在要break的时候我就也写成``try-with``...   
* basic composed types: ``tuple/record/array``这三个, 个人感觉并不是特别好用... @@  
* **taged type** (又叫sum type/variant type): 感觉非常强大, 定义了taged type以后再pattern matching不要太爽... 感觉我对这块理解还不太够, 看别人写的taged type可能可以写一些处理的函数, 自己定义taged type就比较虚了... 好的程序, 把类型定义写好了 基本上就完成一半了...   
* 关于模块(module)的签名的写法什么的, 其实还是有点晕... 可能实践还是不够  
* OCaml里的"Polymorphism"大概相当于Java里的generic/Cpp里的template.   
* pattern matching: 在OCaml里被大量的应用, 感觉比Scala里面的还好用不少...   
* utop作为交互式终端体验还是很棒的  
* 编辑器和ide还是不够丰富, 没找到(非vim/emacs)很好的方案... 不过FUN平台的网络编辑环境非常给力, 自动indent这个feature太喜欢了, 最后所有作业都是直接在web环境下写的...   
* opam包管理器有时候会出现一些模块安装不上的问题  
* 听说``Core``提供了比较完善的函数支持, 希望学一下(也就是看看real world OCaml)  
  
  
compared with Python  
====================  
那么这两个语言和我现在用得最多的语言(Python)相比较一下吧:   
  
  
* 作为Python, 非常羡慕Scala/OCaml的执行速度  
* 眼馋pattern matching和各种compile time保护......   
* Python的REPL([bpython](https://bpython-interpreter.org/))还是比Scala worksheet / ocaml utop体验好不少   
* Python的"自带电池"特色是很大的优点, 很好奇Scala/OCaml有没有提供defaultdict/counter/datetime之类的模块......   
  
