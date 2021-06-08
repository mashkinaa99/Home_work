class Person:

    def __init__(self, a, b, c):
        self.name = a
        self.last_name = b
        self.old = c

    def talk(self):
        print(f'Hello, my name is {self.name} {self.last_name} and I’m {self.old} years old')


name = input('Name: ')
last_name = input('Last name: ')
old = input('Old: ')

c = Person(name, last_name, old)

c.talk()
