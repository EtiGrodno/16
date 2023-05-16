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
        if not isinstance(a, (int, str, list, tuple)):
            raise TypeError('Тип неизвестен')
        print(f' Указанные данные: {a}, Являютса: {type(a)} ')
        return fn(a)
    return wrapper

@function_info
def examination(x):
    if isinstance(x, tuple):
        return (f" Количество всех строк: {len(x)}")
    elif isinstance(x, list):
        x = (str("".join(map(str, x))))
        return (f' Количество букв:{len([i for i in x if str(i).isalpha()])} '
                f' Количество цифр: {len([i for i in x if str(i).isdigit()])}')
    elif isinstance(x, int):
        return(f" Кол-во нечётных цифр: {len([i for i in str(x) if i in '13579'])}")
    elif isinstance(x, str):
        return (f' Количество букв:{len([i for i in x if str(i).isalpha()])} ')

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