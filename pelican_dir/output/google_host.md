Title: 修改host访问google的所有服务
Date: 2012-04-18
Slug: google_host
Tags: google, host

google的服务(mail, doc, site, code, project...)很多都实在很方便(个人感觉QQ, 网易什么的和它绝对不是一个档次). 但是比较悲剧的是, google服务在国内不很稳定, 时不时上不去(比如gmail), 而有的服务(比如site)居然完全上不去...

自己的经验, 使用修改host的方式可以比较好的解决这个问题(而youtube啊, facebook啊什么的修改了不一定好使...) 这里贴一下..

其实就是修改一个文件...linux用户修改`/ect/hosts`, windows用户修改`c:/windows/system32/drivers/etc/hosts`.

**2012-07-06更新**

下面这些host不给力了, 新的host见[我的日志](http:x-wei.github.com/google_youku_host_20120706.html)

<S>
关于google的host, 网上到处都是, 比如[这里](http://www.douban.com/note/161139377/), 不过我没有试过这里的host可不可以(应该可以吧...), 还是把我的host贴出来吧. 这里说一下, 我同时还加了去优酷广告(这里修改完了还要[再处理一下](http://x-wei.github.com/host_youkuqiyi.html)), 上youtube(貌似有点问题). 把这些东西粘贴进hosts文件, 即可访问google的服务, gmail也不会抽风了~~
(要是嫌复制粘贴麻烦, 直接[下载hosts文件](./google_host/hosts))</S>
    
    #优酷屏蔽广告规则如下：
    127.0.0.1       stat.youku.com
    127.0.0.1       static.lstat.youku.com
    127.0.0.1       static.atm.youku.com/crossdomain.xml
    127.0.0.1       valb.atm.youku.com
    127.0.0.1       valc.atm.youku.com
    127.0.0.1       valf.atm.youku.com
    127.0.0.1       valo.atm.youku.com
    127.0.0.1       valp.atm.youku.com
    127.0.0.1       vid.atm.youku.com
    127.0.0.1       walp.atm.youku.com
    #土豆屏蔽广告规则如下：
    127.0.0.1       adextensioncontrol.tudou.com
    127.0.0.1       adplay.tudou.com
    127.0.0.1       adcontrol.tudou.com
    127.0.0.1       iwstat.tudou.com
    127.0.0.1       nstat.tudou.com
    127.0.0.1       stat.tudou.com
    127.0.0.1       stats.tudou.com
    127.0.0.1       at-img1.tdimg.com
    127.0.0.1       at-img2.tdimg.com
    127.0.0.1       at-img3.tdimg.com
    127.0.0.1        *.p2v.tudou.com*
    #PS:    127.0.0.1       at-img1.tdimg.com
    127.0.0.1       at-img2.tdimg.com
    127.0.0.1       at-img3.tdimg.com
    #会导致部分图片无显示（与广告挂钩），建议保留at-img1.tdimg.com，其余两条前打个“#”号去掉，最大化的去除广告和显示图片，具体算法自己选择吧。
    #去迅雷看看广告
    127.0.0.1       pubstat.sandai.net
    127.0.0.1       mcfg.sandai.net
    127.0.0.1       biz5.sandai.net
    127.0.0.1       float.sandai.net
    127.0.0.1       recommend.xunlei.com
    127.0.0.1       cl.kankan.xunlei.com
    #去56广告
    127.0.0.1       acs.56.com
    127.0.0.1       acs.agent.56.com
    127.0.0.1       acs.agent.v-56.com
    127.0.0.1       bill.agent.56.com
    127.0.0.1       union.56.com
    127.0.0.1       v16.56.com
    #去搜狐高清广告
    127.0.0.1       images.sohu.com
    #去新浪视频广告
    127.0.0.1       dcads.sina.com.cn
    #去酷6广告
    127.0.0.1       1.allyes.com.cn
    127.0.0.1       analytics.ku6.com
    127.0.0.1       stat0.888.ku6.com
    127.0.0.1       stat1.888.ku6.com
    127.0.0.1       stat2.888.ku6.com
    127.0.0.1       stat3.888.ku6.com
    127.0.0.1       ku6afp.allyes.com
    #去凤凰网广告(不包括直播部分)
    127.0.0.1       img.ifeng.com
    #去pptv.com广告
    127.0.0.1       pp2.pptv.com
    #去cntv广告
    127.0.0.1       d.cntv.cn
    #去乐视广告
    127.0.0.1       pro.letv.com
    #去奇艺广告
    127.0.0.1       afp.qiyi.com
    127.0.0.1       focusbaiduafp.allyes.com
    #去6间房广告(还有一点点残留)
    127.0.0.1       simba.6.cn
    127.0.0.1       pole.6rooms.com
    127.0.0.1       shrek.6.cn
    127.0.0.1       union.6.cn
    #去激动网广告
    127.0.0.1       86file.megajoy.com
    127.0.0.1       86get.joy.cn
    127.0.0.1       86log.joy.cn
        
    #dropbox
    208.43.202.50 www.dropbox.com
    174.129.11.212 dl.dropbox.com
    184.73.163.57 dl-web.dropbox.com
        
    127.0.0.1	localhost Hasee
    127.0.1.1	Hasee
        
    # The following lines are desirable for IPv6 capable hosts
    ::1     ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
        
        
    127.0.0.1 atm.youku.com
        
    127.0.0.1 Fvid.atm.youku.com
        
    127.0.0.1 html.atm.youku.com
        
    127.0.0.1 valb.atm.youku.com
        
    127.0.0.1 valf.atm.youku.com
        
    127.0.0.1 valo.atm.youku.com
        
    127.0.0.1 valp.atm.youku.com
        
    127.0.0.1 lstat.youku.com
        
    127.0.0.1 speed.lstat.youku.com
        
    127.0.0.1 urchin.lstat.youku.com
        
    127.0.0.1 stat.youku.com
        
    127.0.0.1 static.lstat.youku.com
        
    127.0.0.1 valc.atm.youku.com
        
    127.0.0.1 vid.atm.youku.com
        
    127.0.0.1 walp.atm.youku.com
        
        
    127.0.0.1 valf.atm.youku.com
    127.0.0.1 valb.atm.youku.com
    127.0.0.1 vid.atm.youku.com
        
    ##Google.com       Google.com
    2404:6800:8005::68 www.google.com                     #主页
    #2404:6800:8005::68 www.l.google.com
    2404:6800:8005::c1 m.google.com                       #Google移动版
    2404:6800:8005::54 accounts.google.com                #帐户
    2404:6800:8005::62 id.google.com                      #帐号登录
    #2404:6800:8005::62 id.l.google.com                    #
    2404:6800:8005::62 gg.google.com                      #
    #2404:6800:8005::62 csi.l.google.com
    2404:6800:8005::62 safebrowsing.clients.google.com    #安全浏览客户端服务器
    #2404:6800:8005::62 clients.l.google.com
    2404:6800:8005::62 ns1.google.com                     #域名系统服务器ns-soa/ns
    2404:6800:8005::62 ns2.google.com                     #域名系统服务器ns
    2404:6800:8005::62 ns3.google.com                     #域名系统服务器ns
    2404:6800:8005::62 ns4.google.com                     #域名系统服务器ns
    2404:6800:8005::65 services.google.com                #服务申请
    #2404:6800:8005::65 www3.l.google.com
    2404:6800:8005::76 feedproxy.google.com               #Feed代理
    #2404:6800:8005::76 www4.l.google.com
    2404:6800:8005::d2 jmt0.google.com                    #未知
    2404:6800:8005::62 googlemashups.l.google.com         #位置
    ##Google.com.hk    谷歌香港
    2404:6800:8005::2e www.google.com.hk
    2404:6800:8005::2e images.google.com.hk
    2404:6800:8005::2e video.google.com.hk
    2404:6800:8005::2e maps.google.com.hk
    2404:6800:8005::2e news.google.com.hk
    2404:6800:8005::2e translate.google.com.hk
    2404:6800:8005::2e blogsearch.google.com.hk
    2404:6800:8005::2e picasaweb.google.com.hk
    2404:6800:8005::2e toolbar.google.com.hk
    2404:6800:8005::2e desktop.google.com.hk
    2404:6800:8005::2e id.google.com.hk
    ##Google.cn        谷歌中国（启用此地址无法正常使用谷歌音乐）
    #2401:3800:c001::2c www.google.cn                      #主页
    #2401:3800:c001::2c g.cn                               #主页
    #2401:3800:c001::2c google.cn                          #主页
    #2401:3800:c001::2c ipv6cn.l.google.com 
    #IPv6：ipv6.google.cn
    2401:3800:c001::84 music.googleusercontent.cn
    ##Google.com.tw    Google台湾
    2404:6800:8005::2f www.google.com.tw                  #主页
    2404:6800:8005::2f picasaweb.google.com.tw            #picasaweb
    ##Google.co.jp     Google日本
    2a00:1450:8006::30 www.google.co.jp
    #IPv6：ipv6.google.co.jp
    ##
    2404:6800:8005::20 www.google.com.tr 土耳其
    2404:6800:8005::21 www.google.com.au 澳大利亚
    2404:6800:8005::22 www.google.com.vn 越南
    2404:6800:8005::23 www.google.com.pk 巴基斯坦
    2404:6800:8005::24 www.google.com.my 马来西亚
    2404:6800:8005::25 www.google.com.pe
    2404:6800:8005::26 www.google.co.za
    2404:6800:8005::27 www.google.co.ve
    2404:6800:8005::28 www.google.com.ph
    2404:6800:8005::29 www.google.com.ar
    2404:6800:8005::2a www.google.co.nz
    2404:6800:8005::2b www.google.lt
    #2404:6800:8005::2c www.google.cn     中国（已死）
    2404:6800:8005::2d www.google.com.sg
    2404:6800:8005::2e www.google.com.hk 香港
    2404:6800:8005::2f www.google.com.tw 台湾
    2404:6800:8005::30 www.google.co.jp  日本
    2404:6800:8005::31 www.google.ae
    2404:6800:8005::32 www.google.co.uk  英国
    2404:6800:8005::33 www.google.com.gr
    2404:6800:8005::34 www.google.de 
    2404:6800:8005::35 www.google.co.il
    2404:6800:8005::36 www.google.fr     法国
        
    2404:6800:8005::38 www.google.it
    2404:6800:8005::39 www.google.lv
    2404:6800:8005::3a www.google.ca
    2404:6800:8005::3b www.google.pl
    2404:6800:8005::3c www.google.ch
    2404:6800:8005::3d www.google.ro
    2404:6800:8005::3e www.google.nl
    2404:6800:8005::3f www.google.com.ru
    2404:6800:8005::40 www.google.at     奥地利
        
    2404:6800:8005::42 www.google.be
        
    2404:6800:8005::44 www.google.co.kr
    2404:6800:8005::45 www.google.com.ua
        
    2404:6800:8005::48 www.google.fi     芬兰
    2404:6800:8005::49 www.google.co.in
    2404:6800:8005::4a www.google.pt
    2404:6800:8005::4b www.google.com.ly
    2404:6800:8005::4c www.google.com.br
        
    #Web               网页
    2404:6800:8005::68 www.google.com                     #主页
    2404:6800:8005::68 www.l.google.com
    2404:6800:8005::62 www0.l.google.com
    2404:6800:8005::62 www1.l.google.com
    2404:6800:8005::62 www3.l.google.com
    2404:6800:8005::62 suggestqueries.google.com          #搜索建议
    2404:6800:8005::62 suggestqueries.l.google.com        #搜索建议
    2404:6800:8005::62 clients0.google.com                #客户端服务器
    2404:6800:8005::62 clients1.google.com                #客户端服务器
    2404:6800:8005::62 clients2.google.com                #客户端服务器
    2404:6800:8005::62 clients3.google.com                #客户端服务器
    2404:6800:8005::62 clients4.google.com                #客户端服务器
        
    #Images            图片
    2404:6800:8005::68 images.google.com                  #主页
    2404:6800:8005::68 images.l.google.com                #
    2404:6800:8005::62 tbn0.google.com
    2404:6800:8005::62 tbn1.google.com
    2404:6800:8005::62 tbn2.google.com
    2404:6800:8005::62 tbn3.google.com
    2404:6800:8005::62 tbn4.google.com
    2404:6800:8005::62 tbn5.google.com
    2404:6800:8005::62 tbn6.google.com
        
    #Video             视频
    2404:6800:8005::62 video.google.com                   #主页
    #2404:6800:8005::62 video.l.google.com
    2404:6800:8005::62 0.gvt0.com
    2404:6800:8005::62 1.gvt0.com
    2404:6800:8005::62 2.gvt0.com
    2404:6800:8005::62 3.gvt0.com
    2404:6800:8005::62 4.gvt0.com
    2404:6800:8005::62 5.gvt0.com
    2404:6800:8005::62 video-stats.video.google.com
    2404:6800:8005::74 upload.video.google.com
    2404:6800:8005::74 sslvideo-upload.l.google.com
    2404:6800:8005::62 vp.video.google.com 
    2404:6800:8005::62 vp.video.l.google.com 
    2404:6800:8005::62 qwqy.vp.video.l.google.com
    2404:6800:8005::62 nz.vp.video.l.google.com
    2404:6800:8005::62 nztdug.vp.video.l.google.com
    2404:6800:8005::62 pr.vp.video.l.google.com
    2404:6800:8005::62 ug.vp.video.l.google.com
    2404:6800:8005::62 vp01.video.l.google.com
    2404:6800:8005::62 vp02.video.l.google.com
    2404:6800:8005::62 vp03.video.l.google.com
    2404:6800:8005::62 vp04.video.l.google.com
    2404:6800:8005::62 vp05.video.l.google.com
    2404:6800:8005::62 vp06.video.l.google.com
    2404:6800:8005::62 vp07.video.l.google.com
    2404:6800:8005::62 vp08.video.l.google.com
    2404:6800:8005::62 vp09.video.l.google.com
    2404:6800:8005::62 vp10.video.l.google.com
    2404:6800:8005::62 vp11.video.l.google.com
    2404:6800:8005::62 vp12.video.l.google.com
    2404:6800:8005::62 vp13.video.l.google.com
    2404:6800:8005::62 vp14.video.l.google.com
    2404:6800:8005::62 vp15.video.l.google.com
    2404:6800:8005::62 vp16.video.l.google.com
    2404:6800:8005::62 vp17.video.l.google.com
    2404:6800:8005::62 vp18.video.l.google.com
    2404:6800:8005::62 vp19.video.l.google.com
    2404:6800:8005::62 vp20.video.l.google.com
        
    #Map               地图
    2404:6800:8005::68 maps.google.com                    #主页
    2404:6800:8005::68 maps.l.google.com
    2404:6800:8005::62 maps-api-ssl.google.com
    #2404:6800:8005::62 clients.l.google.com
    2404:6800:8005::62 map.google.com
    2404:6800:8005::62 kh.google.com
    2404:6800:8005::62 kh.l.google.com
    2404:6800:8005::62 khmdb.google.com
    2404:6800:8005::62 khm.google.com                     #
    2404:6800:8005::62 khm.l.google.com
    2404:6800:8005::62 khm0.google.com                    #Satellite View
    2404:6800:8005::62 khm1.google.com                    #Satellite View
    2404:6800:8005::62 khm2.google.com                    #Satellite View
    2404:6800:8005::62 khm3.google.com                    #Satellite View
    2404:6800:8005::62 cbk0.google.com                    #Street View
    2404:6800:8005::62 cbk1.google.com                    #Street View
    2404:6800:8005::62 cbk2.google.com                    #Street View
    2404:6800:8005::62 cbk3.google.com                    #Street View
    2404:6800:8005::62 mw0.google.com
    2404:6800:8005::62 mw1.google.com
    2404:6800:8005::62 mw2.google.com
    2404:6800:8005::62 mw3.google.com
    2404:6800:8005::62 mw-small.l.google.com
    2404:6800:8005::62 mt.l.google.com
    2404:6800:8005::62 mt0.google.com
    2404:6800:8005::62 mt1.google.com
    2404:6800:8005::62 mt2.google.com
    2404:6800:8005::62 mt3.google.com
    2404:6800:8005::62 mlt0.google.com
    2404:6800:8005::62 mlt1.google.com
    2404:6800:8005::62 mlt2.google.com
    2404:6800:8005::62 mlt3.google.com
        
    #News              资讯
    2404:6800:8005::68 news.google.com                    #主页
    2404:6800:8005::68 news.l.google.com                  
    2404:6800:8005::62 nt0.ggpht.com
    2404:6800:8005::62 nt1.ggpht.com
    2404:6800:8005::62 nt2.ggpht.com
    2404:6800:8005::62 nt3.ggpht.com
    2404:6800:8005::62 nt4.ggpht.com
    2404:6800:8005::62 nt5.ggpht.com
        
    #Gmail             邮箱
    2404:6800:8005::11 mail.google.com                    #主页
    2404:6800:8005::53 googlemail.l.google.com
    2404:6800:8005::11 googlemail.l.google.com
    2404:6800:8005::12 googlemail.l.google.com
    2404:6800:8005::13 googlemail.l.google.com
    2404:6800:8005::bd chatenabled.mail.google.com        #Gmail中Gtalk聊天服务
    #2404:6800:8005::bd b.googlemail.l.google.com
    2404:6800:8005::62 talk.gmail.com                     #Gmail中Gtalk聊天服务
    2404:6800:8005::62 gmail.google.com                   #
    2404:6800:8005::62 gmail.l.google.com                 #
    2404:6800:8005::62 www.gmail.com                      #Gmail主页
    2404:6800:8005::62 gmail.com                          #Gmail主页
    2404:6800:8005::62 pop.gmail.com                      #pop服务
    2404:6800:8005::62 smtp.gmail.com                     #smtp服务
    2404:6800:8005::62 smtp1.google.com 
    2404:6800:8005::62 smtp2.google.com 
    2404:6800:8005::62 smtp3.google.com 
    2404:6800:8005::62 smtp4.google.com 
    2404:6800:8005::62 smtp5.google.com 
    2404:6800:8005::62 smtp-out.google.com
    2404:6800:8005::62 smtp-out2.google.com
    2404:6800:8005::62 smtp-out3.google.com
    2404:6800:8005::62 imap.google.com                    #
    2404:6800:8005::62 gmail-pop.l.google.com 
    2404:6800:8005::62 gmail-smtp.l.google.com 
    2404:6800:8005::62 gmail-smtp-in.l.google.com 
    2404:6800:8005::62 gmr-smtp-in.l.google.com
        
    #Books             图书
    2404:6800:8005::62 books.google.com                   #主页
    #2404:6800:8005::64 www3.l.google.com
    2404:6800:8005::62 bks0.books.google.com
    2404:6800:8005::62 bks1.books.google.com
    2404:6800:8005::62 bks2.books.google.com
    2404:6800:8005::62 bks3.books.google.com
    2404:6800:8005::62 bks4.books.google.com
    2404:6800:8005::62 bks5.books.google.com
    2404:6800:8005::62 bks6.books.google.com
    2404:6800:8005::62 bks7.books.google.com
    2404:6800:8005::62 bks8.books.google.com
    2404:6800:8005::62 bks9.books.google.com
        
    #Finance           财经
    2404:6800:8005::62 finance.google.com
        
    #Translate         翻译
    2404:6800:8005::62 translate.google.com
        
    #Blog              博客搜索
    2404:6800:8005::63 blogsearch.google.com
    #2404:6800:8005::63 www2.l.google.com
        
    #Calendar          日历
    2404:6800:8005::64 calendar.google.com
    #2404:6800:8005::64 www3.l.google.com
        
    #Photo/Picasa      照片/网络相册
    2404:6800:8005::5d photos.google.com
    #2404:6800:8005::5d picasaweb.l.google.com
    2404:6800:8005::63 picasa.google.com
    #2404:6800:8005::63 www2.l.google.com
    2404:6800:8005::be picasaweb.google.com
    #2404:6800:8005::be picasaweb.l.google.com
    2404:6800:8005::62 lh0.ggpht.com
    2404:6800:8005::62 lh1.ggpht.com
    2404:6800:8005::62 lh2.ggpht.com
    2404:6800:8005::62 lh3.ggpht.com
    2404:6800:8005::62 lh4.ggpht.com
    2404:6800:8005::62 lh5.ggpht.com
    2404:6800:8005::62 lh6.ggpht.com
    2404:6800:8005::62 lh7.ggpht.com
    2404:6800:8005::62 lh8.ggpht.com
    2404:6800:8005::62 lh9.ggpht.com
        
    #Docs              文档
    2404:6800:8005::64 docs.google.com
    2404:6800:8005::64 writely.l.google.com
    2404:6800:8005::62 spreadsheet.google.com
    2404:6800:8005::62 spreadsheets.google.com
    2404:6800:8005::62 spreadsheets0.google.com
    2404:6800:8005::62 spreadsheets.l.google.com
    2404:6800:8005::62 writely.google.com
    2404:6800:8005::62 writely.l.google.com
    2404:6800:8005::62 writely-com.l.google.com
    2404:6800:8005::62 writely-china.l.google.com
        
    #Reader            阅读器
    2404:6800:8005::68 reader.google.com
    2404:6800:8005::68 www2.l.google.com
        
    #Sites             协作平台
    2404:6800:8005::65 sites.google.com
    #2404:6800:8005::65 www3.l.google.com
    #2404:6800:8005::62 ghs.google.com
    #2404:6800:8005::62 ghs.l.google.com
        
    #Group             论坛
    2404:6800:8005::62 groups.google.com
    2404:6800:8005::62 groups.l.google.com
    2404:6800:8005::89 *.googlegroups.com
    2404:6800:8005::89 blob-s-docs.googlegroups.com
    2404:6800:8005::89 2503061233288453901-a-1802744773732722657-s-sites.googlegroups.com
        
    #Scholar           学术搜索
    2404:6800:8005::62 scholar.google.com
    2404:6800:8005::62 scholar.l.google.com
        
    #Tools             工具
    2404:6800:8005::62 tools.google.com
    2404:6800:8005::62 tools.l.google.com
        
    #Code              代码
    2404:6800:8005::64 code.google.com                    #主页
    2404:6800:8005::64 code.l.google.com                  #
    2404:6800:8005::52 *.googlecode.com                   #
    2404:6800:8005::52 chromium.googlecode.com            #
    2404:6800:8005::52 searchforchrome.googlecode.com     #
    2404:6800:8005::52 android-scripting.googlecode.com   #Android Scripting Environment
    2404:6800:8005::52 earth-api-samples.googlecode.com   #
    2404:6800:8005::52 gmaps-samples-flash.googlecode.com #
    2404:6800:8005::52 google-code-feed-gadget.googlecode.com
    2404:6800:8005::52 china-addthis.googlecode.com       #
    2404:6800:8005::52 get-flash-videos.googlecode.com    #get-flash-videos
    2404:6800:8005::52 youplayer.googlecode.com           #YouPlayer
    2404:6800:8005::52 cclive.googlecode.com              #ccLive
        
    #Labs              实验室
    2404:6800:8005::65 labs.google.com
    #2404:6800:8005::65 www3.l.google.com
    2404:6800:8005::62 www.googlelabs.com
    2404:6800:8005::62 browsersize.googlelabs.com         #Browser Size
    2404:6800:8005::62 storegadget.googlelabs.com         #Google Checkout Store Gadget
    2404:6800:8005::62 citytours.googlelabs.com           #City Tours
    2404:6800:8005::62 livingstories.googlelabs.com       #Living Stories
    2404:6800:8005::62 image-swirl.googlelabs.com         #Image Swirl
    2404:6800:8005::62 scriptconv.googlelabs.com          #Script Converter
    2404:6800:8005::62 relatedlinks.googlelabs.com        #Related Links
    2404:6800:8005::62 fastflip.googlelabs.com            #Fast Flip
    2404:6800:8005::62 listen.googlelabs.com              #Google Listen
    2404:6800:8005::62 similar-images.googlelabs.com      #Similar Images
    2404:6800:8005::62 tables.googlelabs.com              #Fusion Tables
    2404:6800:8005::62 newstimeline.googlelabs.com        #Google News Timeline
        
    #Knol              在线百科全书
    2404:6800:8005::65 knol.google.com
    #2404:6800:8005::65 www3.l.google.com
        
    #SketchUp          3D建模工具
    2404:6800:8005::62 sketchup.google.com
    #2404:6800:8005::62 sketchup.l.google.com
        
    #Pack              软件精选
    2404:6800:8005::68 pack.google.com
    #2404:6800:8005::68 www2.l.google.com
    2404:6800:8005::68 cache.pack.google.com
        
    #Blogger           博客服务
    2404:6800:8005::bf www.blogger.com
    2404:6800:8005::bf buttons.blogger.com
    2404:6800:8005::bf beta.blogger.com
    2404:6800:8005::bf draft.blogger.com                  #Blogger 测试区
    2404:6800:8005::bf status.blogger.com                 #Blogger 状态
    2404:6800:8005::bf help.blogger.com                   #支持中心
    2404:6800:8005::bf buzz.blogger.com                   #Blogger Buzz博客（英文）
    2404:6800:8005::bf photos1.blogger.com
    2404:6800:8005::bf bp0.blogger.com
    2404:6800:8005::62 blogger.google.com
    2404:6800:8005::62 blogger.l.google.com
    2404:6800:8005::62 www.blogblog.com
    2404:6800:8005::62 www1.blogblog.com
    2404:6800:8005::62 www2.blogblog.com
    2404:6800:8005::62 img.blogblog.com
    2404:6800:8005::62 img1.blogblog.com
    2404:6800:8005::62 img2.blogblog.com
    2404:6800:8005::62 img.blshe.com
        
        
    #Blogspot          博客服务
    2404:6800:8005::62 www.blogspot.com                   #主页
    #2404:6800:8005::62 blogger.l.google.com
    2404:6800:8005::62 blogsofnote.blogspot.com           #留言博客（英文版本）
    2404:6800:8005::62 knownissues.blogspot.com           #已知问题
    2404:6800:8005::62 1.bp.blogspot.com                  #
    2404:6800:8005::62 2.bp.blogspot.com                  #
    2404:6800:8005::62 3.bp.blogspot.com                  #
    2404:6800:8005::62 4.bp.blogspot.com                  #
    2404:6800:8005::62 googleblog.blogspot.com            #Official Google Blog
    2404:6800:8005::62 googlesystem.blogspot.com          #Google Operating System
    2404:6800:8005::62 googlechromereleases.blogspot.com  #Google Chrome Releases
    2404:6800:8005::62 youtube-global.blogspot.com        #YouTube Blog
    2404:6800:8005::62 igoogledeveloper.blogspot.com      #iGoogle Developer Blog
    2404:6800:8005::62 google-code-featured.blogspot.com  #Featured Projects on Google Code
    2404:6800:8005::62 googlegeodevelopers.blogspot.com   #Google Geo Developers Blog
    2404:6800:8005::62 googlecustomsearch.blogspot.com    #Google Custom Search Blog
    2404:6800:8005::62 chinafreenet.blogspot.com          #中国自由网
    2404:6800:8005::62 gregmankiw.blogspot.com            #GREG MANKIW'S BLOG
    2404:6800:8005::62 xiangeliushui.blogspot.com         #年华似水，岁月如歌
    2404:6800:8005::62 chinagfw.blogspot.com              #GFW Blog
    2404:6800:8005::62 wallpapers-arena.blogspot.com      #Wallpapers Arena
    2404:6800:8005::62 ggq.blogspot.com                   #GG圈
    2404:6800:8005::62 whiteappleer.blogspot.com          #WA＋ER
    2404:6800:8005::62 rain-reader.blogspot.com           #Nostalgia: Those Who Remain
    2404:6800:8005::62 unityteam1.blogspot.com            #生活圈 BLOG
    2404:6800:8005::62 ipv6-or-no-ipv6.blogspot.com       #IPv6 Related Stuff
    2404:6800:8005::62 autoproxy2pac.appspot.com          #
    2404:6800:8005::62 gysj.blogspot.com                  #
    2404:6800:8005::62 szncu.blogspot.com                 #
    #2404:6800:8005::62 *.blogspot.com                     #可以添加你自己的博客地址到这里
        
    #Checkout          买家
    2404:6800:8005::73 checkout.google.com
    #2404:6800:8005::73 checkout.l.google.com
        
    #Orkut             网络社区（貌似错误）
    #2404:6800:8005::62 orkut.google.com
    #2404:6800:8005::62 orkut.l.google.com
    #2404:6800:8005::62 www.orkut.com
    #2404:6800:8005::62 clients1.orkut.com
        
    #Toolbar           工具栏
    2404:6800:8005::62 toolbar.google.com
    #2404:6800:8005::62 tools.l.google.com
    2404:6800:8005::62 www.gmailnotifier.com              #Gmail Notifier
        
    #App Engine
    2404:6800:8005::64 appengine.google.com               #主页
    #2404:6800:8005::64 www3.l.google.com
    2404:6800:8005::62 appspot.l.google.com               #
    2404:6800:8005::62 chart.apis.google.com              #Google 图表 API
    2404:6800:8005::5f *.googleapis.com
    2404:6800:8005::5f translate.googleapis.com           #Google 翻译 API
    2404:6800:8005::5f ajax.googleapis.com                #Ajax API
    2404:6800:8005::8d *.appspot.com
    2404:6800:8005::8d productideas.appspot.com           #Google 汇问
    2404:6800:8005::8d wave-api.appspot.com               #Google Wave API
    2404:6800:8005::8d wave-skynet.appspot.com            #SkyNet
    2404:6800:8005::8d cactus-wave.appspot.com            #
    2404:6800:8005::8d storegadgetwizard.appspot.com      #Google Checkout Store Gadget
    2404:6800:8005::8d moderator.appspot.com              #Google Moderator
    2404:6800:8005::8d haiticrisis.appspot.com            #Google Person Finder: Haiti Earthquake
    2404:6800:8005::8d mytracks.appspot.com               #My Tracks for Android
    2404:6800:8005::8d reader2twitter.appspot.com         #Reader2Tweet
    2404:6800:8005::8d twitese.appspot.com
    2404:6800:8005::8d gfw.appspot.com
    2404:6800:8005::8d go2china9.appspot.com
    2404:6800:8005::8d mirrorrr.appspot.com
    2404:6800:8005::8d mirrornt.appspot.com
    2404:6800:8005::8d soproxy.appspot.com 
    2404:6800:8005::8d so-proxy.appspot.com
    2404:6800:8005::8d go-west.appspot.com
    2404:6800:8005::8d proxytea.appspot.com 
    2404:6800:8005::8d sivanproxy.appspot.com
    2404:6800:8005::8d proxybay.appspot.com
    2404:6800:8005::8d ipgoto.appspot.com
    2404:6800:8005::8d meme2028.appspot.com 
    2404:6800:8005::8d autoproxy2pac.appspot.com
        
    #Chrome            谷歌浏览器
    2404:6800:8005::64 chrome.google.com
        
    #Chromium OS       
    2404:6800:8005::62 goto.ext.google.com
    #2404:6800:8005::62 ghs.l.google.com
        
    #Desktop           桌面
    2404:6800:8005::62 desktop.google.com
    2404:6800:8005::62 desktop.l.google.com
        
    #Google Earth      Google地球
    2404:6800:8005::65 earth.google.com
    #2404:6800:8005::65 www3.l.google.com
        
    #Google Mars       Google火星地图
    2404:6800:8005::65 mars.google.com
    #2404:6800:8005::65 www3.l.google.com
        
    #Panoramio
    2001:4860:8010::8d www.panoramio.com
    #2001:4860:8010::8d appspot.l.google.com
    2001:4860:8010::8d static.panoramio.com
        
    #Keyhole           地理查询软件
    2404:6800:8005::62 www.keyhole.com
    2404:6800:8005::62 geo.keyhole.com
    2404:6800:8005::62 dev.keyhole.com
    2404:6800:8005::62 auth.keyhole.com
        
    #iGoogle Modules   Google小工具
    2404:6800:8005::62 gmodules.com
    2404:6800:8005::62 www.gmodules.com
    2404:6800:8005::62 www.ig.gmodules.com
    2404:6800:8005::62 ig.gmodules.com
    2404:6800:8005::62 ads.gmodules.com
    2404:6800:8005::62 p.gmodules.com
    2404:6800:8005::62 1.ig.gmodules.com
    2404:6800:8005::62 2.ig.gmodules.com
    2404:6800:8005::62 3.ig.gmodules.com
    2404:6800:8005::62 4.ig.gmodules.com
    2404:6800:8005::62 5.ig.gmodules.com
    2404:6800:8005::62 6.ig.gmodules.com
    2404:6800:8005::62 maps.gmodules.com
    2404:6800:8005::62 img0.gmodules.com
    2404:6800:8005::62 img1.gmodules.com
    2404:6800:8005::62 img2.gmodules.com
    2404:6800:8005::62 img3.gmodules.com
    2404:6800:8005::62 skins.gmodules.com
    2404:6800:8005::62 friendconnect.gmodules.com
    2404:6800:8005::62 mc8tdi0ripmbpds25eboaupdulritrp6.friendconnect.gmodules.com
    2404:6800:8005::62 r1rk9np7bpcsfoeekl0khkd2juj27q3o.friendconnect.gmodules.com
    2404:6800:8005::62 r1rk9np7bpcsfoeekl0khkd2juj27q3o.a.friendconnect.gmodules.com
        
    ##Google其他服务
    #Ajax
    2404:6800:8005::62 googleapis-ajax.google.com
    #2404:6800:8005::62 googleapis-ajax.l.google.com
        
    #YouTube
    203.208.46.29	youtube.com
    203.208.46.29	www.youtube.com
    203.208.46.29	gdata.youtube.com
    203.208.46.29	m.youtube.com
    203.208.46.29	help.youtube.com
    74.125.71.116	upload.youtube.com
    203.208.46.29	accounts.youtube.com
    203.208.46.29	insight.youtube.com
    203.208.46.29	apiblog.youtube.com
    203.208.46.29	clients1.youtube.com
    203.208.46.29	s.youtube.com
    203.208.46.29	s2.youtube.com
    203.208.46.29	s.ytimg.com
    203.208.46.29	i1.ytimg.com
    203.208.46.29	i2.ytimg.com
    203.208.46.29	i3.ytimg.com
    203.208.46.29	i4.ytimg.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache1.c.youtube.com
    203.208.46.29	dn.net
    125.56.199.9 photos-d.ak.fbcdn.net
    125.56.199.9 photos-e.ak.fbcdn.net
    125.56.199.9 photos-f.ak.fbcdn.net
    125.56.199.9 photos-g.ak.fbcdn.net
    125.56.199.9 photos-h.ak.fbcdn.neto-o.preferred.sjc07s15.v14.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache1.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache2.c.youtube.com
    203.208.46.29	dn.net
    125.56.199.9 photos-d.ak.fbcdn.net
    125.56.199.9 photos-e.ak.fbcdn.net
    125.56.199.9 photos-f.ak.fbcdn.net
    125.56.199.9 photos-g.ak.fbcdn.net
    125.56.199.9 photos-h.ak.fbcdn.neto-o.preferred.sjc07s15.v8.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache2.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache3.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache4.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache5.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache6.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v24.lscache7.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v1.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v2.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v3.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v4.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v5.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v6.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v7.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v8.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v9.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v10.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v11.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v12.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v13.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v14.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v15.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v16.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v17.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v18.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v19.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v20.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v21.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v22.lscache8.c.youtube.com
    203.208.46.29	o-o.preferred.sjc07s15.v23.lscache8.c.youtube.com
    203.208.46.29	dn.net
    125.56.199.9 photos-d.ak.fbcdn.net
    125.56.199.9 photos-e.ak.fbcdn.net
    125.56.199.9 photos-f.ak.fbcdn.net
    125.56.199.9 photos-g.ak.fbcdn.net
    125.56.199.9 photos-h.ak.fbcdn.neto-o.preferred.sjc07s15.v24.lscache8.c.youtube.com
    203.208.46.29	r1.pek01s01.c.youtube.com
    203.208.46.29	r2.pek01s01.c.youtube.com
    203.208.46.29	r3.pek01s01.c.youtube.com
    203.208.46.29	r4.pek01s01.c.youtube.com
    203.208.46.29	r5.pek01s01.c.youtube.com
    203.208.46.29	r6.pek01s01.c.youtube.com
    203.208.46.29	r7.pek01s01.c.youtube.com
    203.208.46.29	r8.pek01s01.c.youtube.com
    203.208.46.29	r9.pek01s01.c.youtube.com
    203.208.46.29	r10.pek01s01.c.youtube.com
    203.208.46.29	r11.pek01s01.c.youtube.com
    203.208.46.29	r12.pek01s01.c.youtube.com
    203.208.46.29	r13.pek01s01.c.youtube.com
    203.208.46.29	r14.pek01s01.c.youtube.com
    203.208.46.29	r15.pek01s01.c.youtube.com
    203.208.46.29	r16.pek01s01.c.youtube.com
    203.208.46.29	r17.pek01s01.c.youtube.com
    203.208.46.29	r18.pek01s01.c.youtube.com
    203.208.46.29	r19.pek01s01.c.youtube.com
    203.208.46.29	r20.pek01s01.c.youtube.com
    203.208.46.29	r21.pek01s01.c.youtube.com
    203.208.46.29	r22.pek01s01.c.youtube.com
    203.208.46.29	r23.pek01s01.c.youtube.com
    203.208.46.29	r24.pek01s01.c.youtube.com
    203.208.46.29	tc.v1.cache1.c.youtube.com
    203.208.46.29	tc.v2.cache1.c.youtube.com
    203.208.46.29	tc.v3.cache1.c.youtube.com
    203.208.46.29	tc.v4.cache1.c.youtube.com
    203.208.46.29	tc.v5.cache1.c.youtube.com
    203.208.46.29	tc.v6.cache1.c.youtube.com
    203.208.46.29	tc.v7.cache1.c.youtube.com
    203.208.46.29	tc.v8.cache1.c.youtube.com
    203.208.46.29	tc.v9.cache1.c.youtube.com
    203.208.46.29	tc.v10.cache1.c.youtube.com
    203.208.46.29	tc.v11.cache1.c.youtube.com
    203.208.46.29	tc.v12.cache1.c.youtube.com
    203.208.46.29	tc.v13.cache1.c.youtube.com
    203.208.46.29	tc.v14.cache1.c.youtube.com
    203.208.46.29	tc.v15.cache1.c.youtube.com
    203.208.46.29	tc.v16.cache1.c.youtube.com
    203.208.46.29	tc.v17.cache1.c.youtube.com
    203.208.46.29	tc.v18.cache1.c.youtube.com
    203.208.46.29	tc.v19.cache1.c.youtube.com
    203.208.46.29	tc.v20.cache1.c.youtube.com
    203.208.46.29	tc.v21.cache1.c.youtube.com
    203.208.46.29	tc.v22.cache1.c.youtube.com
    203.208.46.29	tc.v23.cache1.c.youtube.com
    203.208.46.29	tc.v24.cache1.c.youtube.com
    203.208.46.29	tc.v1.cache2.c.youtube.com
    203.208.46.29	tc.v2.cache2.c.youtube.com
    203.208.46.29	tc.v3.cache2.c.youtube.com
    203.208.46.29	tc.v4.cache2.c.youtube.com
    203.208.46.29	tc.v5.cache2.c.youtube.com
    203.208.46.29	tc.v6.cache2.c.youtube.com
    203.208.46.29	tc.v7.cache2.c.youtube.com
    203.208.46.29	tc.v8.cache2.c.youtube.com
    203.208.46.29	tc.v9.cache2.c.youtube.com
    203.208.46.29	tc.v10.cache2.c.youtube.com
    203.208.46.29	tc.v11.cache2.c.youtube.com
    203.208.46.29	tc.v12.cache2.c.youtube.com
    203.208.46.29	tc.v13.cache2.c.youtube.com
    203.208.46.29	tc.v14.cache2.c.youtube.com
    203.208.46.29	tc.v15.cache2.c.youtube.com
    203.208.46.29	tc.v16.cache2.c.youtube.com
    203.208.46.29	tc.v17.cache2.c.youtube.com
    203.208.46.29	tc.v18.cache2.c.youtube.com
    203.208.46.29	tc.v19.cache2.c.youtube.com
    203.208.46.29	tc.v20.cache2.c.youtube.com
    203.208.46.29	tc.v21.cache2.c.youtube.com
    203.208.46.29	tc.v22.cache2.c.youtube.com
    203.208.46.29	tc.v23.cache2.c.youtube.com
    203.208.46.29	tc.v24.cache2.c.youtube.com
    203.208.46.29	tc.v1.cache3.c.youtube.com
    203.208.46.29	tc.v2.cache3.c.youtube.com
    203.208.46.29	tc.v3.cache3.c.youtube.com
    203.208.46.29	tc.v4.cache3.c.youtube.com
    203.208.46.29	tc.v5.cache3.c.youtube.com
    203.208.46.29	tc.v6.cache3.c.youtube.com
    203.208.46.29	tc.v7.cache3.c.youtube.com
    203.208.46.29	tc.v8.cache3.c.youtube.com
    203.208.46.29	tc.v9.cache3.c.youtube.com
    203.208.46.29	tc.v10.cache3.c.youtube.com
    203.208.46.29	tc.v11.cache3.c.youtube.com
    203.208.46.29	tc.v12.cache3.c.youtube.com
    203.208.46.29	tc.v13.cache3.c.youtube.com
    203.208.46.29	tc.v14.cache3.c.youtube.com
    203.208.46.29	tc.v15.cache3.c.youtube.com
    203.208.46.29	tc.v16.cache3.c.youtube.com
    203.208.46.29	tc.v17.cache3.c.youtube.com
    203.208.46.29	tc.v18.cache3.c.youtube.com
    203.208.46.29	tc.v19.cache3.c.youtube.com
    203.208.46.29	tc.v20.cache3.c.youtube.com
    203.208.46.29	tc.v21.cache3.c.youtube.com
    203.208.46.29	tc.v22.cache3.c.youtube.com
    203.208.46.29	tc.v23.cache3.c.youtube.com
    203.208.46.29	tc.v24.cache3.c.youtube.com
    203.208.46.29	tc.v1.cache4.c.youtube.com
    203.208.46.29	tc.v2.cache4.c.youtube.com
    203.208.46.29	tc.v3.cache4.c.youtube.com
    203.208.46.29	tc.v4.cache4.c.youtube.com
    203.208.46.29	tc.v5.cache4.c.youtube.com
    203.208.46.29	tc.v6.cache4.c.youtube.com
    203.208.46.29	tc.v7.cache4.c.youtube.com
    203.208.46.29	tc.v8.cache4.c.youtube.com
    203.208.46.29	tc.v9.cache4.c.youtube.com
    203.208.46.29	tc.v10.cache4.c.youtube.com
    203.208.46.29	tc.v11.cache4.c.youtube.com
    203.208.46.29	tc.v12.cache4.c.youtube.com
    203.208.46.29	tc.v13.cache4.c.youtube.com
    203.208.46.29	tc.v14.cache4.c.youtube.com
    203.208.46.29	tc.v15.cache4.c.youtube.com
    203.208.46.29	tc.v16.cache4.c.youtube.com
    203.208.46.29	tc.v17.cache4.c.youtube.com
    203.208.46.29	tc.v18.cache4.c.youtube.com
    203.208.46.29	tc.v19.cache4.c.youtube.com
    203.208.46.29	tc.v20.cache4.c.youtube.com
    203.208.46.29	tc.v21.cache4.c.youtube.com
    203.208.46.29	tc.v22.cache4.c.youtube.com
    203.208.46.29	tc.v23.cache4.c.youtube.com
    203.208.46.29	tc.v24.cache4.c.youtube.com
    203.208.46.29	tc.v1.cache5.c.youtube.com
    203.208.46.29	tc.v2.cache5.c.youtube.com
    203.208.46.29	tc.v3.cache5.c.youtube.com
    203.208.46.29	tc.v4.cache5.c.youtube.com
    203.208.46.29	tc.v5.cache5.c.youtube.com
    203.208.46.29	tc.v6.cache5.c.youtube.com
    203.208.46.29	tc.v7.cache5.c.youtube.com
    203.208.46.29	tc.v8.cache5.c.youtube.com
    203.208.46.29	tc.v9.cache5.c.youtube.com
    203.208.46.29	tc.v10.cache5.c.youtube.com
    203.208.46.29	tc.v11.cache5.c.youtube.com
    203.208.46.29	tc.v12.cache5.c.youtube.com
    203.208.46.29	tc.v13.cache5.c.youtube.com
    203.208.46.29	tc.v14.cache5.c.youtube.com
    203.208.46.29	tc.v15.cache5.c.youtube.com
    203.208.46.29	tc.v16.cache5.c.youtube.com
    203.208.46.29	tc.v17.cache5.c.youtube.com
    203.208.46.29	tc.v18.cache5.c.youtube.com
    203.208.46.29	tc.v19.cache5.c.youtube.com
    203.208.46.29	tc.v20.cache5.c.youtube.com
    203.208.46.29	tc.v21.cache5.c.youtube.com
    203.208.46.29	tc.v22.cache5.c.youtube.com
    203.208.46.29	tc.v23.cache5.c.youtube.com
    203.208.46.29	tc.v24.cache5.c.youtube.com
    203.208.46.29	tc.v1.cache6.c.youtube.com
    203.208.46.29	tc.v2.cache6.c.youtube.com
    203.208.46.29	tc.v3.cache6.c.youtube.com
    203.208.46.29	tc.v4.cache6.c.youtube.com
    203.208.46.29	tc.v5.cache6.c.youtube.com
    203.208.46.29	tc.v6.cache6.c.youtube.com
    203.208.46.29	tc.v7.cache6.c.youtube.com
    203.208.46.29	tc.v8.cache6.c.youtube.com
    203.208.46.29	tc.v9.cache6.c.youtube.com
    203.208.46.29	tc.v10.cache6.c.youtube.com
    203.208.46.29	tc.v11.cache6.c.youtube.com
    203.208.46.29	tc.v12.cache6.c.youtube.com
    203.208.46.29	tc.v13.cache6.c.youtube.com
    203.208.46.29	tc.v14.cache6.c.youtube.com
    203.208.46.29	tc.v15.cache6.c.youtube.com
    203.208.46.29	tc.v16.cache6.c.youtube.com
    203.208.46.29	tc.v17.cache6.c.youtube.com
    203.208.46.29	tc.v18.cache6.c.youtube.com
    203.208.46.29	tc.v19.cache6.c.youtube.com
    203.208.46.29	tc.v20.cache6.c.youtube.com
    203.208.46.29	tc.v21.cache6.c.youtube.com
    203.208.46.29	tc.v22.cache6.c.youtube.com
    203.208.46.29	tc.v23.cache6.c.youtube.com
    203.208.46.29	tc.v24.cache6.c.youtube.com
    203.208.46.29	tc.v1.cache7.c.youtube.com
    203.208.46.29	tc.v2.cache7.c.youtube.com
    203.208.46.29	tc.v3.cache7.c.youtube.com
    203.208.46.29	tc.v4.cache7.c.youtube.com
    203.208.46.29	tc.v5.cache7.c.youtube.com
    203.208.46.29	tc.v6.cache7.c.youtube.com
    203.208.46.29	tc.v7.cache7.c.youtube.com
    203.208.46.29	tc.v8.cache7.c.youtube.com
    203.208.46.29	tc.v9.cache7.c.youtube.com
    203.208.46.29	tc.v10.cache7.c.youtube.com
    203.208.46.29	tc.v11.cache7.c.youtube.com
    203.208.46.29	tc.v12.cache7.c.youtube.com
    203.208.46.29	tc.v13.cache7.c.youtube.com
    203.208.46.29	tc.v14.cache7.c.youtube.com
    203.208.46.29	tc.v15.cache7.c.youtube.com
    203.208.46.29	tc.v16.cache7.c.youtube.com
    203.208.46.29	tc.v17.cache7.c.youtube.com
    203.208.46.29	tc.v18.cache7.c.youtube.com
    203.208.46.29	tc.v19.cache7.c.youtube.com
    203.208.46.29	tc.v20.cache7.c.youtube.com
    203.208.46.29	tc.v21.cache7.c.youtube.com
    203.208.46.29	tc.v22.cache7.c.youtube.com
    203.208.46.29	tc.v23.cache7.c.youtube.com
    203.208.46.29	tc.v24.cache7.c.youtube.com
    203.208.46.29	tc.v1.cache8.c.youtube.com
    203.208.46.29	tc.v2.cache8.c.youtube.com
    203.208.46.29	tc.v3.cache8.c.youtube.com
    203.208.46.29	tc.v4.cache8.c.youtube.com
    203.208.46.29	tc.v5.cache8.c.youtube.com
    203.208.46.29	tc.v6.cache8.c.youtube.com
    203.208.46.29	tc.v7.cache8.c.youtube.com
    203.208.46.29	tc.v8.cache8.c.youtube.com
    203.208.46.29	tc.v9.cache8.c.youtube.com
    203.208.46.29	tc.v10.cache8.c.youtube.com
    203.208.46.29	tc.v11.cache8.c.youtube.com
    203.208.46.29	tc.v12.cache8.c.youtube.com
    203.208.46.29	tc.v13.cache8.c.youtube.com
    203.208.46.29	tc.v14.cache8.c.youtube.com
    203.208.46.29	tc.v15.cache8.c.youtube.com
    203.208.46.29	tc.v16.cache8.c.youtube.com
    203.208.46.29	tc.v17.cache8.c.youtube.com
    203.208.46.29	tc.v18.cache8.c.youtube.com
    203.208.46.29	tc.v19.cache8.c.youtube.com
    203.208.46.29	tc.v20.cache8.c.youtube.com
    203.208.46.29	tc.v21.cache8.c.youtube.com
    203.208.46.29	tc.v22.cache8.c.youtube.com
    203.208.46.29	tc.v23.cache8.c.youtube.com
    203.208.46.29	tc.v24.cache8.c.youtube.com
    203.208.46.29	v1.lscache1.c.youtube.com
    203.208.46.29	v2.lscache1.c.youtube.com
    203.208.46.29	v3.lscache1.c.youtube.com
    203.208.46.29	v4.lscache1.c.youtube.com
    203.208.46.29	v5.lscache1.c.youtube.com
    203.208.46.29	v6.lscache1.c.youtube.com
    203.208.46.29	v7.lscache1.c.youtube.com
    203.208.46.29	v8.lscache1.c.youtube.com
    203.208.46.29	v9.lscache1.c.youtube.com
    203.208.46.29	v10.lscache1.c.youtube.com
    203.208.46.29	v11.lscache1.c.youtube.com
    203.208.46.29	v12.lscache1.c.youtube.com
    203.208.46.29	v13.lscache1.c.youtube.com
    203.208.46.29	v14.lscache1.c.youtube.com
    203.208.46.29	v15.lscache1.c.youtube.com
    203.208.46.29	v16.lscache1.c.youtube.com
    203.208.46.29	v17.lscache1.c.youtube.com
    203.208.46.29	v18.lscache1.c.youtube.com
    203.208.46.29	v19.lscache1.c.youtube.com
    203.208.46.29	v20.lscache1.c.youtube.com
    203.208.46.29	v21.lscache1.c.youtube.com
    203.208.46.29	v22.lscache1.c.youtube.com
    203.208.46.29	v23.lscache1.c.youtube.com
    203.208.46.29	v24.lscache1.c.youtube.com
    203.208.46.29	v1.lscache2.c.youtube.com
    203.208.46.29	v2.lscache2.c.youtube.com
    203.208.46.29	v3.lscache2.c.youtube.com
    203.208.46.29	v4.lscache2.c.youtube.com
    203.208.46.29	v5.lscache2.c.youtube.com
    203.208.46.29	v6.lscache2.c.youtube.com
    203.208.46.29	v7.lscache2.c.youtube.com
    203.208.46.29	v8.lscache2.c.youtube.com
    203.208.46.29	v9.lscache2.c.youtube.com
    203.208.46.29	v10.lscache2.c.youtube.com
    203.208.46.29	v11.lscache2.c.youtube.com
    203.208.46.29	v12.lscache2.c.youtube.com
    203.208.46.29	v13.lscache2.c.youtube.com
    203.208.46.29	v14.lscache2.c.youtube.com
    203.208.46.29	v15.lscache2.c.youtube.com
    203.208.46.29	v16.lscache2.c.youtube.com
    203.208.46.29	v17.lscache2.c.youtube.com
    203.208.46.29	v18.lscache2.c.youtube.com
    203.208.46.29	v19.lscache2.c.youtube.com
    203.208.46.29	v20.lscache2.c.youtube.com
    203.208.46.29	v21.lscache2.c.youtube.com
    203.208.46.29	v22.lscache2.c.youtube.com
    203.208.46.29	v23.lscache2.c.youtube.com
    203.208.46.29	v24.lscache2.c.youtube.com
    203.208.46.29	v1.lscache3.c.youtube.com
    203.208.46.29	v2.lscache3.c.youtube.com
    203.208.46.29	v3.lscache3.c.youtube.com
    203.208.46.29	v4.lscache3.c.youtube.com
    203.208.46.29	v5.lscache3.c.youtube.com
    203.208.46.29	v6.lscache3.c.youtube.com
    203.208.46.29	v7.lscache3.c.youtube.com
    203.208.46.29	v8.lscache3.c.youtube.com
    203.208.46.29	v9.lscache3.c.youtube.com
    203.208.46.29	v10.lscache3.c.youtube.com
    203.208.46.29	v11.lscache3.c.youtube.com
    203.208.46.29	v12.lscache3.c.youtube.com
    203.208.46.29	v13.lscache3.c.youtube.com
    203.208.46.29	v14.lscache3.c.youtube.com
    203.208.46.29	v15.lscache3.c.youtube.com
    203.208.46.29	v16.lscache3.c.youtube.com
    203.208.46.29	v17.lscache3.c.youtube.com
    203.208.46.29	v18.lscache3.c.youtube.com
    203.208.46.29	v19.lscache3.c.youtube.com
    203.208.46.29	v20.lscache3.c.youtube.com
    203.208.46.29	v21.lscache3.c.youtube.com
    203.208.46.29	v22.lscache3.c.youtube.com
    203.208.46.29	v23.lscache3.c.youtube.com
    203.208.46.29	v24.lscache3.c.youtube.com
    203.208.46.29	v1.lscache4.c.youtube.com
    203.208.46.29	v2.lscache4.c.youtube.com
    203.208.46.29	v3.lscache4.c.youtube.com
    203.208.46.29	v4.lscache4.c.youtube.com
    203.208.46.29	v5.lscache4.c.youtube.com
    203.208.46.29	v6.lscache4.c.youtube.com
    203.208.46.29	v7.lscache4.c.youtube.com
    203.208.46.29	v8.lscache4.c.youtube.com
    203.208.46.29	v9.lscache4.c.youtube.com
    203.208.46.29	v10.lscache4.c.youtube.com
    203.208.46.29	v11.lscache4.c.youtube.com
    203.208.46.29	v12.lscache4.c.youtube.com
    203.208.46.29	v13.lscache4.c.youtube.com
    203.208.46.29	v14.lscache4.c.youtube.com
    203.208.46.29	v15.lscache4.c.youtube.com
    203.208.46.29	v16.lscache4.c.youtube.com
    203.208.46.29	v17.lscache4.c.youtube.com
    203.208.46.29	v18.lscache4.c.youtube.com
    203.208.46.29	v19.lscache4.c.youtube.com
    203.208.46.29	v20.lscache4.c.youtube.com
    203.208.46.29	v21.lscache4.c.youtube.com
    203.208.46.29	v22.lscache4.c.youtube.com
    203.208.46.29	v23.lscache4.c.youtube.com
    203.208.46.29	v24.lscache4.c.youtube.com
    203.208.46.29	v1.lscache5.c.youtube.com
    203.208.46.29	v2.lscache5.c.youtube.com
    203.208.46.29	v3.lscache5.c.youtube.com
    203.208.46.29	v4.lscache5.c.youtube.com
    203.208.46.29	v5.lscache5.c.youtube.com
    203.208.46.29	v6.lscache5.c.youtube.com
    203.208.46.29	v7.lscache5.c.youtube.com
    203.208.46.29	v8.lscache5.c.youtube.com
    203.208.46.29	v9.lscache5.c.youtube.com
    203.208.46.29	v10.lscache5.c.youtube.com
    203.208.46.29	v11.lscache5.c.youtube.com
    203.208.46.29	v12.lscache5.c.youtube.com
    203.208.46.29	v13.lscache5.c.youtube.com
    203.208.46.29	v14.lscache5.c.youtube.com
    203.208.46.29	v15.lscache5.c.youtube.com
    203.208.46.29	v16.lscache5.c.youtube.com
    203.208.46.29	v17.lscache5.c.youtube.com
    203.208.46.29	v18.lscache5.c.youtube.com
    203.208.46.29	v19.lscache5.c.youtube.com
    203.208.46.29	v20.lscache5.c.youtube.com
    203.208.46.29	v21.lscache5.c.youtube.com
    203.208.46.29	v22.lscache5.c.youtube.com
    203.208.46.29	v23.lscache5.c.youtube.com
    203.208.46.29	v24.lscache5.c.youtube.com
    203.208.46.29	v1.lscache6.c.youtube.com
    203.208.46.29	v2.lscache6.c.youtube.com
    203.208.46.29	v3.lscache6.c.youtube.com
    203.208.46.29	v4.lscache6.c.youtube.com
    203.208.46.29	v5.lscache6.c.youtube.com
    203.208.46.29	v6.lscache6.c.youtube.com
    203.208.46.29	v7.lscache6.c.youtube.com
    203.208.46.29	v8.lscache6.c.youtube.com
    203.208.46.29	v9.lscache6.c.youtube.com
    203.208.46.29	v10.lscache6.c.youtube.com
    203.208.46.29	v11.lscache6.c.youtube.com
    203.208.46.29	v12.lscache6.c.youtube.com
    203.208.46.29	v13.lscache6.c.youtube.com
    203.208.46.29	v14.lscache6.c.youtube.com
    203.208.46.29	v15.lscache6.c.youtube.com
    203.208.46.29	v16.lscache6.c.youtube.com
    203.208.46.29	v17.lscache6.c.youtube.com
    203.208.46.29	v18.lscache6.c.youtube.com
    203.208.46.29	v19.lscache6.c.youtube.com
    203.208.46.29	v20.lscache6.c.youtube.com
    203.208.46.29	v21.lscache6.c.youtube.com
    203.208.46.29	v22.lscache6.c.youtube.com
    203.208.46.29	v23.lscache6.c.youtube.com
    203.208.46.29	v24.lscache6.c.youtube.com
    203.208.46.29	v1.lscache7.c.youtube.com
    203.208.46.29	v2.lscache7.c.youtube.com
    203.208.46.29	v3.lscache7.c.youtube.com
    203.208.46.29	v4.lscache7.c.youtube.com
    203.208.46.29	v5.lscache7.c.youtube.com
    203.208.46.29	v6.lscache7.c.youtube.com
    203.208.46.29	v7.lscache7.c.youtube.com
    203.208.46.29	v8.lscache7.c.youtube.com
    203.208.46.29	v9.lscache7.c.youtube.com
    203.208.46.29	v10.lscache7.c.youtube.com
    203.208.46.29	v11.lscache7.c.youtube.com
    203.208.46.29	v12.lscache7.c.youtube.com
    203.208.46.29	v13.lscache7.c.youtube.com
    203.208.46.29	v14.lscache7.c.youtube.com
    203.208.46.29	v15.lscache7.c.youtube.com
    203.208.46.29	v16.lscache7.c.youtube.com
    203.208.46.29	v17.lscache7.c.youtube.com
    203.208.46.29	v18.lscache7.c.youtube.com
    203.208.46.29	v19.lscache7.c.youtube.com
    203.208.46.29	v20.lscache7.c.youtube.com
    203.208.46.29	v21.lscache7.c.youtube.com
    203.208.46.29	v22.lscache7.c.youtube.com
    203.208.46.29	v23.lscache7.c.youtube.com
    203.208.46.29	v24.lscache7.c.youtube.com
    203.208.46.29	v1.lscache8.c.youtube.com
    203.208.46.29	v2.lscache8.c.youtube.com
    203.208.46.29	v3.lscache8.c.youtube.com
    203.208.46.29	v4.lscache8.c.youtube.com
    203.208.46.29	v5.lscache8.c.youtube.com
    203.208.46.29	v6.lscache8.c.youtube.com
    203.208.46.29	v7.lscache8.c.youtube.com
    203.208.46.29	v8.lscache8.c.youtube.com
    203.208.46.29	v9.lscache8.c.youtube.com
    203.208.46.29	v10.lscache8.c.youtube.com
    203.208.46.29	v11.lscache8.c.youtube.com
    203.208.46.29	v12.lscache8.c.youtube.com
    203.208.46.29	v13.lscache8.c.youtube.com
    203.208.46.29	v14.lscache8.c.youtube.com
    203.208.46.29	v15.lscache8.c.youtube.com
    203.208.46.29	v16.lscache8.c.youtube.com
    203.208.46.29	v17.lscache8.c.youtube.com
    203.208.46.29	v18.lscache8.c.youtube.com
    203.208.46.29	v19.lscache8.c.youtube.com
    203.208.46.29	v20.lscache8.c.youtube.com
    203.208.46.29	v21.lscache8.c.youtube.com
    203.208.46.29	v22.lscache8.c.youtube.com
    203.208.46.29	v23.lscache8.c.youtube.com
    203.208.46.29	v24.lscache8.c.youtube.com 
    #Twitter 
        
    199.59.148.84 oauth.twitter.com
    199.59.148.84 twitter.com
    199.59.148.84 www.twitter.com
    199.59.148.84 api.twitter.com
    199.59.148.201 search.twitter.com
    199.59.148.139 userstream.twitter.com
    199.59.148.84 ssl.twitter.com
    199.59.148.84 status.twitter.com
    199.59.148.84 assets0.twitter.com
    199.59.148.84 assets1.twitter.com
    199.59.148.84 assets2.twitter.com
    199.59.148.84 assets3.twitter.com
    199.59.148.84 static.twitter.com
    184.29.36.124 platform.twitter.com
    219.76.10.138 platform0.twitter.com
    199.59.148.206 help.twitter.com
    199.59.148.206 support.twitter.com
    209.84.4.102 si0.twimg.com
    209.84.4.102 si1.twimg.com
    209.84.4.102 si2.twimg.com
    209.84.4.102 si3.twimg.com
    209.84.4.102 si4.twimg.com
    209.84.4.102 si5.twimg.com
        
    #Facebook 脸谱网（尚未完全部署）
    69.63.189.16 facebook.com
    69.63.189.16 www.facebook.com
    69.63.181.31 m.facebook.com
    69.63.181.20 login.facebook.com
    69.63.179.70 secure.facebook.com
    66.220.146.18 apps.facebook.com
    69.63.181.31 touch.facebook.com
    118.214.114.110 s-static.ak.facebook.com
    66.220.147.47 api.facebook.com
    69.63.181.16 zh-CN.facebook.com
    202.157.186.28	static.ak.facebook.com
    202.157.186.34 b.static.ak.facebook.com
    69.63.178.57 secure-profile.facebook.com
    69.63.178.57 secure-media-sf2p.facebook.com
    69.63.178.15 ssl.facebook.com
    69.63.190.18 apps.facebook.com
    118.214.190.105 profile.ak.facebook.com
        
    #Facebook web
    69.63.187.17 fbcdn.net
    97.65.135.139 external.ak.fbcdn.net
    124.155.222.50 vthumb.ak.fbcdn.net
    97.65.135.163 static.ak.fbcdn.net
    97.65.135.163 b.static.ak.fbcdn.net
    202.157.186.34 creative.ak.fbcdn.net
    118.214.190.128 profile.ak.fbcdn.net
    69.63.176.21 s-hprofile-sf2p.fbcdn.net
    125.56.199.9 photos-a.ak.fbcdn.net
    125.56.199.9 photos-b.ak.fbcdn.net
    125.56.199.9 photos-c.ak.fbcdn.net
    125.56.199.9 photos-d.ak.fbcdn.net
    125.56.199.9 photos-e.ak.fbcdn.net
    125.56.199.9 photos-f.ak.fbcdn.net
    125.56.199.9 photos-g.ak.fbcdn.net
    125.56.199.9 photos-h.ak.fbcdn.net

