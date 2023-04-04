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
if (birth_day >= 21 and birth_day <= 31 and birth_month == 3) or (birth_day >= 1 and birth_day <= 20 and birth_month == 4):
    print("Овен")
# Телец : 21 апреля – 21 мая
elif (birth_day >= 21 and birth_day <= 30 and birth_month == 4) or (birth_day >= 1 and birth_day <= 21 and birth_month == 5):
    print("Телец")
# Близнецы : 22 мая – 21 июня
elif (birth_day >= 22 and birth_day <= 31 and birth_month == 5) or (birth_day >= 1 and birth_day <= 21 and birth_month == 6):
    print("Близнецы")
# Рак : 22 июня – 22 июля
elif (birth_day >= 22 and birth_day <= 30 and birth_month == 6) or (birth_day >= 1 and birth_day <= 22 and birth_month == 7):
    print("Рак")
# Лев : 23 июля – 23 августа
elif (birth_day >= 23 and birth_day <= 31 and birth_month == 7) or (birth_day >= 1 and birth_day <= 23 and birth_month == 8):
    print("Лев")
# Дева : 24 августа – 22 сентября
elif (birth_day >= 24 and birth_day <= 31 and birth_month == 8) or (birth_day >= 1 and birth_day <= 22 and birth_month == 9):
    print("Дева")
# Весы : 23 сентября – 23 октября
elif (birth_day >= 23 and birth_day <= 30 and birth_month == 9) or (birth_day >= 1 and birth_day <= 23 and birth_month == 10):
    print("Весы")
# Скорпион : 24 октября – 22 ноября
elif (birth_day >= 24 and birth_day <= 31 and birth_month == 10) or (birth_day >= 1 and birth_day <= 22 and birth_month == 11):
    print("Скорпион")
# Стрелец : 23 ноября – 21 декабря
elif (birth_day >= 23 and birth_day <= 30 and birth_month == 11) or (birth_day >= 1 and birth_day <= 21 and birth_month == 12):
    print("Стрелец")
# Козерог : 22 декабря – 20 января
elif (birth_day >= 22 and birth_day <= 31 and birth_month == 12) or (birth_day >= 1 and birth_day <= 20 and birth_month == 1):
    print("Козерог")
# Водолей : 21 января – 18 февраля
elif (birth_day >= 21 and birth_day <= 31 and birth_month == 1) or (birth_day >= 1 and birth_day <= 18 and birth_month == 2):
    print("Водолей")
# Рыбы : 19 февраля – 20 марта
elif (birth_day >= 19 and birth_day <= 29 and birth_month == 2) or (birth_day >= 1 and birth_day <= 20 and birth_month == 3):
    print("Рыбы")
else:
    print("Проверьте корректность данных!")
