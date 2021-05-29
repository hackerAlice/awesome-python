#!/usr/bin/python3

"""
tracer.py中文件使用装饰器的一种替代方法
"""

calls = 0

def tracer(func, *args):
    global calls
    calls += 1
    print("call %s to %s" % (calls, func.__name__))
    func(*args)

def spam(a, b, c):
    print(a, b, c)


if __name__ == "__main__":
    spam(1, 2, 3)
    tracer(spam, 1, 2, 3)