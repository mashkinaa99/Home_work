class TVController:

    def __init__(self, channels, i, n, a):
        self.channels = channels
        self.i = i
        self.n = n
        self.a = a

    def first_channel(self):
        return self.channels[self.i]

    def last_channel(self):
        if self.i == 0:
            return self.channels[self.i + 2]

        if self.i == 1:
            return self.channels[self.i + 1]

        if self.i == 2:
            return self.channels[self.i]

    def turn_channel(self):

        if self.n == '1':
            self.i = 0
            return self.channels[self.i]

        if self.n == '2':
            self.i = 1
            return self.channels[self.i]

        if self.n == '3':
            self.i = 2
            return self.channels[self.i]

    def next_channel(self):

        if self.i == 0:
            self.i = 1
            return self.channels[self.i]

        if self.i == 1:
            self.i = 2
            return self.channels[self.i]

        if self.i == 2:
            self.i = 0
            return self.channels[self.i - 2]

    def previous_channel(self):

        if self.i == 0:
            self.i = 2
            return self.channels[self.i]

        if self.i == 1:
            self.i = 0
            return self.channels[self.i]

        if self.i == 2:
            self.i = 1
            return self.channels[self.i]

    def current_channel(self):

        return self.channels[self.i]

    def is_exist(self):
        if self.a == '1' or self.a == '2' or self.a == '3' or self.a == 'BBC' or self.a == 'Discovery' or self.a == 'TV1000':
            return 'Yes'
        else:
            return 'No'


i = 0
n = '1'
a = '4'

channels = ['BBC', 'Discovery', 'TV1000']

controller = TVController(channels, i, n, a)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel())
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist())
