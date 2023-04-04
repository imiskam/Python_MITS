# Задание 1
# В файле, в одну строку записаны слова и числа через пробел или _
# найти сумму всех чисел.

def find_sum_of_numbers(file):
    list_ = []
    for i in file:
        if i.isdigit():
            list_.append(int(i))
    return sum(list_)


with open("test.txt", encoding="UTF-8") as file:
    file1 = file.readline()
    print(f"Сумма всех чисел в текстовом документе: {find_sum_of_numbers(file1)}")


####################################################################

# Задание 2
# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по
# возрастанию, а потом слова по возрастанию их длины.

def sort_list(file):
    file1 = file.read().split()
    file2 = file1.copy()
    list_of_numbers = sorted(int(i) for i in file1 if i.isdigit())
    list_of_strings = sorted([i for i in file2 if i.isalpha()], key=len)
    return list_of_numbers + list_of_strings


with open("test2.txt", encoding="UTF-8") as file:
    print(f"Отсортированный список: {sort_list(file)}")


####################################################################

# Задание 3
# Создать текстовый файл, записать в него построчно данные, которые
# вводит пользователь. Окончанием ввода пусть служит пустая строка.

def write_entered_text(file):
    while True:
        textline_input = input("Введите строку, чтобы записать ее в файл (для выхода из программы нажмите Enter): ")
        file.write(textline_input + "\n")
        if textline_input == "":
            break


with open("test3.txt", "w", encoding="UTF-8") as file:
    write_entered_text(file)


####################################################################

# Задание 4
# В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.

def count_total_lines_and_characters(file):
    strings_number = 0
    for i in file:
        # Удалить символы перевода строки при чтении файла
        i = i.rstrip('\n\r')
        strings_number += 1
        print(f"Количество символов в строке {i} - {len(i)}")
    print(f"Количество строк - {strings_number}")


with open("test4.txt", "r", encoding="UTF-8") as file:
    count_total_lines_and_characters(file)


####################################################################

# Домашнее задание 1
# Есть массив состоящий из слов и чисел, нужно записать в
# файл сначала слова в порядке их длины, а после слов
# цифры в порядке возрастания

def write_sorted_words_then_numbers(list_, file):
    list_of_words = sorted([i for i in list_ if isinstance(i, str)], key=len)
    list_of_numbers = sorted(int(i) for i in list_ if isinstance(i, int))

    for word in list_of_words:
        file.write(word + " ")
    file.write("\n")

    for number in list_of_numbers:
        file.write(str(number))
        file.write(" ")


list_ = [2, 3, 1, "hi", "hello", 123, "bye"]

with open("test_dz1.txt", "w+", encoding="UTF-8") as file:
    write_sorted_words_then_numbers(list_, file)
