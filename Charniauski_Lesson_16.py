#ДЗ на четверг (Ivanov_Lesson_15.py)
# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0
# №2. Привяжите к предыдущей функции декоратор, который будет выводить
# информацию о том, какой тип данных вы отправили:
# кортеж, список, число, строку или какой-то другой
#
#Сбарсываем ссылку на файл в репозитории



def function_info(fn):
    def wrapper(a):
        data_type = type(a).__name__
        print(f' Указанные данные: {a}, Являютса: {data_type} ')
        return fn(a)
    return wrapper

@function_info
def examination(x):
    if isinstance(x, tuple):
        return (f" Количество всех строк: {len(x)}")
    elif isinstance(x, list):
        return (f' Количество букв:{sum(isinstance(item, str) for item in x)} '
                f' Количество цифр: {sum(isinstance(item, int) for item in x)}')
    elif isinstance(x, int):
        return(f" Кол-во нечётных цифр: {sum(int(digit) % 2 != 0 for digit in str(x))}")
    elif isinstance(x, str):
        return (f' Количество букв:{sum(1 for char in x if char.isalpha())} ')
    else:
        print("Неподходящий тип данных. Введите тип данных соответствующий:tuple,string list, or integer.")


print(examination((1,2,3,'a','bc8?',7,8,9)))
print(examination([1,2,3,'a','bc8?']))
print(examination(788))
print(examination('78g8'))
print(examination((1,2,3,'a','bc8?',7,8,91,2,3,'a','bc8?')))
print(examination(785982318))
print(examination({
    'milk': [4, 9],
    'cheese': [6, 15],
    'bread': [5, 8],
    'apple': [7, 10]
}))