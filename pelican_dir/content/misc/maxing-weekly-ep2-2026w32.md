Title: Maxing周刊 EP2 2026w32
Date: 2026-08-09
Category: misc
Tags: weekly
Slug: maxing-weekly-ep2-2026w32

### news / 新闻
- **Google管理层变动**: Jeff Dean离开, Demis卸任Deepmind CEO
  - 不管是同事圈还是自媒体的报道, 震动都挺大的
  - Jeff Dean算是工程师之神了吧 几乎所有google的基础设施都是他参与构建的: protobuf/spanner/mapreduce/tensorflow/... 还有他的[latency numbers everyone should know](https://medium.com/@bojanskr/latency-numbers-every-programmer-should-know-d85f8d3f8e6a)也是系统设计的经典内容
  - 对Demis了解不多, 感觉卸任CEO的原因估计也是Gemini模型持续不给力, 而他更热衷于AI4Science两方面的结果吧
  - 看了不少人的评价和报道 大意就是Google在Gemini和GCP之间选择了来钱更快的GCP, 与此同时原来那个与众不同的Google可能也一去不复返了
- **长鑫存储上市即成为中国市值第一**
  - 简单了解了一下背景, 感觉除了创始人NB, [合肥国资委](https://wallstreetcn.com/articles/3778000)也确实厉害啊, 逆势押注给长鑫续命, 活该人家现在赚麻了
  - 另外合肥还有京东方和蔚来汽车, 不得不说合肥当年的领导有点水平
  - 长鑫好像目前还是只能生产消费级的DRAM -- 那也很不错了 赶紧把存储的价格卷下来吧 这两年涨价太严重了!
  - AI计算需要的HBM他们暂时还造不了, 但我觉得也就是迟早的事...
- **竹知了事件发酵**
  - 总之就很难评... 觉得正反两方都挺无聊的
  - 对比一下雷军对于玩梗的包容度就高不少

### gems / 分享
- **工具分享**: [codexbar](https://github.com/steipete/CodexBar)
  - 来自openclaw之父的小工具
    - (话说openclaw从年初的爆火到现在基本销声匿迹 也就几个月时间吧 AI圈实在是日新月异)
  - 作用是快速在桌面panel查看各种AI订阅的用量, 还是蛮方便的, 还提供了CLI版本方便做自动化.
- **博主推荐**: (小红书) [营养师Zoe倬倬](https://xhslink.cn/m/4cvk6mwEm6o)
  - 住在德国的营养师 分享一些德国超市/药店可以买到的补剂/食物, 感觉蛮靠谱的
  - 她(以及很多别人)很推荐的D3+K2+镁的组合, 看到[migros上也可以买到](https://www.migros.ch/de/product/522003500000)

### misc / 杂记
- **本周Gemini笑话**: 
  - > 美国政府宣布, 不允许美国用户未经授权使用Gemini4, 只能授权给海外用户使用
  - 很多人说Gemini是美国豆包就罢了 看到这一条我真绷不住了😂
  - 不过我的观点一直是 **"以大多数人的prompt/harness水平 根本用不到拼模型能力"** (from "以大多数人的努力水平 根本用不着拼天赋")
  - 你说Gemini表现拉吧 其实多加一些约束, 多给一些context/skill 日常工作其实也很够用了...

- [**我的chrome插件**](https://chromewebstore.google.com/detail/pageanno-%E2%80%94-web-highlights/pfndflekgohhakofbdmkgihchmckijhk)
  - 这周上架了公司内部版本 -- 代码一点没改 但是不这么上架一下 内部文档的页面就无法trigger
  - 这周还是很忙 没时间把代码开源, 又鸽了
  - 这里简单说一下为什么用我的不是其他竞品:
    - 高亮内容对网页内容的更新非常鲁棒 -- 尤其对那种经常更新的内部文档页面非常有用 否则很容易几周前的高亮文字在网页内容改变以后就完全错位了
    - 只用chrome自带的加密同步和本地存储机制, 数据完全不经过第三方 -- 这保证了可以在任何敏感内容(比如内部文档)上使用
    - 有搜索功能 查找之前的高亮内容 -- 有时候想不起来某个事情在什么地方, 搜索可以快速找到对应的网页和段落

- **回归经典工具**
  - **笔记工具**: 在高强度使用obsidian几周以后 我又切回了[zim wiki](https://zim-wiki.org/)
    - 原因就是zim的WYSIWYG编辑功能实在太流畅了 写作完全没有摩擦
    - 当然zim有它自己的问题, 比如没有tabs -- 但我之前自己写了一个tabbar插件完美解决
    - 目前还没搞定的是zim不支持章节折叠 -- 有空的时候vibe一下
    - 之前很好奇为啥它编辑功能为啥这么强, 用GLM的服务搞了个[zim的代码wiki](https://zread.ai/zim-desktop-wiki/zim-desktop-wiki)
  - **思维导图**: [freeplane](https://docs.freeplane.org/)依旧最好用
    - freeplane有一说一默认的主题和模板确实丑 但是我自定义了模板 再把快捷键自己调教一下 用的算是非常顺手了
    - 但之前还有一些使用上的不便之处 一些小的细节 本来以为不好弄 结果随手google一下, AI Overview给了我一个可以settings的选项就搞定了!
    - 还发现可以通过脚本来做一些节点样式的自动化 我想要输入特定链接就默认给节点添加图标的功能(有点类似GoogleDoc里的自动chipify links功能), 用gemini很快就实现了 -- 不禁感叹我对freeplane的开发还不到百分之一!!
  - 以上两个工具, **都是开源了20多年的老牌效率软件**, 这么多年来(尤其最近几年) 涌现了很多很fancy的技术和工具 可这俩依旧能打 历久弥新 (虽说历史包袱肯定少不了吧...)

