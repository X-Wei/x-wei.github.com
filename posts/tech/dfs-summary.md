Title: 深度优先搜索(DFS)小结      
date: 2015-10-18      
Slug: dfs-summary      
Tags: algorithm      
   
今天总结一下也许是搜索问题里最重要的算法: DFS !    
   
由于树可以看成是一个graph, 这里还是只写对于graph的DFS算法. Graph类的定义还是用每一个节点保存邻居信息:    
   
	public class GraphNode{      
		int val;      
		List<GraphNode> neighbors;      
	}   
   
   
为了防止重复, 仍然用一个HaseSet记录走过的节点:    
   
``HasheSet<GraphNode> visited = new HasheSet<GraphNode>();``    
   
Recursive DFS   
-------------   
首先写递归版本的DFS, DFS就是一条路走到底, 不撞南墙不回头, 所以递归写起来很自然: 每到一个节点, 标记其已经访问过了, 然后对于邻居里面没有访问的节点继续递归进行DFS.    
   
递归的DFS代码非常简洁:    
   
	public void DFS(GraphNode nd){      
		System.out.println(nd.val);    
		visited.add(nd);   
		for(GraphNode next: nd.neighbors){   
			if( !visited.contains(next) )   
				DFS(next);   
		}   
	}   
   
虽然这个算法很短, 但是它非常重要, 回溯算法(backtracking)其实就相当于在问题的求解域做一个dfs. 另外拓扑排序也是基于递归dfs进行一点点修改.    
   
Non-recursive DFS   
-----------------   
非递归版本的dfs同样很重要, 因为毕竟非递归的版本效率高一些, 另外这个算法和bfs非常相似, 只不过把队列queue换成了栈stack而已:    
   
	public void DFS(GraphNode start){      
		Stack<GraphNode> s = new Stack<GraphNode>();   
		q.push(start);      
		visited.add(start);      
		while(!s.empty()){      
			GraphNode cur = s.pop();      
			System.out.println(cur.val);      
			for(GraphNode next: cur.children){       
				if(!visited.contains(next)){      
					s.push(next);      
					visited.add(next); // mark node as visited when adding to stack!       
				}      
			}      
		}//while      
	}   
   
同样要注意的一点就是在把一个节点入栈的时刻就将其标记为已访问.    
   
(for Trees) DFS with depth   
--------------------------   
和上次[bfs](http://x-wei.github.io/bfs-summary.html)一样, **对于树而言**, 在dfs搜索的过程中也可以记录该节点所在的depth.    
   
非递归版本的程序就是用一个和上面``s``平行的栈记录深度, 程序和"BFS with distance"很像. 递归版本只要在函数签名里加上一个depth的参数即可. 这两个实现都很简单, 就不写了.    
   
注意这个只对于树有意义, 对一个图而言没有depth一说...    
   
DFS for binary tree: Preorder traversal   
---------------------------------------   
dfs另一个有用的性质是: 对于**二叉树**而言, dfs得到的节点顺序正是其前序遍历(preorder traversal)的顺序.    
   
其实前序遍历的定义就相当于是一个递归版本的dfs了:    
``[preorder(node)] = node.val + [preorder(node.left)] + [preorder(node.right)]``   
   
DFS with path   
-------------   
如果在访问到某一个节点的时候想同时获得到该点的路径, 其实也不麻烦.    
   
对于递归版本的dfs而言, 可以在参数里面用一个List记录到当前节点的路径.    
   
非递归的版本的话... 貌似不是很trival, 需要对stack做好维护, 可能需要一个hashmap什么的... 以后有空了再写写.    
   
Cycle Detection   
---------------   
判断一个有向图是否存在回路是一个非常重要的问题, 简单修改dfs就可以做到了.    
   
在递归版本的dfs里, 我们对每一个点改为**三种标记**:    
*未访问过(0), 正在访问其邻居节点(1), 已经访问完该节点以及所有该节点可以到达的节点(2)*.    

什么时候会出现回路呢? *就是当前节点v的一个邻居u的状态为1的时候*. 因为该节点状态为1, 即还没有把它以后的节点全部遍历, 所以当前节点v肯定可以从u到达, 而现在又可以从v到达u, 所以构成一个回路.    
   
为了表示一个节点的三种状态, 我们把visited的定义改一下, 定义为一个hashmap:       
``HasheMap<GraphNode, Boolean> visited = new HasheMap<GraphNode, Boolean>();``    
   
节点不在visited表示还未访问过, 节点对应为false表示正在访问, 节点对应为true表示已经访问该节点以及所有可以从它到达的节点.    
   
写一下代码:    
   
	public void DFS(GraphNode nd){      
		visited.put(nd, false); // mark as status-1   
		for(GraphNode next: nd.neighbors){   
			if( !visited.contains(next) )   
				DFS(next);   
			else if(visited.get(next)==false) // found cycle   
				System.out.println("Cycle detected!!!");   
		}// now all touchable nodes from nd are visited   
		visited.put(nd, true); // mark as status-2   
	}   
   
非递归版本的话貌似也不很容易, 暂时不写了, 以后有空了考虑一下...   
   
Topology Sort   
-------------   
这一节(以及上一节)参考这个非常棒的视频: <https://class.coursera.org/algo-003/lecture/52>    
   
拓扑排序是一个dfs的应用, 所谓拓扑排序是指在一个DAG(有向无回路图)里给每个节点定义一个顺序(v1...vn), 使得按照这个顺序遍历的节点, 每一个节点vi都是之前遍历过的的节点(v1 ~ vi-1)所指向的(或没有任何其他节点指向的).    
   
好像还没说清楚... 拓扑排序的一个应用就是对于各种依赖性(比如学习课程A需要先学习过课程B)组成的图寻找一个节点遍历的顺序使其可行.    
   
**propositions**:    
   
>* 拓扑排序的结果不唯一.    
* 有回路的图不存在拓扑顺序.   
* 如果一个节点没有出边, 那么它可以放在拓扑排序的最后面(没有节点以来它).   
* 如果一个节点没有入边, 那么它可以放在拓扑排序的最后面.    
   
   
   
简单修改一下递归的dfs就可以处理拓扑排序: 维护一个计数器``K``(初始化为n=所有节点数), 每当一个点已经遍历完毕(所有通过这个点可以到达的点都已经被走过)以后, 就把这个点的顺序设为K, 同时减少K.    
   
就用一个HashMap来为每个节点关联一个序号好了:    
``HasheMap<GraphNode, Integer> order = new HasheMap<GraphNode, Integer>();``    
	   
	public void DFS(GraphNode nd){      
		for(GraphNode next: nd.neighbors){   
			if( !visited.contains(next) )   
				DFS(next);   
		}// all touchable nodes from nd are visited   
		order.put(nd, K--);   
	}   
   
是不是特别简单, 太神奇了!    
   
上面只是对于一个点进行的, 为了给所有点拓扑排序, 只要从一个没有出边的节点出发进行遍历, 一直运行到所有的节点都已经访问过为止.    
   
   
