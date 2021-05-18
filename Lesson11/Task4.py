# Пользовательское исключение
#
# Создайте собственное исключение с именем `CustomException`, вы можете унаследовать его от базового класса Exception,
# но расширите его функциональность, чтобы записывать каждое сообщение об ошибке в файл с именем` logs.txt`.
# Советы: используйте метод __init__, чтобы расширить функциональность для сохранения сообщений в файл.
import os.path

class CustomException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        if os.path.isfile('logs.txt'):
            with open('logs.txt', 'a') as a:
                a.write(*args)
                a.write('\n')
                a.close()


        else:
            open('logs.txt', 'w')



try:
    val = input("input positive number: ")
    if not val.lstrip('-').isdigit():
        raise CustomException("Must be int")

    val = int(val)
    if val < 0:
        raise CustomException("Neg val: " + str(val))

    print(val + 10)
except CustomException as e:
    print(e)

# def __init__(self, msg):