Title: 通过Flutter hooks简化代码
Slug: note-on-flutter-hooks
Tags: Flutter
Date: 2021-03-21

看了Resocoder和Robert Brunhage的两个视频, 这篇总结一下其中的内容(我其实还没实践过).

本文主要参考自:
- [pub package](https://pub.dev/packages/flutter_hooks)
- [Video by Robert Brunhage](https://www.youtube.com/watch?v=A1DUBgIsCv8)
- [Tutorial by Resocoder](https://resocoder.com/2020/01/21/flutter-hooks-hide-fab-animation-100-widget-code-reuse/)

## The problem

Flutter hooks想解决的问题是`StatefulWidget`的一些常见pattern太复杂, 减少了代码的可读性("readability").

一个典型例子就是animation controller:

```dart
class MyPage extends StatefulWidget{
  @override
  _MyPageState createState() => _MyPageState();
}

class _MyPageState extends State<MyPage>
    with SingleTickerProviderStateMixin {
  AnimationController _animController;

  @override
  void initState() {
    super.initState();
    _animController = AnimationController(
      vsync: this,
      duration: kThemeAnimationDuration,
      value: 1, // initially visible
    );
  }

  @override
  Widget build(BuildContext context) {
    // use _animController here
  }

  @override
  void dispose() { 
    _animController.dispose();
    super.dispose();
  }
}
```

这种pattern在vanilla flutter里经常被使用, 但是对同一个controller在好几个地方操作(`initiState()`/`setState()`/`dispose()`), 真的不好读.

Flutter hooks就可以把这种重复的pattern抽离出来, 把`StatefulWidget`变成类似`StatelessWidget`的`HookWidget`, 简化代码, 大大提高可读性.

(btw 这个包的作者是Rémi Rousselet大神, 质量有保障👌)

## 使用现成的Hooks

对于常用的pattern有现成的hooks可以直接套用. 比如上面的animation controller例子, 用flutter hooks可以写成这样:

```dart
class MyPage extends HookWidget {  //! StatelessWidget => HookWidget
  @override
  Widget build(BuildContext context) {
    final animController = useAnimationController(
        duration: kThemeAnimationDuration, 
        initialValue: 1,
    );
    // use _animController here
  }
}
```

⚡️Flutter hooks自带了不少[现成的hooks](https://pub.dev/packages/flutter_hooks#existing-hooks), 有的面向Animation, 有的面向Stream等等, 有时间可以好好看一看...

## 自定义Hook

cf. Resocoder的[教程](https://resocoder.com/2020/01/21/flutter-hooks-hide-fab-animation-100-widget-code-reuse/#t-1616317538465)

如果现成的hook不满足条件, 其实自己实现起来也非常容易, 基本就是把原来`StatefulWidget/State<Foo>`的内容变成`Hook<R>/HookState<R,Foo>`. 其中`Foo`是我们自定义的类名, `R`则是state的类型. 比如对于之前的例子: `Foo`=`MyPage`, `R`=`AnimationController`.

这里列一下二者的区别, 基本是一一对应的, 所以迁移起来不难:

| `StatefulWidget`                   | `Hook<R>`                       |
| ---------------------------------- | ------------------------------- |
| `class Foo extends StatefulWidget` | `class Foo extends Hook<R>`     |
| `createState() => State<Foo>`      | `createState() => HookState<R>` |

| `State<Foo>`              | `HookState<R, Foo>`      |
| ------------------------- | ------------------------ |
| `R _data;`                | `R _data;`               |
| `initState() {_data=...}` | `initHook() {_data=...}` |
| `build(ctx) => Widget`    | `build(ctx) => R`        |
| `dispose()`               | `dispose()`              |
| `widget.xxx`              | `hook.xxx`               |

当自定义的`Hook/HookState`写好以后, 根据Flutter hooks的惯例, 需要写一个`useXxHooks`的函数, 返回类型是`R`:

```dart
R useMyHooks(...) {
  return Hook.use(_FooHook());
}
```

## useState/useEffect

cf. Robert Brunhage的[视频](https://www.youtube.com/watch?v=A1DUBgIsCv8)

对于**不追求逻辑复用**, 只想去掉`initState()`/`dispose()`的场景, 可以考虑直接把一个`StatefulWidget`变成`HookWiget`. Flutter hooks提供了`useState`和`useEffect`, 让我们可以直接在`HookWiget.build()`函数里面创建/修改状态.

**创建状态**: 用[`useState(R initialVal)`](https://pub.dev/documentation/flutter_hooks/latest/flutter_hooks/useState.html).\
注意返回值的是一个`ValueNotifier<R>` (cf. [[202102212026 ChangeNotifier, ValueNotifier and StateNotifier|各种notifier]]), 获得包含的值需要`.value`.

**修改状态**: [`useEffect()`](https://pub.dev/documentation/flutter_hooks/latest/flutter_hooks/useEffect.html), 有两个参数:

- 第一个参数(`effect()`)是一个函数`Dispose? Function()`
    - 可以把修改状态的内容(比如原先`setState`的内容)放在这里
    - `effect`可以返回另一个函数(`Dispose?`), 这个函数会_在`effect()`下次一被调用或者当widget dispose的时候运行_.
- 第二个可选参数`keys`是一个list, 控制`effect()`何时被调用:
    - 如果为null(默认), 则_每次`build()`_ 都会调用`effect()`
    - 如果非null, 则只在_第一次`build()`, 以及当任何keys元素改变时_才调用`effect()`\
       **注意: `keys`可以是空list, 但非null**, 比如`keys=[]`, 此时effect只运行一次.

这种方法可以把一个`StatefulWidget`简化为类似`StatelessWidget`的`HookWidget`, 简化代码. 例如用useState/useEffect写一个简单计时器, 代码相比vanilla flutter要简洁许多:

```dart
class MyTimerPage extends HookWidget {
  @override
  Widget build(BuildContext context) {
    final _numberNotifier = useState(0);  //! Create state

    useEffect(  //! Change state
      /*effect=*/() {
        //! ~= initState()
        final timer = Timer.periodic(
          Duration(seconds: 1), 
          //! ~= setState()
          (time) => _numberNotifier.value = time.tick,
        );
        return timer.cancel;  //! ~= dispose()
      }, 
      /*keys=*/const [],  //! => effect() is called only once
    );

    return Scaffold(
      body: Center(
        child: Text(_numberNotifier.value.toString()),
      ),
    );
  }
}
```

当然这样写的缺点就是逻辑无法复用, 要复用逻辑的话可以参考上一节"自定义Hook":

1. 把useState/useEffect的内容放进一个`_MyTimerHook extends Hook<int>`

2. 定义`int useMyTimer()`函数:

    ```dart
    int useMyTimer() {
      return Hook.use(_MyTimerHook());
    }
    ```

3. 在`HookWidget`里使用`useMyTimerHook`:

    ```dart
    class MyTimerPage extends HookWidget {
      @override
      Widget build(BuildContext context) {
        final number = useMyTimer();
        return Text(number.toString());
      }
    }
    ```

## 最佳实践

pub上列出了几条[最佳实践](https://pub.dev/packages/flutter_hooks#rules):

**所有hook的函数都以'use'开头:**

```dart
Widget build(BuildContext context) {
  // starts with `use`, good name
  useMyHook();
  // doesn't start with `use`, could confuse people into thinking that this isn't a hook
  myHook();
  // ....
}
```

**不要在分支条件里使用hook:**

```dart
Widget build(BuildContext context) {
  useMyHook();  //! Good: DO call hooks unconditionally
  // ....
}

Widget build(BuildContext context) {
  if (condition) {
    useMyHook();  //! BAD: DON'T wrap use into a condition
  }
  // ....
}
```
