import requests
from bs4 import BeautifulSoup
import csv
import json

# Задание 1
# Введите два числа с клавиатуры. Поделите одно на другое.
# Обработайте ошибку деления на ноль, если ошибок нет, то результат
# деления возвести в квадрат. Также используйте оператор finally.

num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
try:
    division_result = num1 / num2
except ZeroDivisionError:
    print("Деление на ноль!")
else:
    print(division_result ** 2)
finally:
    print("Сработал Finally")

##################################################################

# Задание 2
# Введите два числа с клавиатуры. Поделите одно на другое.
# Обработайте деления на ноль, преобразования и общее исключение.

try:
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))
    division_result = num1 / num2
except ZeroDivisionError:
    print("Деление на ноль!")
except ArithmeticError:
    print("Произошла арифметическая ошибка")
except ValueError:
    print("Произошла ошибка преобразования")
except Exception:
    print("Произошла другая ошибка")
else:
    print("Ошибок не произошло")

##################################################################

# Домашнее задание
# Ввод с клавиатуры. Если строка введённая с клавиатуры –
# это числа, то поделить первое на второе. Обработать
# ошибку деления на ноль. Если второе число 0, то
# программа запрашивает ввод чисел заново. Также если
# были введены буквы, то обработать исключение.


while True:
    try:
        str1 = input("Введите число 1: ")
        str2 = input("Введите число 2: ")
        if str1.isdigit() and str2.isdigit():
            result = int(str1) / int(str2)
            print(result)
            break
        elif str1.isalpha() or str2.isalpha():
            raise ValueError("Нужно ввести числа!")
    except ZeroDivisionError:
        print("Деление на 0!")
        continue
