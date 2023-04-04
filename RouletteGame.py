import random

print("""
==============================================================================
Добро пожаловать в наше казино!
В игре "Рулетка" Вы можете сделать свою ставку на:
1) конкретное число (0 - 36) ---> сумма возрастает в 35 раз!
2) "Четное"/"Нечетное" число ---> выигрыш составляет 40% от ставки!
3) диапазон чисел (вводить "1-18" или "19-36") ---> выигрыш составляет 10% от ставки!
4) "Красный"/"Черный" цвет ---> выигрыш составляет 50% от ставки!
==============================================================================
""")
# игроки могут выбирать себе имя
user1_name = input("Игрок 1, укажите Ваше имя: ")
user2_name = input("Игрок 2, укажите Ваше имя: ")
user3_name = input("Игрок 3, укажите Ваше имя: ")
# игроки приходят в казино с разными суммами
user1_account = int(input(f"{user1_name}, задайте количество долларов в Вашем кармане: "))
user2_account = int(input(f"{user2_name}, задайте количество долларов в Вашем кармане: "))
user3_account = int(input(f"{user3_name}, задайте количество долларов в Вашем кармане: "))
# объявлены переменные для диапазонов чисел
range1_18 = range(1, 18)
range19_36 = range(19, 36)

roulette_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
# цвет определяется срезом по списку с определенным шагом
red_numbers = roulette_numbers[1::2]
black_numbers = roulette_numbers[2::2]
# изначально счетчик игры стоит на нуле
game_cycle = 0
# цикл нужен для смены игр и подсчета денег пользователей
while True:
    # проверки на пустой счет пользователя
    if user1_account <= 0 or user2_account <= 0 or user3_account <= 0:
        # вложенные if для того, чтобы все счета прошли проверку на отсутствие средств
        # и только потом выполнился break в случае совпадения.
        # на выходных попробую сделать логику на то, что если у одного игрока заканчиваются деньги, остальные продолжают игру до опустошения счетов.
        # пока что не хватает времени
        if user1_account <= 0:
            print(f"{user1_name}, Вы - банкрот! Срочно займите денег и поскорее возвращайтесь к нам снова :)")
        if user2_account <= 0:
            print(f"{user2_name}, Вы - банкрот! Срочно займите денег и поскорее возвращайтесь к нам снова :)")
        if user3_account <= 0:
            print(f"{user3_name}, Вы - банкрот! Срочно займите денег и поскорее возвращайтесь к нам снова :)")
        print("Игра окончена!")
        break

    print(f"Игра {game_cycle} началась!")
    # объявлены переменные со ставками и суммой ставок
    user1_bet = input(f"{user1_name}, на что ставите?: ")
    user1_money_per_bet = int(input("Введите сумму для Вашей ставки: "))
    user2_bet = input(f"{user2_name}, на что ставите?: ")
    user2_money_per_bet = int(input("Введите сумму для Вашей ставки: "))
    user3_bet = input(f"{user3_name}, на что ставите?: ")
    user3_money_per_bet = int(input("Введите сумму для Вашей ставки: "))
    # генератор случайных чисел от 0 до 36, принт результата и цвета
    roll_result = str(random.randint(0, 36))
    print(f"Выпадение шарика на: {roll_result}")
    if int(roll_result) in red_numbers:
        print("Цвет: Красный")
    elif int(roll_result) in black_numbers:
        print("Цвет: Черный")

    # РЕАЛИЗАЦИЯ ДЛЯ ИГРОКА 1
    if user1_bet == roll_result:  # совпадение по конкретному числу
        user1_account += user1_money_per_bet * 35
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
        if int(user1_bet) == 0 and int(roll_result) == 0:  # совпадение по нулю
            user1_account += user1_money_per_bet * 35
            print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Четное" and int(roll_result) % 2 == 0:  # совпадение по четности
        user1_account += user1_money_per_bet / 100 * 40
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Нечетное" and int(roll_result) % 2 == 1:  # совпадение по нечетности
        user1_account += user1_money_per_bet / 100 * 40
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "1-18" and int(roll_result) in range1_18:  # совпадение по диапазону 1
        user1_account += user1_money_per_bet / 100 * 10
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "19-36" and int(roll_result) in range19_36:  # совпадение по диапазону 2
        user1_account += user1_money_per_bet / 100 * 10
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Красный" and int(roll_result) in red_numbers:  # совпадение по красному цвету
        user1_account += user1_money_per_bet / 100 * 50
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    elif user1_bet == "Черный" and int(roll_result) in black_numbers:  # совпадение по черному цвету
        user1_account += user1_money_per_bet / 100 * 50
        print(f"{user1_name}, Вы выиграли! Ваш текущий счет: ", user1_account)
    else:
        user1_account -= user1_money_per_bet
        print(f"{user1_name}, Вы проиграли! Ваш текущий счет: ", user1_account)

    # РЕАЛИЗАЦИЯ ДЛЯ ИГРОКА 2
    if user2_bet == roll_result:  # совпадение по конкретному числу
        user2_account += user2_money_per_bet * 35
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
        if int(user2_bet) == 0 and int(roll_result) == 0:  # совпадение по нулю
            user2_account += user2_money_per_bet * 35
            print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Четное" and int(roll_result) % 2 == 0:  # совпадение по четности
        user2_account += user2_money_per_bet / 100 * 40
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Нечетное" and int(roll_result) % 2 == 1:  # совпадение по нечетности
        user2_account += user2_money_per_bet / 100 * 40
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "1-18" and int(roll_result) in range1_18:  # совпадение по диапазону 1
        user2_account += user2_money_per_bet / 100 * 10
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "19-36" and int(roll_result) in range19_36:  # совпадение по диапазону 2
        user2_account += user2_money_per_bet / 100 * 10
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Красный" and int(roll_result) in red_numbers:  # совпадение по красному цвету
        user2_account += user2_money_per_bet / 100 * 50
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    elif user2_bet == "Черный" and int(roll_result) in black_numbers:  # совпадение по черному цвету
        user2_account += user2_money_per_bet / 100 * 50
        print(f"{user2_name}, Вы выиграли! Ваш текущий счет: ", user2_account)
    else:
        user2_account -= user2_money_per_bet
        print(f"{user2_name}, Вы проиграли! Ваш текущий счет: ", user2_account)

    # РЕАЛИЗАЦИЯ ДЛЯ ИГРОКА 3
    if user3_bet == roll_result:  # совпадение по конкретному числу
        user3_account += user3_money_per_bet * 35
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
        if int(user3_bet) == 0 and int(roll_result) == 0:  # совпадение по нулю
            user3_account += user3_money_per_bet * 35
            print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    elif user3_bet == "Четное" and int(roll_result) % 2 == 0:  # совпадение по четности
        user3_account += user3_money_per_bet / 100 * 40
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    elif user3_bet == "Нечетное" and int(roll_result) % 2 == 1:  # совпадение по нечетности
        user3_account += user3_money_per_bet / 100 * 40
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    elif user3_bet == "1-18" and int(roll_result) in range1_18:  # совпадение по диапазону 1
        user3_account += user3_money_per_bet / 100 * 10
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    elif user3_bet == "19-36" and int(roll_result) in range19_36:  # совпадение по диапазону 2
        user3_account += user3_money_per_bet / 100 * 10
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    elif user3_bet == "Красный" and int(roll_result) in red_numbers:  # совпадение по красному цвету
        user3_account += user3_money_per_bet / 100 * 50
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    elif user3_bet == "Черный" and int(roll_result) in black_numbers:  # совпадение по черному цвету
        user3_account += user3_money_per_bet / 100 * 50
        print(f"{user3_name}, Вы выиграли! Ваш текущий счет: ", user3_account)
    else:
        user3_account -= user3_money_per_bet
        print(f"{user3_name}, Вы проиграли! Ваш текущий счет: ", user3_account)
    # счетчик возрастает на 1, если все ставки сделаны и у всех игроков есть деньги
    game_cycle += 1
