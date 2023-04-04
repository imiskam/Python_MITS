import math

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
square = math.sqrt(p * (p - a) * (p - b) * (p - c)) # формула Герона
print(square)