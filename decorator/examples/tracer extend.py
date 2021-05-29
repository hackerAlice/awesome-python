"""
tracer.py的扩展
"""

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        self.func(*args, **kwargs)


@tracer
def spam(a, b, c):  # spam = trace(spam)
    print(a + b + c)  # Wraps spam in a decorator object


@tracer
def eggs(x, y):
    print(x ** y)


if __name__ == "__main__":
    spam(1, 2, 3)
    spam(a=3, b=4, c=5)

    eggs(2, 6)
    eggs(4, 4)