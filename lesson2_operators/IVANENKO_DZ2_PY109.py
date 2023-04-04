import math
import random
from faker import Faker

# Задание 2
expression1 = 17 / 2 * 3 + 2
expression2 = 2 + 17 / 2 * 3
expression3 = 19 % 4 + 15 / 2 * 3
expression4 = (15 + 6) - 10 * 4
expression5 = 17 / 2 % 2 * 3 ** 3
print(expression1, expression2, expression3, expression4, expression5)

# Задание 6
# формула - b^2 − 4ac
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))
discriminant = (b ** 2) - (4 * a * c)
print(discriminant)

# Задание 7
# нахождение периметра треугольника (P = A + B + C)
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
perimeter = a + b + c
print(perimeter)
# нахождение площади треугольника
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
p = (a + b + c) / 2
square = math.sqrt(p * (p - a) * (p - b) * (p - c))  # формула Герона
print(square)

# Задание 8
rand = random.randint(100, 999)
print(rand)

int1 = rand // 100
print(int1)
int2 = (rand // 10) % 10
print(int2)
int3 = rand % 10
print(int3)
result = int1 + int2 + int3
print(result)

# Задание 9 (креативное)
# IT компания за год нанимает 50 сотрудников, которым на старте платит бонус в размере $700
# Найти общее количество трат на стартовые бонусы за 5 лет

people_count_per_year = 50
extra_money = 700
years = 5
result = (people_count_per_year * extra_money * years)
print(result)
print("Слишком много, надо кого-то уволить")

# Задание 10
annas_apples = 2
pauls_apples = 5
print("У Анны", annas_apples, "яблок, у Пола", pauls_apples, "яблок.")

# Задание 11
edge_length = float(input("Введите длину ребра куба: "))
# вычисляем площадь поверхности куба
surface_square = edge_length ** 2
print(surface_square)
# вычисляем объем куба
volume = edge_length ** 3
print(volume)

# Задание 12
# если за сутки улитка в итоге проползает 1м, то 20м * 1м/день = 20 дней
day_speed = 2
night_speed = -1
tree_height = 20
days_result = tree_height / (day_speed + night_speed)
print(days_result)

# Задание 13 (Faker)
fake = Faker(['ru_RU', 'en_US', 'ja_JP'])
print("1.", fake.name(), fake.address(), end='\n')
print("2.", fake.name(), fake.address(), end='\n')
print("3.", fake.name(), fake.address(), end='\n')
