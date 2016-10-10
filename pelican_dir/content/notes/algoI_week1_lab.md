Title: [Algorithms I] Week1-Lab: Percolation
Date: 2015-07-07
Slug:  algoI_week1_lab
Tags: algorithm

model & problem
===============
(原文描述太啰嗦了)  
A system using an N-by-N grid of sites.   
→ Each site is either open or blocked.   
→ A **full** site is an open site that can be connected to an open site in the top row via a chain of neighboring open sites. (这个full的定义有玄机 而且导致后面写程序时有个问题, 看论坛想了半天才想出来, 见后文.)  
→ We say the system **percolates** if there is a path of connected open sites form the top row to the bottom row.   

![](images/file:///home/wx/Dropbox/ZIM_NOTES/0._TmpNotes/Algorithms%2C_4th_ed/Week1-Assignment-Percolation/pasted_image.png)   

⇒ pb: if sites are independently set to be open with probability **p**, what is the probability that the system percolates?   
![](images/file:///home/wx/Dropbox/ZIM_NOTES/0._TmpNotes/Algorithms%2C_4th_ed/Week1-Assignment-Percolation/pasted_image001.png)   
→ When N is sufficiently large, there is a threshold value **p*** such that when p < p* a random N-by-N grid almost never percolates, and when p > p*, a random N-by-N grid almost always percolates.   
→ No mathematical solution for determining the percolation threshold p* has yet been derived.   
⇒ Your task is to *write a computer program to estimate p**.   


Method
======


* API:

        public class Percolation {
           public Percolation(int N)               // create N-by-N grid, with all sites blocked
           public void open(int i, int j)          // open site (row i, column j) if it is not open already
           public boolean isOpen(int i, int j)     // is site (row i, column j) open?
           public boolean isFull(int i, int j)     // is site (row i, column j) full?
           public boolean percolates()             // does the system percolate?
           public static void main(String[] args   // test client (optional)
        }


* Corner cases: the row and column indices i and j are integers between 1 and N. **1≤i,j≤N**

if i/j out of range: ``java.lang.IndexOutOfBoundsException``
if N<=0 in constructor: ``java.lang.IllegalArgumentException``

* Performance requirements: N2 for constructor, const for other operations



* **Monte Carlo simulation**
	* all sites init to be closed

    → randomly choose a blocked site (i,j) and open it 
    → *repeat until percolates* ⇒ the fraction of opened sites is an estimation of p*


* ex. 20*20 grid, when percolated: 

![](images/file:///home/wx/Dropbox/ZIM_NOTES/0._TmpNotes/Algorithms%2C_4th_ed/Week1-Assignment-Percolation/pasted_image002.png)   
⇒ estimated p* = 204/400=0.51
	

* repeat the estimation for T times, get T estimations 

    → get mean and std:    
    ![](images/file:///home/wx/Dropbox/ZIM_NOTES/0._TmpNotes/Algorithms%2C_4th_ed/Week1-Assignment-Percolation/pasted_image003.png)   
    → 95% 置信区间:   
    ![](images/file:///home/wx/Dropbox/ZIM_NOTES/0._TmpNotes/Algorithms%2C_4th_ed/Week1-Assignment-Percolation/pasted_image004.png) 
	

* create API for this simulation: 

        public class PercolationStats {
           public PercolationStats(int N, int T)     // perform T independent experiments on an N-by-N grid
           public double mean()                      // sample mean of percolation threshold
           public double stddev()                    // sample standard deviation of percolation threshold
           public double confidenceLo()              // low  endpoint of 95% confidence interval
           public double confidenceHi()              // high endpoint of 95% confidence interval
           public static void main(String[] args)    // test client (described below)
        }
    

    -if  N ≤ 0 or T ≤ 0: ``java.lang.IllegalArgumentException``  
    -``main()`` : takes two command-line arguments N and T  
⇒ performs T independent computational experiments on an N-by-N grid, and prints out the mean, standard deviation, and the 95% confidence interval for p*.   
(Use [standard random](http://introcs.cs.princeton.edu/java/stdlib/javadoc/StdRandom.html) from our standard libraries to generate random numbers; use [standard statistics](http://introcs.cs.princeton.edu/java/stdlib/javadoc/StdStats.html) to compute the sample mean and standard deviation.   
Here is the algo API: <http://algs4.cs.princeton.edu/code/index.php>)  


Code
====

注意一定要用它们提供的那些库, 否则自己写的话代码就长了....   
shuffle, mean, stddev什么的直接用他们的函数库就可以做到.   
<http://algs4.cs.princeton.edu/code/index.php>   
另外UF也是用他们写好的, WeightedQuickUnionUF.   

按照提示, 除了格子的N^2个节点以外再增加两个节点: 顶部和底部的虚拟节点. 这里写的时候注意一开始也是不恩能够把它们与第一行/最后一行相连的 — 要在一个格子open以后再相连. 

### backwash问题  
这次题目有一点比较困难就是, 需要实现isFull()函数, 这个函数判断一个格子(i,j)是否和顶部相连. 这里如果直接用UF的connected()判断是否和顶部虚拟节点相连的话是有问题的, 如下图:   
![](images/file:///home/wx/Dropbox/ZIM_NOTES/0._TmpNotes/Algorithms%2C_4th_ed/Week1-Assignment-Percolation/pasted_image005.png)   
白色格子表示格子是open的, 蓝色格子表示格子是open并且是*full*的(i.e. 和顶部相连的), 左边图片里的状态是对的, 右边图片里底下部分的格子状态则不对: 如左下角的格子, 其实是没有和顶部联通的, 如果我们用两个虚拟节点的话, 由于底部虚拟节点和顶部虚拟节点相连, 所以和底部虚拟节点相连的左下角部分就被判断成了full的. 

这个问题一开始我以为可以很简单解决, 后来发现没那么容易... (注意题目还要求isFull()也要在常数时间给出结果).  
一个不优雅的办法是, 建立两个UF, 一个用来判断percolation, 另一个UF里没有底部虚拟节点所以可以专门用来判断isFull(). 

这样解决的话使可以通过测试, 不过非常不好看, 另外一个UF的内存占用是8N^2(内部有size[]和id[]两个int数组), 比较大. 

在论坛上找了半天, 看了一些人的分享终于想到了这个非常妙的办法: 

1. UF只建立顶部虚拟节点, 不建立底部虚拟节点. 
2. 判断isFull只需要用UF的connected()一下就好了
3. 问题是怎么判断percolation:   
    a. 建立一个数组 ``boolean connectedToBottom[]``, 指示某一点是否和底部相连   
    b. trick在这里: 不必修改一个联通分支的所有点的``connectedToBottom``的值, **只需要修改联通分支的root(UF的find)即可**. 在进行union的时候先查看两个component的root是不是连到底部, 然后有一个连到底部的话, 在union以后把合并后的联通分支的``connectedToBottom``状态改为true即可   
    c. 然后判断percolate: 先找到顶部虚拟节点锁在component的root, 然后看这个root是否连到底部即可!   

这样用一个boolean数组(N^2内存)代替了一个新的UF(8N^2内存), 而且实现也更加优雅.    
非常有意思的练习...




