Title: 最短路径三剑客: Floyd, Dijkstra, Bellman   
date: 2015-10-18 17:00     
Slug: shortest-path-summary      
Tags: algorithm      
Series: 算法笔记
 

   
weighted graph的最短路径问题有三个非常有名的算法, 分别以三个大牛的名字命名, 今天用尽量简洁的篇幅一一介绍.    
   
 简单起见(这回只写伪代码好了), 对于图的定义如下:   
   
* node index = ``{1,2,...,n}``   
* ``e[u,v]`` = distance of edge(u,v); if (u,v) is not an edge, ``e[u,v]=INF``   
* 令N=点的数量, M=边的数量   
   
   
任意两点最短路径: Floyd-Warshall   
========================   
Floyd算法解决的问题是: 对于**任意**两个节点``s``(source)和``t``(target), 求s到达t的最短路径.    
   
Floyd算法的思想是动态规划:    
   
>* 定义``d(i,j,k)``为点i到点j之间, **只允许借道节点1...k的最短路径**   
* 初始化: ``d(i,j,0)=e[i,j] ``(即i到j之间不经由其他任何中转节点的最短路径)   
* 更新dij的公式就是: ``d(i,j,k)=min( d(i,j,k-1), d(i,k-1,k-1)+e[k,j])``   
* 更新n次   
   
   
每次更新dij的意思就是: 现在从i到j可以经过节点k了, 那么看一下ij之间从k这个点经过的话(i → k → j 这条路)能不能缩短dij.    
   
i到j最短路径最终就是: ``d(i,j,n)`` 即i到j的路程可以经过1~n中的任何中转节点.    
   
伪代码特别短(其实真代码也一样短....):    

    for all [i,j]: // initialize   
        d[i,j] = e[i,j]    
    for k = 1 ~ n: // relax for k times:    
        for all [i,j]:   
            d[i,j] = min(d[i,j], d[i,k] + e[k,j])   
   
核心代码只有最后三行... 运行结束后``d[i,j]``就保存着任意i和j之间的最短路径长度.    
程序主循环n次, 每次要处理遍历所有的ij组合, 所以复杂度是**O(N^3)**.    
   
单源最短路径: Dijkstra   
================   
Dijkstra算法解决的问题是: 没有负权边的情况下, 从**源节点**``s``到其他任意节点``t``的路径长度.    
   
   
* 维护一个dist数组, dist[i]就表示(目前为止)s到i的最短距离.    
* 对于每个元素, **标记**是否其dist是否已经确定不再更改(或者说维护两个集合: 一个集合的dist确定, 另一个未确定).    
   
   
Dijkstra算法是一种贪心策略: 每次在未确定最短路径的节点里挑选距离s最近的那个点, 把这个点标记为已经确定dist, 然后对从这个点出发的边进行松弛.    
   
为了标记每个点, 这里用一个bool数组表示: ``determined[i]``为true表示i的dist已经是最短路程, 为false表示还不确定.    
   
算法如下:    
   
>* 初始化``dist[i] = e[s,i]``, ``determined[i]``全为false   
* 在dist未确定的元素里(``determined[i]==false``)寻找一个dist最小的节点``u:``   
	* 标记``u``的dist已经确定``determined[i]=true``   
	* 用u的所有出边进行松弛: s到i如果经过(u,i)这条边会不会变近? ``dist[i] = min(dist[i], dist[u]+e[u,i])``    
	* 重复循环直到所有的点都确定dist(or 重复N遍即可: *每次只会确定一个新的节点的距离*)   
   
   
伪代码:    

	for i in 1~n:   
		dist[i] = e[s,i]   
		determined[i] = false   
	loop N times:    
		u = argmin(dist[i]) among all i that determined[i]==false   
        determined[u] = true // determine one node at each loop     
		for v such that e[u,v]<INF:   
			dist[v] = min( dist[v], dist[u]+e[u,v] )   
   
以上代码的复杂度为O(N^2), 不过如果用堆来优化寻找最近的u的距离, 复杂度可以变得更低.    
   
有负权边的单源最短路径: Bellman-Ford   
=========================   
Dijkstra算法的缺点在于不能处理边长为负数的情况, 而这就是Bellman-Ford算法解决的.    
   
Bellman算法也是一种动态规划(动态规划这个东西就是Bellman提出来的):    
   
>* 定义``d(i,k)``为源点s到i**最多经过k条边的**最短距离   
* 初始化: ``d(i,1)=e[s,i]``   
* 每次更新di的公式: ``for all (u,v): d(v,k)=min( d(v,k-1), d(u,k-1)+e[u,v] ) ``   
* 更新n-1次   
   
   
为什么是更新n-1次? 因为s到i的最短路径至多只有n-1条边(即s到i的路径经过了所有n个点).    
注意每次更新, 需要把**所有的边**试一遍: 看看用每条边(u,v)能不能松弛dv.    
   
伪代码:    

	for i in 1~n:   
		dist[i] = e[s,i]   
	loop n-1 times:    
		for all (u,v) such that e[u,v]<INF:   
			dist[v] = min( dist[v], dist[u]+e[u,v] )   
   
核心代码也是最后三行... 太tm精妙了!!    
   
外层循环N-1次, 内层循环M次, 所以代码的复杂度是O(NM).   
   
More   
====   
以下问题有空再写...   
   
* negative cycle   
* A*   
   
