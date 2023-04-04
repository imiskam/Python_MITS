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
