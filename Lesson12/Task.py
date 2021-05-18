class Animal:

    def talk(self):
        pass


class Dog(Animal):

    def talk(self):
        return 'woof woof'


class Cat(Animal):

    def talk(self):
        return 'meow'


dog = Dog()
cat = Cat()


def cat_say():
    return cat.talk()


def dog_say():
    return dog.talk()


print(cat_say())
print(dog_say())
