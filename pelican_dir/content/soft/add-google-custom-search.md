Title: 使用google自定义搜索以及让google收录自己的网站
Date: 2012-04-23
Slug: add-google-custom-search
Tags: pelican, google


虽然我的blog点击人数可能还是个位数的, 我还是每天都想折腾一下它...

bootstrap2模板里提供了很丰富的内容(可以看farseerfc学长的页面), 其中的google站内搜索我觉得很有用, 于是也自己去弄了一下...

#使用google自定义搜索

要登录google[自定义搜索](http://www.google.com/cse/?hl=zh-CN), 的页面, 用google帐号登录, 然后选择新建一个自定义搜索引擎, 会看到这样的界面: 

![](_images/./add-google-custom-search/pasted_image.png)

第一项的名称和描述啥的随便填就行, 关键是第二项"要搜索的网站", 可以点击"了解详情"看一下应该怎么写. 比如我的网站是`x-wei.github.com`, 而且我想是在这个网站的所有子页面中搜索, 于是这里就填写: `x-wei.github.com/*`即可~ 第三项当然是免费版, 然后下一步.

下一步是一个测试, 可以在搜索框里尝试一下能不能得到想要的结果(**我就是这里有问题的, 待会说**). 如果没问题, 点击下一步, 下一步是给出了一段html代码, 把这些代码加入网页就可以添加google自定义搜索栏了(不过使用pelican写博客的话就不用这样了, 见后文).

嗯, 这个过程还是非常简单的吧!~

#如何把自定义搜索栏加入pelican生成的页面

首先, 可能只能使用bootstrap2这个主题... 然后, 在`settings.py`文件里加入这一行: 
`GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"`
注意, 引号里的那一串字符是你刚才申请的自定义搜索引擎的id, 这个id在哪里? 再次登录google自定义搜索, 这次点"管理现有引擎", 点击你刚才创建的那个引擎的"控制面板":

![](_images/./add-google-custom-search/pasted_image001.png)

在基本信息里面就会看到"搜索引擎的唯一 ID", 把那一串数字赋值给GOOGLE_CUSTOM_SEARCH_SIDEBAR即可~

#让google收录你的网站

但是我没有那么顺利的完成以上, 因为我在测试自定义引擎的时候总是搜不到任何我的网站的东西... 还以为是设置搜索的网页格式写错了呢... 非常崩溃... 后来在zyb同学的提醒下意识到可能是google没有收录我的网页... 果然, google怎么也搜不到我的网站的内容唉...

那么怎么才能让google收录自己的网页?? 难道要坐等几个月后google发现我? 呵呵, 其实是可以主动申请让搜索引擎收录自己的网站的, 我看的[这里](http://zhidao.baidu.com/question/102933806.html). 原来就是很简单的一个工作, [登录http://www.google.com/addurl/?hl=zh-CN&continue=/addurl]() (要是想被百度收录就登录 <http://www.baidu.com/search/url_submit.html> ) 填上你的网址以及验证码(google的验证码太难辨认... 而百度的有点太简单了吧...)就可以了, 我昨天填的, 今天一试发现就可以搜索到了! 然后又发现google自定义搜索也好使了!~~


