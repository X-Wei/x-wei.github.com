Title: 用fvm管理多个Flutter SDK
Slug: flutter-use-fvm
Tags: Flutter
Date: 2020-10-16

background
----------

flutter有很多channel: stable/beta/dev/master, 而目前有些功能只在某个channel上可用, 比如Linux support目前只在dev channel支持.

我日常用的是beta channel, 但是想写Linux程序时每次``flutter channel dev``的话 需要花费很多时间--因为要下载新channel的内容, switch回去的时候又要等半天(因为要从新下载).

今天看到Flutter Explained的视频: <https://youtu.be/R6vKde1vIGQ> 这正是解决这个问题的! 它可以cache不同版本的flutterSDK 然后每个repo可以设置不同的版本号, 而且VSCode也只需要简单配置.

enable fvm
----------

一行命令即可开启fvm:
``$ pub global activate fvm``

常用法:

* ``fvm flutter``: Proxies flutter commands 用于选择合适的flutter版本
	* 也就是说用``fvm flutter``来代替flutter命令 — 会自动pick当前repo所用的SDK
	* 比如: ``fvm flutter doctor``
* ``fvm list``: 查看目前安装的flutter 版本
* ``fvm use``: 选择使用一个SDK版本
* ``fvm install dev/beta/stable/...``: 安装SDK 


use fvm
-------

在flutter文件夹里运行``fvm use xxx``即可
	$ cd my_flutter_proj
	$ fvm use dev
	$ fvm list
	Versions path:  /home/xwei/fvm/versions
	beta
	dev ✔
	
这个会在当前目录下添加一个``.fvm``的文件夹, 里面包含了到指定SDK的软链接 以及一个json config:

	$ ls .fvm
	flutter_sdk@  fvm_config.json

接下来就可以愉快的用flutter dev开发linux app了:
	$ fvm flutter config --enable-linux-desktop
	$ fvm flutter devices
	2 connected devices:
	Android SDK built for x86 (mobile) • emulator-5554 • android-x86 • Android 10 (API 29) (emulator)
	Linux (desktop)                    • linux         • linux-x64   • Linux
	$ fvm flutter create .
	$ fvm flutter run -d linux

VScode config
-------------

cf. <https://github.com/leoafarias/fvm#vscode>
让vscode使用fvm flutter (而不是默认flutter), 只要修改settings.json把那个flutter_sdk的软链接即可:

	$ cat .vscode/settings.json 
	{
	  "dart.flutterSdkPaths": [".fvm/flutter_sdk"]
	}

然后在VSCode的command palette里输入``Flutter: Change SDK``, 就可以选择flutter SDK了

other config
------------

### change cache path
fvm默认cache在``~/fvm``文件夹下, 可以修改``FVM_HOME``环境变量改到别的位置.
cf. <https://github.com/leoafarias/fvm#change-fvm-cache-directory>

### bash/fish alias
每次都写`fvm flutter`有点麻烦 可以在bashrc/config.fish里加上一行 ``alias ff=fvm flutter``

综上, 只需要在.bashrc里加上:
	alias ff='fvm flutter'
	export FVM_HOME="$HOME/.local/fvm"

我一般用fish, 是在``config.fish``里加上:
	alias ff='fvm flutter'
	set FVM_HOME "$HOME/.local/fvm"

