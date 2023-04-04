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