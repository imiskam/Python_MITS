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