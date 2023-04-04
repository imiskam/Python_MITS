int_1 = int(input("Введите число 1: "))
int_2 = int(input("Введите число 2: "))
int_3 = int(input("Введите число 3: "))

if int_1 > int_2 and int_1 > int_3:
    print(int_1)
elif int_2 > int_1 and int_2 > int_3:
    print(int_2)
elif int_3 > int_1 and int_3 > int_2:
    print(int_3)