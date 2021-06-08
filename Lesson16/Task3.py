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


c = Iterator(1, 10)
list_iter = []
for i in c:
    list_iter.append(i)

print(list_iter)
