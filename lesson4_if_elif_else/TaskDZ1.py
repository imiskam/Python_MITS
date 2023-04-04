import random

print("""Добро пожаловать в лотерею!
Правила игры: компьютер случайным образом генерирует двузначное число от 1 до 20.
Если вы угадываете первую цифру, вы получаете 20 % выигрыша.
Если вы угадываете и вторую цифру, вы получаете 100 % выигрыша.
""")

my_bet_1 = int(input("Введите первую цифру: "))
my_bet_2 = int(input("Введите вторую цифру: "))
rand = random.randint(1, 20)
print(f"Ваше число: {my_bet_1}{my_bet_2}")
print(f"Случайное число: {rand}")
if my_bet_1 == rand // 10:
    print("Ваш выигрыш за частичное угадывание: 20 %")
    if my_bet_2 == rand % 10:
        print("Ваш выигрыш за полное отгадывание: 100 %")
else:
    print("Вы проиграли")

