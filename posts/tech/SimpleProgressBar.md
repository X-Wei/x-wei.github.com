Title: 一个简单的python进度条
Date: 2014-08-14
Tags: python
Slug: 一个简单的python进度条

在处理大量数的时候, 如果输出类似 "process i out of n files..." 这样的内容来只是进度的话, 虽然可以显示目前的进度(用来安慰等待的心情...)但有个问题是, 如果输出了太多行(比如一万行...), 就看不到前面的内容了... 

所以想找一个命令行下面的进度条, 其实python已经有了(不止一个)进度条的包了, 比如[progressbar](https://pypi.python.org/pypi/progressbar/2.3-dev), 但是不知为什么这个包在windows下面没有能做到刷新显示 -- 就是刷新进度的时候, 没有把原先那一行去掉, 而是在下面再输出了一行... (不过后来在linux下面使用这个包是没问题的, 好奇怪...)

所以想办法自己写了一个, 发现要实现一个简单的进度条还是很简单的, 关键就是使用`\r`, 这样会把光标移动到当前行的开头: 这样下次输出的时候就会把原先的内容冲掉了. 

代码只有不到二十行: 

```python
import sys, time

class SimpleProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width
 
    def update(self, x):
        '`x`: progress in percent (0~100)'
        assert 0 <= x <= 100
        if int(self.width * (x / 100.0)) == int(x): # not necessary to update display
            return
        self.pointer = int(self.width * (x / 100.0))
        pg = '%d%% [%s]' % (int(x), '#' * self.pointer + '-' * (self.width - self.pointer))
        sys.stdout.write(pg)
        sys.stdout.flush()
        sys.stdout.write('\r')
        if x == 100:  # if finished, print a new line
            sys.stdout.write('\n')
```

用法也很简单, 先新建一个SimpleProgressBar对象, 在要更新进度条的时候, 调用update方法即可...

```python
# An example of usage...
pb = SimpleProgressBar()
for i in range(301):
    pb.update(i*100.0/300)
    time.sleep(0.1)
```

再吐槽一下windows, 不仅那个progressbar的包不好使, multiprocessing的包也不好使, 郁闷... 