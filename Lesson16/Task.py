class Iterator:

    def __init__(self, *items):
        self.items = items

    def __getitem__(self, num):
        num += 1
        return num, self.items[num - 1]


iterator = Iterator('c', 'v', 'd')

for count, value in iterator:
    print(count, value)


