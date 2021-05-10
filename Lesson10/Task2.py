class Dog:
    age_factor = 7

    def __init__(self, a):
        self.old = a

    def human_age(self):
        print(int(self.old) * int(Dog.age_factor))


old = input('Old: ')

c = Dog(old)

c.human_age()
