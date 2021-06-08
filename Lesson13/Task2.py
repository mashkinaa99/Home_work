def first():
    print('Test 1')


def second():
    print('Test 2')


def function(func):
    def wrapper():
        print('Function start')
        func()
        print('End of function')

    return wrapper


first_function = function(first)
second_function = function(second)

first_function()
print()
second_function()