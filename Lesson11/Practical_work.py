class Person:

    def __init__(self):
        self.eat = 'pizza'

    def eat(self):
        pass

    def __add__(self, other):
        if other == self:
            return 'New person'

        elif isinstance(other, Gumanoid):
            return 'Predator'


class Gumanoid:

    def __init__(self):
        self.eat = 'people'

    def eat(self):
        pass

    def __add__(self, other):
        if isinstance(other, Person):
            return 'Cry gumanoid'

        elif other == self:
            return 'Egg gumanoid\'s'


x = Gumanoid()
y = Person()

print(y + y)
print(x + x)
print(x + y)
print(y + x)
