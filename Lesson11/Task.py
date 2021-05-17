class Person:

    def __init__(self, name, last_name, age):
        self.name = name
        self.age = age
        self.last_name = last_name
        print(f'New person: {self.name} {self.last_name}')

    def tell(self):
        print(f'Persons name: {self.name} {self.last_name},',
              f'Age: {self.age},',
              end=' ')


class Student(Person):
    def __init__(self, name, last_name, age, marks):
        Person.__init__(self, name, last_name, age)
        self.marks = marks
        print(f'({self.name} is a student)')

    def tell(self):
        super().tell()
        print(f'Marks: {self.marks}')


class Teacher(Person):

    def __init__(self, name, last_name, age, salary):
        Person.__init__(self, name, last_name, age)
        self.salary = salary
        print(f'({self.name} is a teacher)')

    def tell(self):
        super().tell()
        print(f'Salary: {self.salary}')


t = Teacher('Alena', 'Kalashnikova', 22, 15000)
s = Student('Artem', 'Kalashnikov', 24, 12)

print()

members = [t, s]
for member in members:
    member.tell()
