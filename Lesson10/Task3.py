class TVController:
    channel = 0

    def __init__(self, channels):
        self.channels = channels
        self.count = len(channels)

    def first_channel(self):
        self.channel = 0
        return self.channels[0]

    def last_channel(self):
        self.channel = self.count - 1
        return self.channels[self.channel]

    def turn_channel(self, channel_number):
        if 0 < channel_number <= self.count:
            self.channel = channel_number - 1
            return self.channels[self.channel]

    def next_channel(self):
        self.channel += 1

        if self.channel > self.count - 1:
            self.channel = 0

        return self.channels[self.channel]

    def previous_channel(self):
        self.channel -= 1

        if self.channel > self.count - 1:
            self.channel = 0

        return self.channels[self.channel]

    def current_channel(self):
        return self.channels[self.channel]

    def is_exist(self, number):
        if number in range(self.count) or number in self.channels:
            return 'Yes'
        else:
            return 'No'


channels = ['BBC', 'Discovery', 'TV1000']

controller = TVController(channels)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(4))
