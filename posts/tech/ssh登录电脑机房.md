Title: ssh远程登录学校机房电脑
Date: 2013-07-02
Tags: shell
Slug: ssh远程登录学校机房电脑


X[机房的电脑](http://www.enseignement.polytechnique.fr/profs/informatique/Philippe.Chassignet/MOYENS/stations.html)配置还是很高的, 所以...

远程登录的命令是: 
    ssh -X xing.wei@truite.polytechnique.fr

(-X命令表示允许使用X程序.)

登录进去以后, 可以在终端里输入命令, 比如查看系统板本: 

    $  lsb_release -a
    LSB Version:	:core-4.0-ia32:core-4.0-noarch:graphics-4.0-ia32:graphics-4.0-noarch:printing-4.0-ia32:printing-4.0-noarch
    Distributor ID:	n/a
    Description:	CentOS
    Release:	n/a
    Codename:	n/a

机房是centOS, 高效稳定. 

然后可以在终端输入命令来启动程序, 比如``eclipse &, ``就会在你这边的电脑显示出来eclipse的窗口 (加"&"是可以使多个程序同时启动).

几个常用的程序: 

    eclipse &
    scilab & 
    firefox &

可惜不知道咋能显示远程的桌面, 不过这也差不多够了, 以后用eclipse或者scilab这类比较"大"的程序, 直接用机房的工作站做好了...
