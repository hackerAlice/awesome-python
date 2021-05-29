class Number:
    def __init__(self, start):  # On Number(start)
        self.data = start

    def __sub__(self, other):  # On instance - other, 重载减法
        return Number(self.data - other)


if __name__ == "__main__":
    X = Number(5)
    Y = X - 2
    print(Y.data)