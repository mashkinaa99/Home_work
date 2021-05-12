class Person:

    def __init__(self):
        self.eat = 'pizza'

    def eat(self):
        pass

    def __add__(self, other):
        if other == 'Person':
            return 'New person'

        elif other == 'Gumanoid':
            return 'Predator'


class Gumanoid:

    def __init__(self):
        self.eat = 'people'

    def eat(self):
        pass

    def __add__(self, other):
        if other == 'Person':
            return 'Cry gumanoid'

        elif other == 'Gumanoid':
            return 'Egg gumanoid\'s'


x = Gumanoid()
y = Person()

print(x + 'Person')
print(y + 'Person')
