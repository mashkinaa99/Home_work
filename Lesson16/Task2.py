class Iterator:

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        var = self.start
        self.start += self.step
        return var


c = list(Iterator(0, 10))
print(c)
