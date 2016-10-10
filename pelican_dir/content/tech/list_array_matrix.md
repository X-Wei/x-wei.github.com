Title: numpy: list, array, matrix小结   
Date: 2015-09-09   
Slug:  list_array_matrix
Tags: python     

   
python科学计算包的基础是numpy, 里面的array类型经常遇到. 一开始可能把这个array和python内建的列表(list)混淆, 这里简单总结一下列表(list), 多维数组(np.ndarray)和矩阵(np.matrix)的区别.    
   
list列表   
------   
列表属于python的三种基本集合类型之一, 其他两种是元组(tuple)和字典(dict). tuple和list区别主要在于是不是mutable的.    
   
list和java里的数组不同之处在于, python的list可以包含任意类型的对象, 一个list里可以包含int, string或者其他任何对象, 另外list是可变长度的(list有``append``, ``extend``和``pop``等方法).   
   
所以, python内建的所谓"列表"其实是功能很强大的数组, 类比一下可以说它对应于java里面的``ArrayList<Object>`` .    
   
ndarray多维数组   
-----------   
ndarray是numpy的基石, 其实它更像一个java里面的标准数组: 所有元素有一个相同数据类型(dtype), 不过大小不是固定的.    
   
ndarray对于大计算量的性能非常好, 所以list要做运算的时候一定要先转为array(``np.array(_a_list_)``).    
   
   
* ndarray带有一些非常实用的[函数](http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html), 列举几个常用的: ``sum, cumsum, argmax, reshape, T, ...``   
   
   
* ndarray有[fancy indexing](http://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#arrays-indexing), 非常实用, 比如: ``a[a>3]`` 返回数组里大于3的元素   
   
   
* ndarray之间的乘法: 如果用乘法运算符``*``的话, 返回的是每个位置元素相乘(类似matlab里面的``.*``), 想要矩阵相乘需要用``dot()``.   
   
   
* 常见矩阵的生成: ``ones, zeros, eye, diag, ...``   
   
   
matrix矩阵   
--------   
*matrix是ndarray的子类*, 所以前面ndarray那些优点都保留了.    
   
同时, matrix全部都是二维的, 并且加入了一些更符合直觉的函数, 比如对于matrix对象而言, 乘号运算符得到的是矩阵乘法的结果. 另外``mat.I``就是逆矩阵...   
   
不过应用最多的还是ndarray类型.    
   
参考资料:    
<http://docs.scipy.org/doc/numpy/reference/index.html>   
<http://math.mad.free.fr/depot/numpy/base.html>   
<http://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u>   
