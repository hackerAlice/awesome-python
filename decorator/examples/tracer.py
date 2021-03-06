"""
Simpale decoraor examples.
"""

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print("call %s to %s" % (self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):  # spam = trace(spam)
    print(a + b + c)  # Wraps spam in a decorator object


if __name__ == "__main__":
    spam(1, 2, 3)