import random
import sys

# Задание 1
int_ = int(input("Введите целое число: "))
if int_ % 2 == 0:
    print("Это четное число")
else:
    print("Нечетное число")

##################################

# Задание 2
hand = int(input("Введите 1 для левой руки или 2 для правой руки: "))
finger_no = int(input("Введите номер пальца и получите его название: "))
# ветвление для левой руки
if hand == 1 and finger_no == 1:
    print("Мизинец")
elif hand == 1 and finger_no == 2:
    print("Безымянный")
elif hand == 1 and finger_no == 3:
    print("Средний")
elif hand == 1 and finger_no == 4:
    print("Указательный")
elif hand == 1 and finger_no == 5:
    print("Большой")
# ветвление для правой руки
elif hand == 2 and finger_no == 1:
    print("Большой")
elif hand == 2 and finger_no == 2:
    print("Указательный")
elif hand == 2 and finger_no == 3:
    print("Средний")
elif hand == 2 and finger_no == 4:
    print("Безымянный")
elif hand == 2 and finger_no == 5:
    print("Мизинец")
# если верхние условия не выполняются
else:
    print("У вас больше 2 рук или больше 5 пальцев")

##################################

# Задание 3
month_no = int(input("Введите номер месяца: "))
if month_no in (1, 2, 12):
    print("Зима")
elif month_no in (3, 4, 5):
    print("Весна")
elif month_no in (6, 7, 8):
    print("Лето")
elif month_no in (9, 10, 11):
    print("Осень")
else:
    print("Такого месяца не существует!")

##################################

# Задание 4
int_1 = int(input("Введите число 1: "))
int_2 = int(input("Введите число 2: "))
int_3 = int(input("Введите число 3: "))

if int_1 > int_2 and int_1 > int_3:
    print(int_1)
elif int_2 > int_1 and int_2 > int_3:
    print(int_2)
elif int_3 > int_1 and int_3 > int_2:
    print(int_3)

##################################

# Задание 5
print("""Добро пожаловать в игру "Камень, ножницы, бумага"!
Чтобы выбрать Камень ---> введите 1.
Чтобы выбрать Ножницы ---> введите 2.
Чтобы выбрать Бумагу ---> введите 3.
""")

my_turn = int(input("Введите число: "))
computer_turn = random.randint(1, 3)
print("Выбор компьютера: ", computer_turn)

if my_turn not in (1, 2, 3):
    # доп. проверка: если не вводится число в диапазоне 1-3,
    # программа обрабатывает ошибку и закрывается
    print("Число 1/2/3 не было введено!")
    sys.exit()
elif my_turn == 1 and computer_turn == 2:
    print("Выигрыш!")
elif my_turn == 2 and computer_turn == 3:
    print("Выигрыш!")
elif my_turn == 3 and computer_turn == 1:
    print("Выигрыш!")
elif my_turn == computer_turn:
    print("Ничья!")
else:
    print("Вы проиграли!")

##################################

# Задание 6
int_1 = int(input("Введите число 1: "))
int_2 = int(input("Введите число 2: "))

# задать переменную, которой будет присвоено значение boolean
integers = int_1 >= int_2
print(integers)
# использовать сразу переменную boolean вместо логических операторов
if integers:
    print(int_1, "больше", int_2)
else:
    print(int_1, "меньше или равно", int_2)

##################################

# Задание 7
a = int(input("Введите сторону 1: "))
b = int(input("Введите сторону 2: "))
c = int(input("Введите сторону 3: "))

# записать значения в переменную boolean
is_triangle_exists = a + b > c or a + c > b or b + c > b
if is_triangle_exists:
    print("Треугольник с заданными сторонами существует")
    if a == b == c:
        print("Это равносторонний треугольник")
else:
    print("Это несуществующий треугольник")

##################################

# Задание 8
int_1 = float(input("Введите число 1: "))
operation = input("Введите операцию: ")
int_2 = float(input("Введите число 2: "))

# operation это str, поэтому сравниваем ее со значением строки
if operation == "+":
    print(int_1 + int_2)
elif operation == "-":
    print(int_1 - int_2)
elif operation == "*":
    print(int_1 * int_2)
elif operation == "/":
    print(int_1 / int_2)
else:
    print("Проверьте корректность ввода!")

##################################

# Задание 9
str_ = input("Введите строку: ")
# задать предикат, где значение введенной строки с большой буквы будет сравниваться с "Mister"
is_mister = str_.capitalize() == "Mister"
if is_mister:
    print(is_mister)
else:
    print(False)

##################################

# Задание 10
armor_color = input("Enter the armor color: ").capitalize()  # red, yellow, black
shield_color = input("Enter the shield color: ").capitalize()  # red, yellow, black
color_list = ("Red", "Yellow", "Black")

# задать предикат, в котором цвет доспехов и щита будут сравниваться с введенными пользователем
is_equipment = armor_color != "Red" and armor_color in color_list \
               and shield_color == "Black" and shield_color in color_list  # доп. проверки на наличие нужного цвета в списке
# проверка предиката
if is_equipment:
    print(is_equipment)
else:
    if armor_color not in color_list or shield_color not in color_list:
        print(f"The {armor_color} or {shield_color} color doesn't exist")
    print(False)

##################################

# Домашнее задание 1
print("""Добро пожаловать в лотерею!
Правила игры: компьютер случайным образом генерирует двузначное число от 1 до 20.
Если вы угадываете первую цифру, вы получаете 20 % выигрыша.
Если вы угадываете и вторую цифру, вы получаете 100 % выигрыша.
""")

my_bet_1 = int(input("Введите первую цифру: "))
my_bet_2 = int(input("Введите вторую цифру: "))
rand = random.randint(1, 20)
print(f"Ваше число: {my_bet_1}{my_bet_2}")
print(f"Случайное число: {rand}")
if my_bet_1 == rand // 10:
    print("Ваш выигрыш за частичное угадывание: 20 %")
    if my_bet_2 == rand % 10:
        print("Ваш выигрыш за полное отгадывание: 100 %")
else:
    print("Вы проиграли")

##################################

# Домашнее задание 2
# Январь - 31 день
# Февраль - 28 дней (29 в високосном)
# Март - 31 день
# Апрель - 30 дней
# Май - 31 день
# Июнь - 30 дней
# Июль - 31 день
# Август - 31 день
# Сентябрь - 30 дней
# Октябрь - 31 день
# Ноябрь - 30 дней
# Декабрь - 31 день

birth_day = int(input("Введите день своего рождения: "))
birth_month = int(input("Введите месяц своего рождения: "))
# Овен : 21 марта – 20 апреля
if (birth_day >= 21 and birth_day <= 31 and birth_month == 3) or (
        birth_day >= 1 and birth_day <= 20 and birth_month == 4):
    print("Овен")
# Телец : 21 апреля – 21 мая
elif (birth_day >= 21 and birth_day <= 30 and birth_month == 4) or (
        birth_day >= 1 and birth_day <= 21 and birth_month == 5):
    print("Телец")
# Близнецы : 22 мая – 21 июня
elif (birth_day >= 22 and birth_day <= 31 and birth_month == 5) or (
        birth_day >= 1 and birth_day <= 21 and birth_month == 6):
    print("Близнецы")
# Рак : 22 июня – 22 июля
elif (birth_day >= 22 and birth_day <= 30 and birth_month == 6) or (
        birth_day >= 1 and birth_day <= 22 and birth_month == 7):
    print("Рак")
# Лев : 23 июля – 23 августа
elif (birth_day >= 23 and birth_day <= 31 and birth_month == 7) or (
        birth_day >= 1 and birth_day <= 23 and birth_month == 8):
    print("Лев")
# Дева : 24 августа – 22 сентября
elif (birth_day >= 24 and birth_day <= 31 and birth_month == 8) or (
        birth_day >= 1 and birth_day <= 22 and birth_month == 9):
    print("Дева")
# Весы : 23 сентября – 23 октября
elif (birth_day >= 23 and birth_day <= 30 and birth_month == 9) or (
        birth_day >= 1 and birth_day <= 23 and birth_month == 10):
    print("Весы")
# Скорпион : 24 октября – 22 ноября
elif (birth_day >= 24 and birth_day <= 31 and birth_month == 10) or (
        birth_day >= 1 and birth_day <= 22 and birth_month == 11):
    print("Скорпион")
# Стрелец : 23 ноября – 21 декабря
elif (birth_day >= 23 and birth_day <= 30 and birth_month == 11) or (
        birth_day >= 1 and birth_day <= 21 and birth_month == 12):
    print("Стрелец")
# Козерог : 22 декабря – 20 января
elif (birth_day >= 22 and birth_day <= 31 and birth_month == 12) or (
        birth_day >= 1 and birth_day <= 20 and birth_month == 1):
    print("Козерог")
# Водолей : 21 января – 18 февраля
elif (birth_day >= 21 and birth_day <= 31 and birth_month == 1) or (
        birth_day >= 1 and birth_day <= 18 and birth_month == 2):
    print("Водолей")
# Рыбы : 19 февраля – 20 марта
elif (birth_day >= 19 and birth_day <= 29 and birth_month == 2) or (
        birth_day >= 1 and birth_day <= 20 and birth_month == 3):
    print("Рыбы")
else:
    print("Проверьте корректность данных!")
