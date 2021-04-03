Title: Flutter状态管理 - 三种Notifier的比较
Slug: flutter-notifiers-compare
Tags: Flutter
Date: 2021-04-03

Flutter(或者更宽泛的app开发)可以一句话总结为:

> **`UI = f(state)`**

即app的当前界面(UI)反映了当前程序状态(state). Flutter的状态管理就是app根据**当前app的state**的显示和更新UI.

我们假设state是一个类型为`T`的object, 在下文的购物车例子中, state是当前购物车的内容(类型`T`=`List<Item>`).

关于如何在widget tree里获取state, 可以有provider/riverpod等选项, e.g.`Provider<T>`. 但是如果直接用`T`作为状态会有问题: 就是当state的值被修改以后, **对应的UI并不会自动rebuild**(除非其他逻辑如`setState`触发了rebuild).

如果希望在state修改以后, UI自动触发监听它的UI更新, 则需要**用各种Notifier来包裹state**. 例如我们不用`T`作为state, 而是用`ValueNotifier<T>`.

这里主要介绍和比较三种常用的Notifier: `ChangeNotifier`, `ValueNotifier` 和 `StateNotifier`. 
本文参考了[Resocoder](https://resocoder.com/2020/12/11/flutter-statenotifier-riverpod-tutorial-immutable-state-management/), [Andrea Bizzotto](https://codewithandrea.com/videos/flutter-state-management-setstate-freezed-state-notifier-provider/)以及[FunWithFlutter](https://blog.funwith.app/posts/provider-with-statenotifier)的tutorial.

## ChangeNotifier

`ChangeNotifier`是Flutter SDK自带的class: 一个`ChangeNotifier`可以被widgets监听(listen), state改变后, 如果要**让所有监听它的widget重新build**, 需要手动调用`notifyListeners()`函数.

cf. [Flutter官方的state management文档](https://flutter.dev/docs/development/data-and-backend/state-mgmt/simple#changenotifier).

比如文档里的例子, 我们的state是当前购物车的内容, 于是我们定义`CartModel`类(继承`ChangeNotifier`)作为state:

```dart
class CartModel extends ChangeNotifier {
  final List<Item> _items = []; // 购物车内容, 设为private
  // 只读的购物车内容(getter)
  UnmodifiableListView<Item> get items => UnmodifiableListView(_items);

  int get totalPrice => _items.length * 42; // 当前购物车总价的getter(假设每件都是42块)

  /// 加入物品到购物车
  void add(Item item) {
    _items.add(item);
    notifyListeners(); // <==***This call tells the widgets that are listening to this model to rebuild.
  }

  /// 清空购物车
  void removeAll() {
    _items.clear();
    notifyListeners(); // <==***This call tells the widgets that are listening to this model to rebuild.
  }
}
```

ChangeNotifier结合Provider[(`ChangeNotifierProvider`](https://pub.dev/documentation/provider/latest/provider/ChangeNotifierProvider-class.html)), 就是一个比较基础的state management解决方案.

## ValueNotifier

`ChangeNotifier`有个问题是每次都要手动调用`notifyListeners()`才能让监听的widget更新.

如果想每当数据发生变化的时候, 都自动通知监听的widget -- 这就可以用`ValueNotifier<T>`.

`ValueNotifier`是`ChangeNotifier`的子类. 它把数据保存到`T value`里, **每当`value`发生变化的时候, 监听的widget都重新build**, 省去了`notifyListeners()`这一步.

还是上面的例子, 改为用ValueNotifier就是:

```diff
-class CartModel extends ChangeNotifier {
+class CartModel extends ValueNotifier<List<Item>> {
- final List<Item> _items = []; // 不用声明_items以及items getter了 -- ValueNotifier自动把数据保存在`value`

+ CartModel(): super(<Item>[]); // 构造函数要提供value的初始值
  
- int get totalPrice => _items.length * 42;
+ int get totalPrice => value.length * 42;

  void add(Item item) {
+   value.add(item);
-   _items.add(item);
-   notifyListeners(); // 不必call notifyListeners()
  }

  void removeAll() {
+   value.clear(item);
-   _items.clear();
-   notifyListeners();
  }
}
```

对于provider, ValueNotifier也有对应的[ValueListenableProvider](https://pub.dev/documentation/provider/latest/provider/ValueListenableProvider-class.html)供使用.
如果不用provider/riverpod, Flutter SDK里也有[ValueListenableBuilder](https://api.flutter.dev/flutter/widgets/ValueListenableBuilder-class.html)可以在`value`更改时自动rebuild -- 类似provider的`Consumer`.

## StateNotifier

`StateNotifier`不是Flutter SDK自带, 需要使用[`state_notifier`](https://pub.dev/packages/state_notifier)或者[`flutter_riverpod`](https://pub.dev/packages/flutter_riverpod)包. 也有对应的`StateNotifierProvider`(来自flutter_state_notifier包), 用法和`ValueListenableProvider`类似.

Flutter的`ValueNotifier`主要有以下问题:

1. `ValueNotifier`属于Flutter而不是纯dart, 不能用于写非flutter的库;
2. `value`是public成员 -- 也就是说**任何人都可以在外部修改`ValueNotifier.value`**, 听上去很不安全

`StateNotifier`就解决了这两个问题:

1. 它不依赖flutter, 可用于纯dart的开发;
2. 在`StateNotifier`类之外修改`state`的时候, 会**有linting提示**.

`StateNotifier`用法和`ValueNotifier`几乎一样, 只不过`value`变成了`state`, 迁移起来应该很容易:

```diff
-class CartModel extends ValueNotifier<List<Item>> {
+class CartModel extends StateNotifier<List<Item>> {
  CartModel(): super(<Item>[]); // 构造函数要提供state的初始值

- int get totalPrice => value.length * 42;
+ int get totalPrice => state.length * 42;

  void add(Item item) {
+   state.add(item);
-   value.add(item);
  }

  void removeAll() {
+   state.clear();
-   value.clear();
  }
}
```


## 总结

**TLDR: `StateNotifier`是坠好的.**

|                          | `ChangeNotifier`           | `ValueNotifier<T>`              | `StateNotifier<T>`            |
| ------------------------ | -------------------------- | ------------------------------- | ----------------------------- |
|                          | Flutter SDK                | Flutter SDK                     | state_notifier package        |
| 获取state                | 手写getter                 | `.value`                        | `.state`                      |
| 修改state                | 手写setter或者其他function | `value`是public, 任何人都可修改 | 在外部修改`state`会有lint提示 |
| 状态变化时触发监听UI更新 | 手动`notifyListeners()`    | 自动                            | 自动                          |

另外`StateNotifier`推荐结合[freezed package](https://pub.dev/packages/freezed)使用, 以后有时间再总结一下freezed的用法以及它好在哪里.