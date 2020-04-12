Title: R语言从入门到放弃 (2). 向量(列表)及函数
Date: 2016-07-26 23:48
Slug:  Rnotes-2-seq_func
Tags: R
Series: R语言从入门到放弃
 


首先, R似乎默认所有的变量都为向量vector, 即使一个单独的数字也是长度为1的, 所以``1``等价于``c(1)``.  

	> a <- 1
	> a
	[1] 1
	> length(a)
	[1] 1
	> a[1]
	[1] 1
	> typeof(a)
	[1] "double" # means "double vector" (I think)
	> 1 == c(1)
	[1] TRUE


fancy indexing
--------------
R的vector/list/matrix支持类似numpy(稍有不同)的fancy indexing, 以下是例子: 

	> v <- 1:10
	> v[1:3] # slicing
	[1] 1 2 3
	> v[-(1:3)] # EXCLUDING first 3 elements
	[1]  4  5  6  7  8  9 10
	> v[-1] # EXCLUDING first element
	[1]  2  3  4  5  6  7  8  9 10
	> v[c(2,4,9)]
	[1] 2 4 9
	> v[v%%2==0] # indexing using logical array
	[1]  2  4  6  8 10
	
	# works also for lists
	> l <- list(1,2,3,"aa")
	> l[-1]
	[[1]]
	[1] 2
	
	[[2]]
	[1] 3
	
	[[3]]
	[1] "aa"


以下是矩阵的fancy indexing例子: 

	> mat <- matrix(1:9, nrow=3, ncol=3)
	> mat
	     [,1] [,2] [,3]
	[1,]    1    4    7
	[2,]    2    5    8
	[3,]    3    6    9
	> mat[1,]
	[1] 1 4 7
	> mat[1,c(2,3)]
	[1] 4 7
	> mat[-1,]
	     [,1] [,2] [,3]
	[1,]    2    5    8
	[2,]    3    6    9
	> mat[,2]
	[1] 4 5 6


names / dimnames
----------------
好玩的是可以用``names``/``dimnames``函数给每个值加上一个名字: 

	> names(v) <- paste("elem", sep="-", 1:length(v))
	> v
	 elem-1  elem-2  elem-3  elem-4  elem-5  elem-6  elem-7  elem-8  elem-9 elem-10 
	      1       2       3       4       5       6       7       8       9      10 
	> names(v) <- paste("elem", sep="_", 1:length(v))
	> v
	 elem_1  elem_2  elem_3  elem_4  elem_5  elem_6  elem_7  elem_8  elem_9 elem_10 
	      1       2       3       4       5       6       7       8       9      10 
	> v$elem_1
	Error in v$elem_1 : $ operator is invalid for atomic vectors
	> v["elem_1"]
	elem_1 
	     1
	> names(l) <- paste("elem", sep="_", 1:length(l))
	> l$elem_1
	[1] 1
	> l[1]
	$elem_1
	[1] 1
	> l["elem_1"]
	$elem_1
	[1] 1

上面例子看到, vector不能使用``$``来获得"field", 但是list可以, 这是list和vector的一个区别. 

下面是矩阵的例子: 
	
	> dimnames(mat) <- list( paste("row",sep="_", 1:nrow(mat)), paste("col",sep="_", 1:ncol(mat)) )
	> mat
	      col_1 col_2 col_3
	row_1     1     4     7
	row_2     2     5     8
	row_3     3     6     9
	> mat["row_1","col_1"]
	[1] 1
 


c()
---
关于``c``这个函数, 值得一提的除了它自动"展开"参数的list/vector以外(上次博客提到), 还有就是它会自动cast, 文档里是这么说的: 

>The output type is determined from the highest type of the components in the hierarchy NULL < raw < logical < integer < double < complex < character < list < expression. 

其中的logical, integer, character都属于(atomic) vector, list和他们不同, 见后文. 

以下是例子: 

	> c(1,2,TRUE) # logical < integer
	[1] 1 2 1
	> c(1,2,"char") # integer < character
	[1] "1"    "2"    "char"
	> c(1,2,list(1)) # integer < list
	[[1]]
	[1] 1
	
	[[2]]
	[1] 2
	
	[[3]]
	[1] 1


vector VS list ( matrix VS data.frame )
---------------------------------------
用于集合主要是vector和list, 他们的区别是: **vector只能存放同样类型的元素, 而list可以存放不同类型的元素***.* 

vector可以是: numeric, logical, char... 类比一下, vector类似java里的array, list类似python的list. 

另外访问第i个元素, vector是 ``v[i]``, 而list需要用两个括号 ``l[[i]]``(``l[i]``还是一个list, ``l[[i]]``才是想要的东西... )

看例子: 

	> c(1,2,3) # numeric vector
	[1] 1 2 3
	> c(1,2,"a") # c() 自动cast把前两个数字转成了char, 变成一个char类型的vector
	[1] "1" "2" "a"
	> list(1,2,"a") # list
	[[1]]
	[1] 1
	
	[[2]]
	[1] 2
	
	[[3]]
	[1] "a"

同理, matrix和data.frame也类似, matrix的所有元素必须相同, 而data.frame可以每一列各不相同(不过一列之中需要相同). 另外data.frame也支持用``$``选取一列, matrix则不支持.

functions
---------

R的函数定义为如下形式, 注意, 函数体的最后一句就是返回值, 不用显示写"return" (类似scala).

	myfunnction <- function(params, ...){
	  # ...
	  the.return.value
	}

另外注意到上面函数定义, 参数里有三个点``...``, 这个不是必须的, 它的的作用见下一节. 

R是函数式语言: 一个function可以作为参数传递, 例子就是``apply``, 见下一节.

apply/lapply/sapply
-------------------

### apply
apply这个函数的doc写到用法为: 

``apply(X, MARGIN, FUN, ...)``

``X``是操作的数据(**一般为matrix**), ``MARGIN``为选择对行或列操作(类似numpy的``axis``参数), ``FUN``就是作为参数传入的函数了. 

	> mat <- matrix(1:12, nrow=3, ncol=4)
	> mat
	     [,1] [,2] [,3] [,4]
	[1,]    1    4    7   10
	[2,]    2    5    8   11
	[3,]    3    6    9   12
	> apply(mat, 1, sum) # apply on row
	[1] 22 26 30
	> apply(mat, 2, sum) # apply on col
	[1]  6 15 24 33


这里类似做reduce操作, 而MARGIN就是指定要reduce哪一个维度. 

另外文档里的三个点``...``很有意思, 它是**参数FUN的额外参数** ! 下面是一个例子, 给FUN传入了一个匿名函数: ``function(x,power) sum(x^power)``, 它计算x里元素的power次方, 然后加起来. 所以在apply里可以指定FUN这个``power``参数的数值, 这就对应着apply用法里的这三个点``...``.

	> apply(mat, 1, function(x,power) sum(x^power), power=1 )
	[1] 22 26 30
	> apply(mat, 1, function(x,power) sum(x^power), power=2 )
	[1] 166 214 270


### lapply/sapply
如果说上面``apply``一般用在matrix上, 用于将一个matrix **reduce**为向量的话, ``lapply/sapply``就是**map**操作了: 作用在一个vector/list上, 返回对每一个元素进行操作后的新list. 

它们的区别大概是: lapply返回list, sapply返回vector. 

	> sq <- function(x) x^2
	> l <- list(1,2,3,4)
	> v <- 1:4
	> lapply(v, sq) # lapply returns a list
	[[1]]
	[1] 1
	
	[[2]]
	[1] 4
	
	[[3]]
	[1] 9
	
	[[4]]
	[1] 16
	
	> lapply(l, sq) # lapply returns a list
	[[1]]
	[1] 1
	
	[[2]]
	[1] 4
	
	[[3]]
	[1] 9
	
	[[4]]
	[1] 16
	
	> sapply(v, sq) # sapply returns a vector
	[1]  1  4  9 16
	> sapply(l, sq) # sapply returns a vector
	[1]  1  4  9 16

