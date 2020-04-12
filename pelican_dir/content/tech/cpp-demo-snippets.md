Title: C++ STL小结&代码片段  
Slug: cpp-demo-snippets
Tags: C++
Date: 2016-01-09
 
  
总结了一下C++ STL里面用的比较频繁的一些代码片段. (地址: <https://github.com/X-Wei/cpp-demo-snippets/tree/master/STL>)  
cpp文档: <http://en.cppreference.com/w/cpp>  
  
常用的library主要有:   
``<algorithm>, <vector>, <queue>, <set>, <map>, <cmath>``  
  
另外一个常见的cpp文件开头版本是:   
  
	#include <iostream>  
	#include <vector>  
	#include <algorithm>  
	using namespace std;  
	#define forloop(i,lo,hi) for(int i = (lo); i <= (hi); i++)  
	#define rep(i,N) forloop(i,0,(int)N-1)  
  
  
algorithm  
=========  
  
### copy()  
``OutputIt copy( InputIt first, InputIt last, OutputIt d_first );``  
>Copies the elements in the range, defined by ``[first, last)``, to another range beginning at ``d_first``.   
  
注意如果要放入的container大小不够, 最后一个参数要用``back_inserter``.  
  
ex.  
   
	int a[] = {1,2,3,4,5};  
	vector<int> v(5);  
	copy(a, a+5, v.begin());  
	vector<int> v2;  
	// if v2 needs to increase capacity, need to use back_inserter  
	copy(v.begin(), v.end(), back_inserter(v2));   
  
  
### sort()  
``void sort( RandomIt first, RandomIt last, [Compare comp]);``  
>Sorts the elements in the range ``[first, last)`` in ascending order.  
  
	int a[] = {3,1,5,0,8,9};  
	vector<int> v(&a[0], &a[0]+6);  
	sort(a, a+6);  
	sort(v.begin(), v.end());  
  
如果想要降序排列, 可以直接reverse一下: ``reverse(v.begin(), v.end());``  
  
如果自定义比较函数的话, 可以自己写一个cmp函数(内容和重载的小于运算符相同), 然后把函数名放在第三个参数:   
  
	bool my_cmp(const pair<int, int> &lhs, const pair<int, int> &rhs) {  
		return (lhs.first < rhs.first) || (lhs.first==rhs.first && lhs.second < rhs.second);  
	}  
	//...  
	sort(vp.begin(), vp.end(), my_cmp);  
  
  
或者把元素封装为class/struct, 然后重载它的小于号``<``运算符:  
  
	class MyFooClass {  
		public :  
		int x,y;      
		MyFooClass(int xx, int yy){  
			x = xx;  
			y = yy;  
		}  
		bool operator < ( const MyFooClass & other ) const {  
			return (x<other.x) || (x==other.x && y<other.y) ;  
		}  
	};  
	
	struct MyFooStruct {  
		int x,y;  
		MyFooStruct(int xx, int yy){  
			x = xx;  
			y = yy;  
		}  
		bool operator < ( const MyFooStruct & other ) const {  
			return (x<other.x) || (x==other.x && y<other.y) ;  
		}  
	};  
  
  
vector  
======  
  
### vector  
相当于java里面的``ArrayList``.   
主要操作: ``push_back()``, ``pop_back()`` (所以可以当作stack使用).   
  
另外iterator操作也很常用(set, map等同理):   
  
	for(vector<int>::iterator it=v1.begin(); it!=v1.end(); it++)  
			cout << *it << " ";  
  
### pair  
就是一个first一个second.   
另外有``make_pair``函数可以构造pair.   
  
	pair<string, int> p1("pair1", 1);  
	pair<string, int> p2 = make_pair("pair2", 2);  
  
  
另外两个尖括号再一起时一定要中间加空格, 否则就是位操作运算符了!   
``pair<string, pair<int, double> > p3 = make_pair("pair3", make_pair(3,3.33));``  
  
queue  
=====  
包含普通队列和优先队列(pq)  
  
### queue  
  
	bool empty() const;  
	reference front();  
	void push( const value_type& value );  
	void pop();  
  
  
### priority_queue  
(pq的实现也可以用``<algorithm>``里的``make_heap``, ``pop_heap``, ``push_heap``等方法. priority_queue 其实就是algorithm里面函数的封装...)  
和queue的API区别是, pq查看队首的函数叫``top``而不是``front``.  
  
	bool empty() const;  
	const_reference top() const;  
	void push( const value_type& value );  
	void pop();  
  
使用自定义的cmp方法, 可以把cmp的内容作为括号运算符``()``的重载放入一个struct作为第三个类型参数, 第二个是container, 一般用vector即可.   
  
	struct MyCmpStruct{  
		bool operator()(const pair<int, int> &lhs, const pair<int, int> &rhs){  
			return   return (lhs.first < rhs.first) || (lhs.first==rhs.first && lhs.second < rhs.second);  
		}  
	};  
	priority_queue<pair<int,int>, vector<pair<int,int> >, MyCmpStruct> ppq;  
  
另一种方法是自定义元素的struct/class, 然后重载小于``<``运算符为cmp (同sort).   
  
set/map  
=======  
C++里面的set/map是用红黑树实现的, 所以key类型需要支持比较运算.   
set/map也支持iterator操作(``begin()``, ``end()``), 而且由于是BST, 顺序自然是排好了的.   
  
### set  
  
	std::pair<iterator,bool> insert( const value_type& value );  
	void erase( iterator pos );  
	size_type count( const Key& key ) const;  
	iterator find( const Key& key );  
  
* ``insert``和``erase``的参数可以是iterator或者value.   
* ``count``的返回值为1或0  
* ``find``如果没找到则返回``s.end()``  
  
  
### map<K,V>  
map的value_type是一个``pair<K,V>``, 所以遍历是这样:   
  
	for(map<string,int>::iterator it=m.begin(); it!=m.end(); it++)  
			cout << it->first << ":" << it->second << ", ";  
  
  
* insertion: 用``[]``或者``insert``函数  

        map<string,int> m;  
        m["aa"] = 3;  
        m.insert( make_pair("dd", 6) );  
   
  
注意``insert``函数如果key已经存在的话value不会改变! 但是用``[]``的话则可以.   
  
  
* ``erase/find/count``: 同set.   
  
  
