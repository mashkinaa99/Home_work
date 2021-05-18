class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.deno = denominator

    def __add__(self, other):
        if self.deno == other.deno:
            top = self.num + other.num
            bottom = self.deno
            i = 10
            while i <= 10:
                if self.deno % i == 0 and top % i == 0:
                    top = int(top / i)
                    bottom = int(self.deno / i)
                    i -= 1
                return f'Result: {top}/{bottom}'

        else:
            bottom = self.deno * other.deno
            self.num = self.num * other.deno
            other.num = other.num * self.deno
            top = self.num + other.num
            i = 10
            while i <= 10:
                if bottom % i == 0 and top % i == 0:
                    top = int(top / i)
                    bottom = int(bottom / i)
                    i -= 1
                return f'Result: {top}/{bottom}'

    def __sub__(self, other):
        if self.deno == other.deno:
            top = self.num - other.num
            bottom = self.deno
            i = 10
            while 0 < i <= 10:
                if self.deno % i == 0 and top % i == 0:
                    top = int(top / i)
                    bottom = int(self.deno / i)
                    i -= 1
                return f'Result: {top}/{bottom}'

        else:
            bottom = self.deno * other.deno
            self.num = self.num * other.deno
            other.num = other.num * self.deno
            top = self.num - other.num
            i = 10
            while 0 < i <= 10:
                if bottom % i == 0 and top % i == 0:
                    top = int(top / i)
                    bottom = int(bottom / i)
                    i -= 1
                return f'Result: {top}/{bottom}'

    def __mul__(self, other):
        bottom = self.deno * other.deno
        top = self.num * other.num
        i = 10
        while 0 < i <= 10:
            if bottom % i == 0 and top % i == 0:
                top = int(top / i)
                bottom = int(bottom / i)
                i -= 1
            return f'Result: {top}/{bottom}'

    def __truediv__(self, other):
        bottom = self.deno * other.num
        top = self.num * other.deno
        i = 10
        while 0 < i <= 10:
            if bottom % i == 0 and top % i == 0:
                top = int(top / i)
                bottom = int(bottom / i)
                i -= 1
            return f'Result: {top}/{bottom}'


def interface():
    while True:
        try:
            print('1. Addition of fractions',
                  '2. Subtraction of fractions',
                  '3. Multiplication of fractions',
                  '4. Division of fractions',
                  sep='\n')
            a = int(input('What do you want to do: '))
            ftrst_1, ftrst_2 = map(int, input('Enter firs fraction (a/b): ').split('/'))
            second_1, second_2 = map(int, input('Enter second fraction (a/b): ').split('/'))
            x = Fraction(ftrst_1, ftrst_2)
            y = Fraction(second_1, second_2)
            if a == 1:
                print(x + y)

            elif a == 2:
                print(x - y)

            elif a == 3:
                print(x * y)

            elif a == 4:
                print(x / y)

        except ValueError:
            print('Incorrect data, try again')


interface()