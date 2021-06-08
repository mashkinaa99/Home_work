from functools import wraps


def logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'{func.__name__} called with {*args, *kwargs}')

    return wrap


@logger
def add(x, y):
    return x + y


add(1, 2)


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


square_all(2, 4, 6)
