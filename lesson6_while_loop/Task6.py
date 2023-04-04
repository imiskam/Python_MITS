while True:
    num1 = float(input("Введите число 1: "))
    num2 = float(input("Введите число 2: "))
    operation = input("Введите операцию: ")
    if operation == "0":
        print("Программа завершена")
        break
    elif operation == "+":
        print(num1 / num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Деление на 0!")
