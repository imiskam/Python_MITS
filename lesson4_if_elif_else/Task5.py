import random
import sys

print("""Добро пожаловать в игру "Камень, ножницы, бумага"!
Чтобы выбрать Камень ---> введите 1.
Чтобы выбрать Ножницы ---> введите 2.
Чтобы выбрать Бумагу ---> введите 3.
""")

my_turn = int(input("Введите число: "))
computer_turn = random.randint(1, 3)
print("Выбор компьютера: ", computer_turn)

if my_turn not in (1, 2, 3):
    # доп. проверка: если не вводится число в диапазоне 1-3,
    # программа обрабатывает ошибку и закрывается
    print("Число 1/2/3 не было введено!")
    sys.exit()
elif my_turn == 1 and computer_turn == 2:
    print("Выигрыш!")
elif my_turn == 2 and computer_turn == 3:
    print("Выигрыш!")
elif my_turn == 3 and computer_turn == 1:
    print("Выигрыш!")
elif my_turn == computer_turn:
    print("Ничья!")
else:
    print("Вы проиграли!")
