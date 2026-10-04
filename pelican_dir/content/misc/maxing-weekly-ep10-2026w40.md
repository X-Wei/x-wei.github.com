Title: Maxing周刊 EP10 2026w40: "LLM"怎么读
Date: 2026-10-04
Category: misc
Tags: weekly
Slug: maxing-weekly-ep10-2026w40

## news / 新闻

- 迪拜航空劫机事件
- Google动态:
  - [Gemini4 Argon发布](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
    - 为啥这次不叫Pro了...
    - 我用下来感觉和Opus 5.5体感差不多? 或者说我的日常工作已经测不出这些模型的智能区别了
    - 能力虽然不错, 但槽点是外部用户还暂时用不上 依旧贷款冠军🏆...
    - 不过已经在收紧免费用户的模型配额了(Gemini/Antigravity), 应该是为了给Argon发布腾出算力
  - [Google发射TPU上天](https://mp.weixin.qq.com/s/1kRkj814wwzQvS6E-cWguQ) -- 搭乘SpaceX火箭上天, 算是太空算力第一步? 挑战依旧很多, 比如太空辐射/散热/故障维修/etc.
- OpenAI DevDay 2026：发布个人 Agent (dots) 与 GPT-6.1 Sol
  - GPT6-Sol上线一周就被取代 成为最短命旗舰模型
  - dots, 上周就开始爆火的muse, 还有更早的grok bot, 和又起大早赶晚集的Gemini Spark -- 感觉各大厂的目光投向了同一个方向? 利好CPU/云服务?
    - 上周浅尝了一下Gemini Spark, 感觉比较一般...
    - 但说实话家里有台Mac mini以后 这些服务对我吸引力一般

## gems / 分享

- Karpathy的[LLM输出规范](https://36kr.com/p/4009626690539397) / [X原帖](https://x.com/karpathy/status/2105819303471976479)
  - 大神出手就是不同凡响, 这次解决的是人脑如何快速理解AI的输出的问题
  - 采用了航空手册的规范 要求输出更简单清晰, 另外还有引导模型直接输出可以交互的html和动画 -- 下周看看效果如何吧
  - 大约一年前 [Karpathy guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md) 也火了一阵 我一直装着这个skill, 主要的作用还是约束大模型理解需求, 不要过度设计
  - 随着模型的进步 **现在的瓶颈已经渐渐从控制LLM别跑偏 改成了人类能否快速理解LLM给的结论了**

- [小米的训练mimo-2.6Pro实时直播](https://mimo.xiaomi.com/rl/#overview)
  - 可以看到training curve以及benchmark的表现, 烧了300万刀
  - 这个公开程度至少值得表扬👍

- 写到这想起来一个很小的Tip: **"LLM"怎么读**: 
  - 如果按照标准英文字母念法, "LLM"发音非常拗口
  - 我的方案是把重音放在双L连读上 -- 🗣️ **"艾来赖木"** 

- Antigravity 使用tip: `/browser`激活浏览器自动化
  - chrome授权以后 就可以帮你操作浏览器, 而且还会*截图或者录屏* 记录agent的操作流程
  - 一旦迈出这一步 把一些不那么重要的浏览器任务交给agent, 就打开了新世界的大门(见下文)



## misc / 杂记

### 运动:
- 健身三天, 两次瑜伽一次力量 本周依旧比较疲劳...
- 周五拉伸以后标准引体做了7个 有进步

### 周末带娃 
- SBB天票好去处: [Stanserhorn石丹峰缆车🚠](https://www.myswitzerland.com/zh-hans/experiences/stanserhorn-vintage-cable-car-amp-cabrio-cable-car/)
  - 1893年的上山齿轮火车
  - 2012年新建的世界首个敞篷双层缆车
  - 非常赞的一点是 每个时段的座位有限(会提前给你发一张占位票) 不会出现别处缆车人挤人的现象..
  - SBB天票完美覆盖所有内容 -- 木质小火车和缆车用easyride不划算(往返的火车+缆车就要至少41CHF了)
  - 海拔比瑞吉山还高一点 高处可以看到10个湖泊(就认出来了卢塞恩湖和楚格湖), 还有土拨鼠乐园(不过没见到土拨鼠)

- [楚格佛光静心小院](https://events.mindfulpeace.org/s/a6d014f0-e660-43c7-abf0-059b666b34da)
  - 周日参加了他们组织的正念徒步活动
  - 类似于基础的正念练习, 把日常生活的很多事情全身心地投入, 走路就全神贯注的走路, 吃饭就仔细品味每一口食物的味道
  - 加上周围美丽的风景和明媚的天气, 非常棒的体验! 🏞

### 把更多任务交给agent
以前我不愿意(或者不敢)把包含个人数据的任务交给远程agent, 有点数据洁癖了. 但是最近发现, 一旦迈过这个坎, 把一些相对不太隐私机密的信息和任务放手交给AI, 真的是立竿见影的提效!

- 我选择用antigravity, 主要感觉Google的用户数据管理还是比较能让人放心的...
- 不太敏感的文件直接丢给它 让它分析研究 给结论
  - 比如, 用它来对比几个搬家公司的合同&报价, 以及给出推荐建议 -- 没有AI这会是一个至少两小时的费神工作
- 用`/browser`自动操作浏览器
  - 几分钟修好了家里的wifi放大器问题 -- 只需要登陆wifi控制台然后把地址交给它就好了
  - 我自己部署的openlist想要添加GoogleDrive mount -- [openlist官方tutorial](https://doc.oplist.org/guide/drivers/google_drive)太长了而且有的地方已经过时, 很难follow, 交给它以后, 几分钟就帮我搞定了GCP上的各种设置问题

