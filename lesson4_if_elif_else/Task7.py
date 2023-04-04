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
