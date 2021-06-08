import re


def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            text_splited = re.split(r'(\W)', text)
            text_changed = list(map(lambda word: '*' if word in words else word, text_splited))
            result = ''.join(text_changed)

            return result
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('Steve'))

