Title: Scrapy 上手笔记
date: 2015-04-19
Slug: Scrapy 上手笔记
Tags: python, scrapy
 

Scrapy是用来爬取数据的很流行的包, 这里小记一下. 以前几天做的[一个爬虫](https://github.com/X-Wei/OneArticleCrawler)为例子, 这个爬虫把韩寒一个app的前九百多期的文章抓了下来. 

I. installation
---------------
scrapy的安装参考: <http://scrapy-chs.readthedocs.org/zh_CN/latest/topics/ubuntu.html>

(直接pip安装的好像缺少什么包)


II. prerequisite
----------------

### XPath
需要学习scrapy首先需要会XPath, 这是一种方便与在html/xml文档里查找所需元素的语句. 这个还是很好学的, 其实只需要花一刻钟时间看看w3school的[教程](http://www.w3school.com.cn/xpath/), 就可以掌握够用的知识进行下一步了. 

这里总结一下我觉得会用到的语句(不全, 不过经常用到): 

* ``//book``	选取所有名字叫做book的元素
* ``bookstore/book`` 选取bookstore的子元素中所有叫book的元素
* ``//title[@lang='eng']`` 选取lang属性为"eng"的所有title元素
* ``//titile/text()`` 选取title元素的文字内容
* ``descendant-or-self::text()``: 选取自己或者所有后代节点的文字内容


另外还有个在线测试XPath语句的网站, 可以用这个测试XPath语句: 

<http://xpath.online-toolz.com/tools/xpath-editor.php>

### 审查元素
再一个就是要用chrome的"审查元素"功能, 用这个功能可以看到想查找的网页内容对应在html文件的位置, 甚至可以直接右键复制想要的元素的XPath......(不过有时候并不是最合理的, 所以刚才XPath也不是白学...)

III. scrapy shell
-----------------
网上的教程一般是从一个[tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html)开始的, 介绍了一个小项目, 但是我觉得从scrapy shell开始应该更合理, 有时候甚至没必要建立一个工程, 在这个shell里就可以抓到想要的数据. 

启动的办法很简单: 

    $scrapy shell 'url'

其中``url``就写想要爬取的一个网址. 

这个shell简单说来, 就是一个测试爬虫的交互环境, 除了*多了一些特殊变量和函数*, 就是一个普通的(i)python shell. 

先说两个scrapy shell多出来的变量: 

* ``response``: 把启动的``url``抓取后得到的``Response``对象, 比如 ``response.body``就包含了抓取来的html内容
* ``sel``: 用刚刚抓取的内容建立的一个``Selector``对象, 简单理解, Selector对象可以让我们执行XPath语句提取想要的内容

经常的用法就是用``response``对象查看爬取的情况(``response.status``), 用``sel``对象测试XPath的正确:
``sel.xpath("xpath_statement").extract()`` 会在获取的response.body里用xpath查找并提取内容. 

再说两个scrapy shell添加的函数:

* ``fetch(request_or_url)``: 修改请求或者网址, 这样scrapy shell会从新用这个request/url抓取数据, 相应的sel和response等对象也会自动更新. 
* ``view(response)``: 在浏览器里查看刚刚抓取的内容.


这里举个例子, 抓取一个的文章标题: 

```
	$ scrapy shell 'http://wufazhuce.com/one/vol.921#articulo'
	......
	In [1]: response.status
	Out[1]: 200
	In [2]: sel.xpath('//*[@id="tab-articulo"]/div/h2/text()').extract()
	<string>:1: ScrapyDeprecationWarning: "sel" shortcut is deprecated. Use "response.xpath()", "response.css()" or "response.selector" instead
	Out[2]: [u'\n\t\t\t\t\t\t\u78b0\u4e0d\u5f97\u7684\u4eba\t\t\t  \t\t']
	In [3]: print sel.xpath('//*[@id="tab-articulo"]/div/h2/text()').extract()[0]
	
							碰不得的人
```
scrapy shell的完整文档在: 
<http://doc.scrapy.org/en/latest/topics/shell.html>

IV. scrapy project
------------------
接下来说建立scrapy工程, 这个按照tutorial走就好了. 
建立工程: 
``scrapy startproject my_proj``

会新建一个my_proj文件夹, 里面的结构是: 

	$ tree 
	.
	└── my_proj
		├── scrapy.cfg
		└── my_proj
			├── __init__.py
			├── items.py
			├── pipelines.py
			├── settings.py
			└── spiders
				└── __init__.py

要修改的文件主要有两个: 

* ``items.py`` 定义要抓取的数据
* ``spiders/xxx.py`` 定义自己的爬虫


### 1. 自定义爬虫
先定义爬虫, 在spiders文件夹里面, 新建一个python文件, 这里定义一个``scrapy.spider.Spider``的子类: 
``` python
class OneSpider(scrapy.spider.Spider):
	name = "one_spider"
	start_urls = [ "http://wufazhuce.com/one/vol.%d#articulo"%i for i in range(1,924) ]
	def parse(self, response):
		title_path = '//*[@id="tab-articulo"]/div/h2/text()' 
		title = response.xpath(title_path).extract()[0].strip()
		print title
```
这里, Spider子类一定需要定义三个东西: 

1. ``name``：　 是爬虫的名字, 一会爬取的时候需要
2. ``start_urls``:　启动时进行爬取的url列表
3. ``parse()`` 方法


爬虫启动的时候会把每一个start_urls里的网址下载, 生成的``Response``对象会传入这个``parse()``方法, 这个方法负责解析返回的``Response``对象, 提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象等...

### 2. 保存抓取的信息到item
刚才只是做到了抓取需要的信息, 还没有能够保存到文件里, 下面要将抓取的信息做成一个``Item``保存.

**首先定义要保存的信息:** 

修改items.py文件, 里面定义一个``scrapy.Item``的子类:
``` python
class OnearticleItem(scrapy.Item):
	# define the fields for your item here like:
	vol = scrapy.Field()
	title = scrapy.Field()
	author = scrapy.Field()
	content = scrapy.Field()
```

这个文件很简单, 只是说明一下要抓取的信息, 他们都是``scrapy.Field()``, 这个东西类似一个字典.

**然后在爬虫里保存item:**

为了保存抓取的内容, 在parse()方法里, 得到需要的数据以后, 新建一个``OnearticleItem``, 把抓到的内容放进这个item里, 然后返回这个item即可. 
``` python
def parse(self, response):
    nb = re.findall('\d+',response.url)[0]
    title_path = '//*[@id="tab-articulo"]/div/h2/text()' 
    author_path = '//*[@id="tab-articulo"]/div/p/text()' 
    content_path = '//div[@class="articulo-contenido"]/descendant-or-self::text()' 
    title = response.xpath(title_path).extract()[0].strip()
    author = response.xpath(author_path).extract()[0].strip()
    content = '\n'.join(  response.xpath(content_path).extract()   ).strip()
    print nb,title,author
    item = OnearticleItem()
    item['vol'] = nb
    item['title'] = title
    item['author'] = author
    item['content'] = content
    return item
```

### 3. 运行爬虫
以上的文件修改好了以后, 只需*在命令行里*启动爬虫即可, 这时候就用到了刚才定义的spider的``name``属性:

``$scrapy crawl one_spider -o one.csv``

大约几分钟功夫, 九百多篇文章就放到了one.csv文件里~
