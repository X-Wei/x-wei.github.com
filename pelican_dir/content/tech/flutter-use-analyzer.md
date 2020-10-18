Title: 用analyzer提高Flutter项目的代码质量
Slug: flutter-use-analyzer
Tags: Flutter
Date: 2020-10-18

Dart默认的linter配置有点弱, 有很多有问题代码也不报错或警告.
添加一个analyzer可以应用dart的最佳代码实践, 对一些不好的代码风格提出警告或者直接报错, 从而提高代码质量.

Cf. resocoder的介绍[文章](https://resocoder.com/2020/01/17/dart-linting-tutorial-healthy-flutter-codebase-with-analysis_options-yaml/) (和视频)

Use an analyzer
--------------
Resocoder推荐[lint](https://pub.dev/packages/lint), 里面提供了一些最佳的dart和flutter代码风格. 类似的选择还有pandentic和effective_dart.

使用方式就是, 先在pubsepc.yaml里添加依赖:

```yaml
# pubspec.yaml
dependency_overrides:
  lint: ^1.3.0
```

然后在根目录新建一个analysis_options.yaml文件:

```yaml
# analysis_options.yaml
include: package:lint/analysis_options.yaml
```

### Exclude folders / disable rules

analyzer默认会扫描文件夹下所有的dart代码, 有时候一些自动生成的代码或者在``build/``文件夹下的代码并不需要被分析, 可以用``exclude``把它们排除在外.

另外有些默认的规则可能不适用于自己的代码, 比如我就比较喜欢加``this``, 认为这样更容易区分成员变量和普通变量, 而这个是[不被推荐](https://dart-lang.github.io/linter/lints/unnecessary_this.html)的(毕竟dart的IDE整合的非常棒). 如果要关闭这一项检查, 只需要在linter rule里把它设为false.

综上, 我的analysis_options.yaml长这样:

```yaml
include: package:lint/analysis_options.yaml

analyzer:
  exclude:
    - build/**

linter:
  rules:
    # Rationale: in our app, the codes are for reading on mobile phones. Adding
    # `this` makes it easier for readers to understand which variables class
    # members and which ones are not.
    unnecessary_this: false
```


Auto-fix suggestions
--------------------
不过在加了analyzer以后我发现VSCode出现了几百个warning, 大部分warning都有简单的fix方法(比如给``Text("foo")``加个``const``之类的). 虽然只要点一下就能fix, 点几百下也实在是太麻烦了...

搜索一下以后发现了解决办法: <https://stackoverflow.com/a/62664168> 

首先用`dartfmt`可以解决一些简单的格式问题:

	# simple style/format fixes
	$ dartfmt --fix --overwrite --follow-links .

要应用analyzer的fix, 需要使用[dartfix](https://pub.dev/packages/dartfix). 不过它目前只支持pedantic, 不能直接用analysis_options.yaml的配置:

	# install dartfix:
	$ pub global activate dartfix
	# Use dartfix to auto-apply pedantic suggestions:
	$ dartfix --pedantic --excludeFix unnecessary_this lib/ --fix prefer_const_declarations --overwrite

但我发现pedantic的检查确实不如lint严格(cf. [二者的比较](https://github.com/passsy/dart-lint#comparison-to-packagepedantic)), 所以我并没有直接用`--pedantic`.

但是, 我们依然可以用dartfix来fix某一类问题(需要先确认某个fix是否被dartfix支持). 比如我看到很多``sort_child_properties_last``的建议, 于是可以:

	# Check if the "sort_child_properties_last" lint is supported by dartfix:
	$ dartfix -h | grep sort_
	• sort_child_properties_last
	# This fix is available ==> Apply it with dartfix:
	$ dartfix --fix sort_child_properties_last  lib/ --overwrite

用类似的方式, 就可以快速应用linter的建议:

	$ dartfix --fix prefer_const_constructors  lib/ --overwrite
	$ dartfix --fix prefer_const_declarations  lib/ --overwrite
	$ dartfix --fix prefer_final_locals  lib/ --overwrite
	
	# Or apply multiple fixes at once:
	$ dartfix --fix prefer_const_declarations,avoid_redundant_argument_values,prefer_collection_literals,curly_braces_in_flow_control_structures,prefer_if_elements_to_conditional_expressions,annotate_overrides,prefer_const_constructors_in_immutables,unnecessary_const,prefer_is_empty,prefer_final_fields \
	    lib/ --overwrite