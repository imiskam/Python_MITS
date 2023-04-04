import random

print("""
Добро пожаловать в наше казино!
В игре "Рулетка" Вы можете сделать свою ставку на:
1) конкретное число (0 - 36) ---> сумма возрастает в 35 раз!
2) Четное/Нечетное число ---> выигрыш составляет 40% от ставки!
3) диапазон чисел (1-18 или 19-36) ---> выигрыш составляет 10% от ставки!
4) конкретный цвет (Красный или Черный) ---> выигрыш составляет 50% от ставки!
""")

user1_account = int(input("Игрок 1, задайте количество долларов в Вашем кармане: "))
user2_account = int(input("Игрок 2, задайте количество долларов в Вашем кармане: "))

range1_18 = range(1, 18)
range19_36 = range(19, 36)

roulette_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
red_numbers = roulette_numbers[1::2]
black_numbers = roulette_numbers[2::2]

game_cycle = 0
# цикл нужен для смены игр и подсчета денег пользователей
while True:
    if user1_account <= 0 or user2_account <= 0:
        if user1_account <= 0:
            print("Игрок 1, Вы - банкрот! Срочно займите денег и поскорее возвращайтесь к нам снова :)")
            if user2_account <= 0:
                print("Игрок 2, Вы - банкрот! Срочно займите денег и поскорее возвращайтесь к нам снова :)")
        break
    user1_bet = input("Игрок 1, сделайте ставку: ")
    user1_money_per_bet = int(input("Введите сумму для вашей ставки: "))
    user2_bet = input("Игрок 2, сделайте ставку: ")
    user2_money_per_bet = int(input("Введите сумму для вашей ставки: "))
    roll_result = str(random.randint(0, 36))
    print("Выпадение шарика на:", roll_result)
    # РЕАЛИЗАЦИЯ ДЛЯ ИГРОКА 1
    if user1_bet == roll_result:  # совпадение по конкретному числу
        user1_account += user1_money_per_bet * 35
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
        if int(user1_bet) == 0 and int(roll_result) == 0:  # совпадение по нулю
            user1_account += user1_money_per_bet * 35
            print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Четное" and int(roll_result) % 2 == 0:  # совпадение по четности
        user1_account += user1_money_per_bet / 100 * 40
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Нечетное" and int(roll_result) % 2 == 1:  # совпадение по нечетности
        user1_account += user1_money_per_bet / 100 * 40
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "1-18" and int(roll_result) in range1_18:  # совпадение по диапазону 1
        user1_account += user1_money_per_bet / 100 * 10
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "19-36" and int(roll_result) in range19_36:  # совпадение по диапазону 2
        user1_account += user1_money_per_bet / 100 * 10
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Красный" and int(roll_result) in red_numbers:  # совпадение по красному цвету
        user1_account += user1_money_per_bet / 100 * 50
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Черный" and int(roll_result) in black_numbers:  # совпадение по черному цвету
        user1_account += user1_money_per_bet / 100 * 50
        print("Игрок 1, Вы выиграли! Ваш текущий счет: ", user1_account)
    else:
        user1_account -= user1_money_per_bet
        print("Игрок 1, Вы проиграли! Ваш текущий счет: ", user1_account)

    # РЕЛИЗАЦИЯ ДЛЯ ИГРОКА 2
    if user2_bet == roll_result:  # совпадение по конкретному числу
        user2_account += user2_money_per_bet * 35
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
        if int(user2_bet) == 0 and int(roll_result) == 0:  # совпадение по нулю
            user2_account += user2_money_per_bet * 35
            print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Четное" and int(roll_result) % 2 == 0:  # совпадение по четности
        user2_account += user2_money_per_bet / 100 * 40
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Нечетное" and int(roll_result) % 2 == 1:  # совпадение по нечетности
        user2_account += user2_money_per_bet / 100 * 40
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "1-18" and int(roll_result) in range1_18:  # совпадение по диапазону 1
        user2_account += user2_money_per_bet / 100 * 10
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "19-36" and int(roll_result) in range19_36:  # совпадение по диапазону 2
        user2_account += user2_money_per_bet / 100 * 10
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Красный" and int(roll_result) in red_numbers:  # совпадение по красному цвету
        user2_account += user2_money_per_bet / 100 * 50
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Черный" and int(roll_result) in black_numbers:  # совпадение по черному цвету
        user2_account += user2_money_per_bet / 100 * 50
        print("Игрок 2, Вы выиграли! Ваш текущий счет: ", user2_account)
    else:
        user2_account -= user2_money_per_bet
        print("Игрок 2, Вы проиграли! Ваш текущий счет: ", user2_account)

    game_cycle += 1
