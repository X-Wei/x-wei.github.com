Title: ADT环境搭建
date: 2013-11-08
Slug: ADT环境搭建
Tags: android, inf422
 
[TOC] 



这学期INF422, 第一节课就是android安装调试环境的搭建(居然要一节课?), 这里总结一下.

### 第一步: 下载bundle
下载[ADT-Bundle](http://developer.android.com/sdk/index.html)
解压缩以后啥都有了, 包含一个eclipse...

### 第二步: 修改环境变量
linux下的环境变量放在``.bashrc文件``, 加入下面一行: 

``PATH=$PATH:<dir>/sdk/tools/:<dir>/sdk/platform-tools/:``

其中`<dir>`是放置SDK的目录地址.

测试一下好不好使, 在终端中输入`android`, 看是否会弹出SDK manager

### 第三步: 新建一个virtual machine
可以用eclipse的AVDmanager做, 也可以用命令行做. 

输入:

``android list targets``

找到想要的target(我们要4.1.2)的那个id(一个数字), 然后, 运行命令: 

 ``android create avd -t <target_id> -n inf422 --abi armeabi-v7a``

这样就生成了一个名叫"inf422"的虚拟机

### 第四步: 关联到自定义的镜像
inf422这门课提供了一个修改过的android镜像, 在[这里](http://www.enseignement.polytechnique.fr/informatique/INF422/ramdisk.img)和[这里](http://www.enseignement.polytechnique.fr/informatique/INF422/kernel-qemu)下载, 下载到本地的目录上了以后, 运行: 
 
``emulator @inf422 -ramdisk <IMAGES>/ramdisk.img -kernel <IMAGES>/kernel-qemu``

其中<IMAGES>是刚刚存放那俩镜像文件的目录. 

### 第五步: telnet连接虚拟机
课程里用的emulator使用telnet服务器, 且是在虚拟机的23端口接收信息. 先重定向一下端口, 定向到localhost的4444端口:

``adb forward tcp:4444 tcp:23``

这样, 以后要登录模拟器emulator的时候, 只需要输入: 

``telnet localhost 4444``

(用户名是root, 不要密码)

第六步: 用两种方法进入虚拟机
---------------
刚才的4444端口是进入emulator用的, 而打开虚拟机的时候, 窗口标题是一个数字再加虚拟机的名字(我的显示的是"5554:inf422"), 这个5554是另外一个端口, 用于用shell方式登陆, 登陆后可以使用shell命令查看文件或者进行一些操作. 

而与之对应, 从4444端口登陆, 则是进入emulator的控制console

*两种方法和AVD交流:*

1. console: linux命令, 命令行
2. emulator: 发送命令产生一些事件(电话, 短信, GPS等)


第二种方式可以模拟一些手机事件, 很有用... 使用help命令查看emulator怎么使用



