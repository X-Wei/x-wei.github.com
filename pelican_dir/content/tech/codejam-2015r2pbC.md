title: codejam2015-round2-pbC 的三种解法       
Date: 2016-05-27     
Slug: codejam-2015-r2pbC     
Tags: algorithm, codejam   
 
[TOC] 
   
昨天做的一道codejam题目, 这个题目的三种解法都非常有代表性, 特此一记.    
   
题目链接在这里:    
<https://code.google.com/codejam/contest/8234486/dashboard#s=p2>   
   
>Elliot's parents speak French and English to him at home. He has heard a lot of words, but it isn't always clear to him which word comes from which language! Elliot knows one sentence that he's sure is English and one sentence that he's sure is French, and some other sentences that could be either English or French. If a word appears in an English sentence, it must be a word in English. If a word appears in a French sentence, it must be a word in French.      
>Considering all the sentences that Elliot has heard, what is the minimum possible number of words that he's heard that must be words in both English and French?        
   
>* Input       
>The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a single line containing an integer N. N lines follow, each of which contains a series of space-separated "words". Each "word" is made up only of lowercase characters a-z. The first of those N lines is a "sentence" in English, and the second is a "sentence" in French. The rest could be "sentences" in either English or French. (Note that the "words" and "sentences" are not guaranteed to be valid in any real language.)   
   
>* Output       
>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of words that Elliot has heard that must be words in both English and French.   
   
>* Limits     
>1 ≤ T ≤ 25.   
>Each word will contain no more than 10 characters.   
>The two "known" sentences will contain no more than 1000 words each.   
>The "unknown" sentences will contain no more than 10 words each.   
>Small dataset   
>2 ≤ N ≤ 20.   
>Large dataset   
>2 ≤ N ≤ 200.   
   
我的codejam程序模板长这样:    
   
	def readval(typ=int):   
		return typ( raw_input() )   
	   
	def readvals(typ=int):   
		return map( typ, raw_input().split() )   
	   
	def testcase(cas):   
		print 'Case #%d: %d' % ( cas, res )   
	   
	if __name__=='__main__':   
		T = int(raw_input())   
		for i in xrange(T):   
			testcase(i+1)   
   
   
法1: 穷举 bruteforce (for small testcase)   
======================================   
在small set(N=20) 中, 对于那18个未知语言的句子, 每句可能是英语或法语. 那么穷举所有可能性, 然后选择双语单词最少的即可. 2^18约等于几十万 , 按说python还是可以handle的 (2^10=1k, 2^ 20=1M, python每秒大约能循环几百万次).    
   
naive bruteforce   
----------------   
   
生成所有的可能性组合, python的``itertools``包里提供了[combinations](https://docs.python.org/2/library/itertools.html#itertools.combinations)函数, ``combinations(iterable, r)``返回所有在iterable中大小为r的子集(的迭代器):    
   
	>>> from itertools import combinations   
	>>> for c in combinations('ABCD', 2): print c   
	('A', 'B')   
	('A', 'C')   
	('A', 'D')   
	('B', 'C')   
	('B', 'D')   
	('C', 'D')   
   
   
用``combination``函数即可实现枚举每句话是英语还是法语的功能.    
   
当每句话是英语还是法语已经确定以后, 可以用集合取交集的方法(``set1.intersection(set2)``)得到两种语言一共有多少个重复的单词. 程序长这样:    
   
	def testcase(cas): # not fast enough...   
		N = readval()   
		En = set( readvals(str) )   
		Fr = set( readvals(str) )   
		if N==2:    
			print 'Case #%d: %d' % ( cas, len(En.intersection(Fr)) )   
			return   
		scent = []   
		for i in xrange(N-2):   
			scent.append( set(readvals(str)) )   
		def partition(engsubset):    
			allEn, allFr = En.copy(), Fr.copy()   
			for i in xrange(N-2):    
				if i in engsubset: allEn.update(scent[i])   
				else: allFr.update(scent[i])   
			return len( allEn.intersection(allFr) )    
		possibleres = []   
		for l in xrange(N-2):    
			for engsubset in combinations(xrange(N-2), l):    
				possibleres.append(partition(engsubset))   
		res = min(possibleres)   
		print 'Case #%d: %d' % ( cas, res )   
   
   
然而, 下载了small testcase以后运行程序, 速度还是不够快, 大约要十分钟才有结果 — 而codejam的提交时间限制是4分钟啊... 程序每次检查2^18种可能性, 但是由于每次检查都要进行集合的union和intersection操作(这种操作的效率并不高, 甚至C++里也是一样), 这个操作太耗费时间了所以不行...    
   
bruteforce using bitmap   
-----------------------   
   
需要更加聪明的穷举方法, 自然的想法就是用bitmap(或者叫bitvector?). 之前的两个基本操作都可以用bitmap完成:    
   
   
* 枚举各个句子的语言种类: 如果每个句子用一位来表示的话(1代表英语, 0代表法语), 那么用N位的bitmap即可表示一种情形. 这个bitmap只需从0增加到2^N-1, 就把2^N个可能性都遍历了. (实际上是2^N-2个可能性, 因为前两个句子已经确定语言了).    
* 两种语言的词汇表进行union/intersection: 假设共有K个不同的单词, 那么用一个K位的bitmap即可表示一种语言包含了哪些单词. 然后集合的union和intersection即可表示为OR和AND的逻辑运算.    
   
   
bit manipulation蛮subtle的, 不过习惯了就好... 另外python的integer可以任意长度, 不用像C/java那样考虑bitmap位数大于64的情况, 还是非常方便的. 代码如下:    
   
	def testcase(cas): # use bitmap instead of set to speedup for small case !!    
		N = readval()   
		scent = []; allwords = set()   
		for i in xrange(N):    
			scent.append( readval(str) )   
			allwords.update( scent[i].split() )   
		words = sorted(allwords)    
		# if K distinct words in total, each sentence can be reprensented as a K-bit bitmap   
		bitmaps = []    
		for i in  xrange(N): #construct bitmaps   
			bm = 0   
			for wd in scent[i].split():   
				bm |= ( 1<< words.index(wd) )   
			bitmaps.append(bm)   
		res = 1e10   
		# look for all combinations    
		for i in xrange(1<<(N-2)):   
			en = bitmaps[0]; fr = bitmaps[1]   
			for k in xrange(N-2):   
				if (1<<k) & i > 0: en |= bitmaps[k+2]   
				else: fr |= bitmaps[k+2]   
			res = min( res, bin(en&fr).count('1') )   
		print 'Case #%d: %d' % ( cas, res )   
    
   
以上代码在我电脑上执行small的时候大约花费1分钟, 比最开始用set的速度提高了十倍. 当然, 对于large的case这种解法肯定就超时了...    
   
法2: 最大流 maxflow   
===============   
   
这个方法也是官方[analysis](https://code.google.com/codejam/contest/8234486/dashboard#s=a&a=2)里提供的答案. 如果将所有句子``S``以及所有单词``w``看作节点, 每个句子的节点``S``于它包含的单词的节点``w``相连, 问题转化成了从节点``S1``到节点``S2``的vertex cut问题 (选取最小的节点集合, 将该集合的节点去掉以后S1和S2不再联通).    
   
然后这个问题又可以转为边的min cut问题: 只需要把每个单词节点w分成左右两个节点``w1``和``w2``, 并且这样添加边(假设w在句子S中):    
   
* ``w1-->w2``, capacity=1   
* ``S-->w1``, capacity=INF   
* ``w2-->S``, capacity=INF   
   
   
在这样构造的图里计算maxflow即可得到mincut, 也就是题目的答案...    
   
在实现这个解法的时候用到了networkx这个包, 它提供了比bgl好用100倍的接口(虽然也比bgl慢差不多100倍 ==...). *任何hashable的object都可以用来作为节点的index*, 所以写起来非常舒服, 15行搞定:    
   
	def testcase_maxflow(ind): # using maxflow !   
		INF = 1e10   
		import networkx as nx   
		G = nx.DiGraph()   
		N = readval()   
		for i in xrange(N):   
			words = readvals(str)   
			si = 'sent-%d'%i   
			G.add_node( si )   
			for wd in words:    
				G.add_edge( wd+'_l', wd+'_r', capacity=1 )   
				G.add_edge( si, wd+'_l', capacity=INF )   
				G.add_edge( wd+'_r', si, capacity=INF )   
		flow_value, flow_dict = nx.maximum_flow(G, 'sent-0', 'sent-1')   
		print 'Case #%d: %d' % ( ind, int(flow_value) )   
   
   
用这个代码即可轻松通过large case... maxflow的建模还真是艺术...orz   
   
法3: 线性规划 (integer) linear programming   
=====================================   
   
写完上面那个解法以后, 我又看了看[大神](https://www.go-hero.net/jam/15/name/linguo)的解法, 发现他居然用的是[pulp](https://pythonhosted.org/PuLP/pulp.html)(python线性规划的包), 于是自己想了一下, 这个问题确实可以用线性规划来建模 !    
   
首先说一句pulp这个包, 它提供了非常好用的接口来构造LP问题, 增加约束或者定义objective只要用``prob+=[expression]``就好了, 可以说比AMPL好用不少... 下面是一个简单的例子:    
   
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
   
   
OK, 本题的建模过程如下:    
对于每一个句子``S``, 定义binary的LP变量``Se``, Se=1表示句子S为英语, =0表示为法语.    
对于每个单词``w``, 定义两个binary变量``we``, ``wf``, 表示单词w是英(法)语单词.    
然后, 再定义变量``wef``, 它表示单词``w``既是英语单词又是法语单词. 所以有这个逻辑关系: ``wef = we AND wf`` 那么这种逻辑关系如何用线性约束描述呢? 可以这样: ``wef >= we+wf-1`` 非常巧妙吧...   
([这篇文章](http://cs.stackexchange.com/questions/12102/express-boolean-logic-operations-in-zero-one-integer-linear-programming-ilp)总结了各种逻辑关系用线性规划的描述方式, 写的得非常详细. )   
   
要最小化的目标函数就是 ``sum(wef)`` 了, 约束除了刚才那个``wef >= we+wf-1``以外, 还要表达单词和句子之间的关系: 如果一个句子为英(法)语, 那么句子里的每一个单词都为英(法)语. 这是一个``se==>we``的逻辑关系, 用线性约束表达为: ``we>=se``.    
   
所以整个模型是:    
   
	Minimize sum(wef)   
	st:   
	we >= se   
	wf >= (1-se)   
	wef >= we+wf-1   
	Se[0]==1, Se[1]==0   
   
用pulp编写的代码如下:    
   
	def testcase(ind):# formulate it as linear programming    
		N = readval()   
		sentc = []   
		allwords = set()   
		for i in xrange(N):   
			sentc.append( set(readvals(str)) )   
			allwords.update( sentc[-1] )   
		words = sorted( allwords )   
		M = len(words)   
		wordsindex = {words[i]:i for i in xrange(M)} # mapping a word to its index   
		pb = LpProblem('Bilingual', LpMinimize)   
		# LP variables   
		Se = [ LpVariable('Se_'+str(i), cat='Binary') for i in xrange(N) ] # Se[i] = indicator(scentence i is english)   
		we = [ LpVariable('we_'+str(j), cat='Binary') for j in xrange(M) ] # we[j] = indicator(word j is english)    
		wf = [ LpVariable('wf_'+str(j), cat='Binary') for j in xrange(M) ] # wf[j] = indicator(word j is french)    
		wef = [ LpVariable('wef_'+str(j), cat='Binary') for j in xrange(M) ] # wef[j] = indicator(word j is BOTH en and fr)    
		pb += sum( wef )   
		pb += Se[0]==1   
		pb += Se[1]==0   
		for i in xrange(N):    
			si = sentc[i]   
			for wd in si:    
				j = wordsindex[wd]   
				pb += we[j] >= Se[i]   
				pb += wf[j] >= (1-Se[i])   
		for j in xrange(M):    
			pb += wef[j] >= we[j]+wf[j]-1 # # wef[i] = we[i] && wf[i]   
		#~ pb.solve( GLPK(msg=0) )   
		pb.solve(  )   
		res = int( value(pb.objective) )   
		print 'Case #%d: %d' % ( ind, res )   
   
    
以上代码在small上运行约1分钟, large约3分钟.    
   
另外我发现[另一个大神](https://www.go-hero.net/jam/15/name/liutianren)代码里没有用Binary/Integer的lp变量, 也就是说他用的是连续的线性规划! 当我把变量的定义改成:    
   
	Se = [ LpVariable('Se_'+str(i), 0, 1) for i in xrange(N) ] # Se[i] = indicator(scentence i is english)   
	we = [ LpVariable('we_'+str(j), 0) for j in xrange(M) ] # we[j] = indicator(word j is english)    
	wf = [ LpVariable('wf_'+str(j), 0) for j in xrange(M) ] # wf[j] = indicator(word j is french)    
	wef = [ LpVariable('wef_'+str(j), 0) for j in xrange(M) ] # wef[j] = indicator(word j is BOTH en and fr)   
    
   
这样以后, 得到的结果还是正确的!! (不过代码运行时间没有显著的提高).    
   
所以是这个模型中的矩阵满足[totally unimodular](https://en.wikipedia.org/wiki/Unimodular_matrix#Total_unimodularity)性质?    
不过这个模型似乎并不满足wikipedia里写的那个充分条件?...@@    
[这里](https://kunigami.wordpress.com/2013/08/12/tu-matrix-recognition/)有一篇真•大神的文章是讲如何识别TU矩阵的 (tl;dr......), 那么是不是各种solver内部已经有了自动判断TU的代码, 所以这两种程序的运行时间差不多?...    
   
总而言之这道题目还是非常有意思的, 三种解法都很有代表性, 这里的技巧估计在codejam里会经常用到...    
