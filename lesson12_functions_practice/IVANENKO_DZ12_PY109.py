import datetime


# 1

# масса (кг)/ рост^2 (м2)
def count_mass_index(weight, height):
    bmi = weight / (height / 100) ** 2
    if bmi >= 25:
        return "Вы имеете избыточный вес!"
    else:
        return "Ваш вес оптимален"


count_mass_index(60, 180)


# 2

def figure_type(*args):
    args_length = len(args)
    if args_length == 3:
        return "Треугольник"
    elif args_length == 4:
        if args[0] == args[1] == args[2] == args[3]:
            return "Квадрат"
        elif args[0] == args[2] and args[1] == args[3]:
            return "Прямоугольник"
        else:
            return "Четырехугольник"
    elif args_length == 5:
        return "Пятиугольник"
    elif args_length == 6:
        return "Шестиугольник"
    elif args_length == 7:
        return "Семиугольник"
    elif args_length == 8:
        return "Восьмиугольник"
    elif args_length == 9:
        return "Девятиугольник"
    elif args_length == 10:
        return "Десятиугольник"
    else:
        return "Тип фигуры неизвестен. Вы ввели меньше 3-х или больше 10-ти сторон!"


figure_type(4, 3, 3, 5, 7, 7)


# 3

def calculate_next_date(year, month, day):
    date = datetime.datetime(year, month, day).date()
    next_date = date + datetime.timedelta(days=1)
    return next_date


calculate_next_date(2000, 8, 31)


# 4 - ДОБАВЛЕНО РЕШЕНИЕ

def calculate_express_delivery(goods_count):
    goods_count -= 1
    return (goods_count * 2.95) + 10.95


print(f"Итоговая сумма доставки: ${calculate_express_delivery(4)}")


# 5

def reduce_numbers(num1, num2):
    # найти макс. делитель
    def find_max_division(num1, num2):
        if num2 == 0:
            return num1
        else:
            return find_max_division(num2, num1 % num2)

    # делить переменные на макс. делитель
    max_division_number = find_max_division(num1, num2)
    new_num1 = num1 // max_division_number
    new_num2 = num2 // max_division_number

    return new_num1, new_num2


reduce_numbers(6, 63)


# 6

def operate_list(list_):
    # 6.1
    list_.reverse()
    print(list_)
    # 6.2
    list_.sort(key=lambda x: (isinstance(x, str), x), reverse=True)
    print(list_)
    # 6.3
    list_.sort(key=lambda x: (isinstance(x, str), x))
    print(list_)
    # 6.4
    list_2_7 = list_[1:7]
    print(list_2_7)
    # 6.5
    list_.pop(9)
    print(list_)
    # 6.6
    list_ = set(list_)
    list(list_)
    print(list_)


operate_list([1, 2, 3, 4, 4, 5, 6, 9, "hi", "hello", "good morning"])


# 7

def count_range(list_, min_border, max_border):
    count = 0
    for i in list_:
        if min_border <= i < max_border:
            count += 1
    return count


print(count_range([1, 3, 5, 8, 19, 20, 21, 54, 77, 54], 5, 20))


# 8 - ДОБАВЛЕНО РЕШЕНИЕ

def count_sublists(list_):
    count = 0
    for obj in list_:
        if isinstance(obj, list):
            count += 1
            count += count_sublists(obj)
    return count


count_sublists([1, 2, 3, [4, 5, 6, [7, 8, 9]], ["hi", "hello", ["bye"]]])


# 9

# функция на проверку палиндрома (перепутал с анаграммой и написал сперва на него, решил оставить)
def is_palindrome(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    if str1[:] == str2[::-1]:
        return True
    else:
        return False


is_palindrome('live', 'evil')


# функция на проверку анаграммы
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    character_dictionary = {}

    # сравнение длины строк
    if len(str1) != len(str2):
        return False
    for character in str1:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    # сравнение одинакового кол-ва символов
    for character in str2:
        if character in character_dictionary:
            character_dictionary[character] -= 1
        else:
            return False
    # если проверки выше пройдены
    return True


is_anagram('вы бор', 'об рыв')


# 10 - ДОБАВЛЕНО РЕШЕНИЕ

def convert_text_to_numbers(entered_text):
    buttons = {"1": [".", ",", "?", "!", ":"],
               "2": ["A", "B", "C"],
               "3": ["D", "E", "F"],
               "4": ["G", "H", "I"],
               "5": ["J", "K", "L"],
               "6": ["M", "N", "O"],
               "7": ["P", "Q", "R", "S"],
               "8": ["T", "U", "V"],
               "9": ["W", "X", "Y", "Z"],
               "0": [" "]}

    for character in entered_text.upper():
        for key, value in buttons.items():
            if character in value:
                print(key * (value.index(character) + 1), end=" ")


entered_text = input("Введите текст: ")
convert_text_to_numbers(entered_text)


# 11 - ДОБАВЛЕНО РЕШЕНИЕ

def flatten_list(list_):
    result = []
    for obj in list_:
        if isinstance(obj, list):
            # метод extend здесь используется для распаковки объектов в корневой список
            result.extend(flatten_list(obj))
        else:
            result.append(obj)
    return result


flatten_list([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]])
