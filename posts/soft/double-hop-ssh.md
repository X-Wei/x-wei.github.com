Title: 两层ssh连接(2-hop ssh connection)代理配置
Date: 2016-07-26
Slug: double-hop-ssh
Tags: ssh
Author: syf



问题: 
现在本地ssh连接eth的cscs服务器, 连接需要进行两次ssh: 第一次本地连接到ela服务器, 第二次从ela再次ssh到cscs. 现在配置本地的ssh代理使之可以一次完成. 

第一步: 生成sshkey
=============

	ssh-keygen
	cat ~/.ssh/id_rsa.pub | ssh your_username@ela.cscs.ch 'cat >> ~/.ssh/authorized_keys'
	ssh your_username@ela.cscs.ch


第二步: 修改.ssh/config文件内容
======================
用文本编辑器打开``.ssh/config``文件, 添加如下内容: 

	Host daint
	    Hostname daint101
	    User your_username
	    ForwardAgent yes
	    ForwardX11 yes
	    Port 22
	    IdentityFile ~/.ssh/id_rsa
	    ProxyCommand ssh -q -Y your_username@ela.cscs.ch netcat %h %p -w 10
 

直连第二层ssh
========
进行了以上配置以后, 连接到cscs就不再需要两层ssh的命令了, 直接:  

``$ssh daint  ``

即可 !

用rsync同步远程文件夹
=============

例子: 把本地文件夹同步到第二层ssh的目录下.

``rsync -a --progress ~/Downloads/nn_coref-master daint:/scratch/daint/your_username/code``
