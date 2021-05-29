# 异常基础


## 1. 异常的角色

* 错误处理
* 事件通知
* 特殊情况处理
* 终止行为
* 非常规控制流程

## 2. 捕获异常

捕获异常的语法

```python
try:
    statement
except:
    statement
```

### 2.1 try/except/else语句

```python
try:
    <statements>
except <name1>:
    <statements>
except (name1, name2):
    <statements>
except <name4> as <data>:
    <statements>
except:
    <statements>
else:
    <statements>
```

上面是`try/except/else语句`的模板，其中`else（可选）`语句块是没有异常发生时执行。

try语句分句形式：

```
except:    捕捉所有(其他)异常类型
except name:    只捕捉特定的异常
except name,value:      捕捉所列的异常和其额外的数据或实例
excpet (name1, name2):   捕捉任何列出的异常
except (name1, name2), value:   捕捉任何列出的异常，并获取其额外数据
else:       如果没有引发异常，就运行
finally:    总是会运行此代码块
```

## 3. 引发异常

使用`rasie`来抛出异常

```python
try:
    raise IndexError
except IndexError:
    print("got exception")
```

## 4. 自定义异常类

一般通过继承`Exception`类来定义异常

```python
class Bad(Exception):
    pass

try:
    raise Bad()
except Bad:
    print('got bad')
```

## 5. 终止行为

无论`try`语句块中是否发生异常，`finally`语句块中的命令总会执行

```python
try:
    raise IndexError
finally:
    print('running...')
```
