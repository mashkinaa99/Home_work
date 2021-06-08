import re


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            text_splited = text.split(' ')

            if len(text_splited[0]) >= max_length:
                return 'Too many characters'

            if type(text_splited[0]) != type_:
                return 'Invalid data type'

            a = str(text_splited[0])
            for args in contains:
                if args not in a:
                    return 'Not all required characters have been entered'

            result = ' '.join(text_splited)
            return result

        return wrapper

    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
