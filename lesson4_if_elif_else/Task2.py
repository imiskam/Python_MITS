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
