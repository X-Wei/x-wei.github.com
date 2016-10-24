title: codejam常用(python)解题工具          
Date: 2016-05-27 18:00        
Slug: codejam-python-tools   
Tags: algorithm, codejam, python      
 
[TOC] 
   
总结一下用python撸codejam时常用的一些库, 并且给一些简单的例子. 发现用python撸codejam非常合适: codejam的时间要求不严格(4/8分钟), 而且程序只要本地运行. 正好可以使用python简洁的语法和丰富的函数库.    
   
collections   
===========   
py自带的一些好用的数据结构...  
<https://docs.python.org/2/library/collections.html>    

``from collections import Counter, deque, defaultdict``   
   
itertools   
=========  
主要是用来穷举的时候它里面一些函数很好用... 

<https://docs.python.org/2/library/itertools.html>   
   
    >>> from itertools import product, combinations   
    >>> a = 'ABCD'; b='EFG'   
    >>> for p in product(a,b):    
    print p   
    ...        
    ('A', 'E')   
    ('A', 'F')   
    ('A', 'G')   
    ('B', 'E')   
    ('B', 'F')   
    ('B', 'G')   
    ('C', 'E')   
    ('C', 'F')   
    ('C', 'G')   
    ('D', 'E')   
    ('D', 'F')   
    ('D', 'G')   
    >>> for c in combinations(a, 2): print c    
    ...        
    ('A', 'B')   
    ('A', 'C')   
    ('A', 'D')   
    ('B', 'C')   
    ('B', 'D')   
    ('C', 'D')   
    >>> for p in permutations(b,2): print p   
    ...    
    ('E', 'F')   
    ('E', 'G')   
    ('F', 'E')   
    ('F', 'G')   
    ('G', 'E')   
    ('G', 'F')   
   
   
bitmap   
======   
聪明一点的穷举需要用bitmap... 实测可以加速十倍...

### use bitmap for combinations (2^N possibilities)   
   
(N elements, each element 2 choices)   
``for mask in xrange(1<<N): ...``   
   
### set/clean Kth bit   
   
set: ``bm |= 1<<k``   
   
clean: ``bm &= ~(1<<k)``   
   
### count nb of 1s in a bitmap   
   
``bin(bm).count('1')``   
   
   
networkx   
========   
   
常用的图论算法都在里面了. nx最棒的是**任何hashable的object都可以用来作为节点的index**, 再想想用C++的bgl, 简直蛋疼...
<https://networkx.readthedocs.io/en/stable/>   
   
### constructing graph   
   
	>>> import networkx as nx   
	>>> G = nx.DiGraph() # use `Graph` for undired graph, `MultiGraph` for dup-edges   
	>>> G.add_node('a') # any hashable obj can be used as node index   
	>>> G.add_edge(1,2) # missing nodes will be automatically added   
	>>> G.add_edge(1,3) # if G is undired(`Graph`), 1-->3 and 3-->1 will be added   
	>>> G.nodes()   
	['a', 1, 2, 3]   
	>>> G.edges()   
	[(1, 2), (1, 3)]   
	>>> G.add_edge(1,2); G.add_node('a') # nx ignores duplicate adding edges/nodes    
	>>> G.nodes()   
	['a', 1, 2, 3]   
	>>> G.edges()   
	[(1, 2), (1, 3)]   
	>>> G[1] # outgoing edges from a node   
	{2: {}, 3: {}}   
	>>> G[1][2]['color']='blue' # easily add edge properties    
	>>> G[1]   
	{2: {'color': 'blue'}, 3: {}}   
	>>> G.add_edge(1,2, capacity=1) # this is another way to add property   
	>>> G.edge   
	{'a': {}, 1: {2: {'color': 'blue', 'capacity': 1}, 3: {}}, 2: {}, 3: {}}   
	>>> G.node['a']['cat']='string node' # can also be: G.add_node('a', cat='string node')   
	>>> G.node   
	{'a': {'cat': 'string node'}, 1: {}, 2: {}, 3: {}}   
   
   
### DiGraph: topo-sort, cycle-detection, strongly connected component   
   
<http://networkx.readthedocs.io/en/stable/reference/algorithms.shortest_paths.html>   
   
	>>> import networkx as nx    
	>>> G = nx.DiGraph()   
	>>> G.add_edge(1,2); G.add_edge(1,3); G.add_edge('a','b')   
	>>> list( nx.strongly_connected_components(G) )   
	[set(['b']), set(['a']), set([2]), set([3]), set([1])]   
	>>> nx.topological_sort(G)   
	[1, 2, 3, 'a', 'b']   
	>>> G.add_edge(2,3); G.add_edge(3,1); G.add_edge('b','a')   
	>>> list( nx.simple_cycles(G) )   
	[[1, 3], [1, 2, 3], ['a', 'b']]   
	>>> list( nx.strongly_connected_components(G) )   
	[set(['a', 'b']), set([1, 2, 3])]   
	>>> G.add_edge(3,4); G.add_edge(4,'a')   
	>>> nx.shortest_path(G,1,'a')   
	[1, 3, 4, 'a']   
	>>> G.add_edge(1,3,weight=2); G.add_edge(1,2,weight=3)   
	>>> nx.shortest_path(G,1,'a')   
	[1, 3, 4, 'a']   
	>>> nx.shortest_path_length(G,1,'a')   
	3   
	>>> nx.shortest_path_length(G,1,'a','weight') # set attribut edge 'weight' as weight, (if not present, weight=1 )   
	4   
   
   
### Undirected Graph: connected component, MST   
<http://networkx.readthedocs.io/en/networkx-1.11/reference/generated/networkx.algorithms.mst.minimum_spanning_tree.html#networkx.algorithms.mst.minimum_spanning_tree>   
   
	>>> G = nx.Graph()   
	>>> G.add_edge(1,2); G.add_edge(1,3); G.add_edge('a','b')   
	>>> list( nx.connected_components(G) )   
	[set(['a', 'b']), set([1, 2, 3])]   
	>>> G.add_edge(2,3)   
	>>> mst =  nx.minimum_spanning_tree(G) # returns a new graph   
	>>> mst.edges()   
	[('a', 'b'), (1, 2), (1, 3)]   
	>>> G.add_edge(1,3,weight=2) # mst takes attribut 'weight', if no present, weight=1   
	>>> nx.minimum_spanning_tree(G).edges()   
	[('a', 'b'), (1, 2), (2, 3)]   
   
   
### maxflow   
<http://networkx.readthedocs.io/en/networkx-1.11/reference/algorithms.flow.html>   
   
	>>> import networkx as nx   
	>>> G = nx.DiGraph()   
	>>> G.add_edge('x','a', capacity=3.0)   
	>>> G.add_edge('x','b', capacity=1.0)   
	>>> G.add_edge('a','c', capacity=3.0)   
	>>> G.add_edge('b','c', capacity=5.0)   
	>>> G.add_edge('b','d', capacity=4.0)   
	>>> G.add_edge('d','e', capacity=2.0)   
	>>> G.add_edge('c','y', capacity=2.0)   
	>>> G.add_edge('e','y', capacity=3.0)   
	>>> flow_value, flow_dict = nx.maximum_flow(G, 'x', 'y')   
	>>> flow_value   
	3.0   
	>>> print(flow_dict['x']['b'])   
	1.0   
   
   
### maximum matching   
NB: maxi**mum** matching != maxim**al** matching...   
there are maximum-matching functions for general undir graph (``max_weight_matching``) and for bipartitie graph (``maximum_matching``), the one for bipartite graph is faster, the general one takes O(V**3).   
   
<http://networkx.readthedocs.io/en/stable/reference/generated/networkx.algorithms.matching.max_weight_matching.html?highlight=maximum_matching>   
   
	>>> G = nx.Graph()   
	>>> G.add_edges_from([(1,2),(2,3),(3,4),(4,5)])   
	>>> mate = nx.max_weight_matching(G, maxcardinality=True)#mate[v] == w if node v   
	 is matched to node w.   
	>>> mate   
	{2: 3, 3: 2, 4: 5, 5: 4}   
	>>> nx.is_bipartite(G)   
	True   
	>>> mate=nx.bipartite.maximum_matching(G)   
	>>> mate   
	{1: 2, 2: 1, 3: 4, 4: 3}   
   
and there are vertex cover algorithms as well......     
   
pulp   
====  
线性规划的库, 供了非常好用的接口来构造LP问题, 增加约束或者定义objective只要用``prob+=[expression]``就好了, 基本上看看例子就能上手. 
面对选择问题的时候线性规划是不错的方法 -- 如果计算速度可以足够快的话... 
  
<https://pythonhosted.org/PuLP/pulp.html>   
   
	>>> from pulp import *   
	>>> x = LpVariable("x", 0, 3)   
	>>> y = LpVariable("y", 0, 1, 'Integer') # var category can be integer   
	>>> prob = LpProblem("myProblem", LpMinimize)   
	>>> prob += x + y <= 2 # add constraint   
	>>> prob += -4*x + y # add objective   
	>>> status = prob.solve() # solve using default solver   
	>>> status = prob.solve(GLPK(msg = 0)) # or use glpk solver   
	>>> LpStatus[status]   
	'Optimal'   
	>>> value(prob.objective) # see objective value   
	-8.0   
	>>> value(x) # see variable value    
	2.0   


关于nx和pulp的应用可以参考[上篇文章](http://x-wei.github.com/codejam-2015-r2pbC.html).

