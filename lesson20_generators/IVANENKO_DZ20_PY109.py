# Задание 1
# Напишите генератор, который на вход получает список чисел
# и возвращает только те числа, которые делятся на 3 без остатка.

list_ = [i for i in range(1, 20)]


def divide_by_3(numbers):
    for i in numbers:
        if i % 3 == 0:
            yield i


for i in divide_by_3(list_):
    print(i)


############################################

# Задание 2
# Напишите итератор (класс), который на вход получает строку и возвращает каждый второй символ этой строки

class Iterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.string):
            raise StopIteration
        char = self.string[self.index]  # получаем текущий элемент списка и сохраняем в переменную символа
        self.index += 2
        return char


for char in Iterator("Шла Саша по шоссе"):
    print(char)


############################################

# Задание 3
# Напишите генератор, который на вход получает два списка чисел и возвращает только те числа,
# которые есть в обоих списках.

def find_same_numbers(list_1, list_2):
    for i in list_1:
        if i in list_2:
            yield i


list_1 = [1, 2, 3, 4, 5]
list_2 = [1, 2, 3, 8, 9]

for i in find_same_numbers(list_1, list_2):
    print(i)


############################################

# Задание 4
# Напишите генератор, который на вход получает список строк и возвращает только те строки, которые содержат букву "a".

def find_strings_with_a(list_):
    for obj in list_:
        if "а" in obj.lower():
            yield obj


list_of_strings = ["сорокА", "воронА", "кАшу", "вАрила", "деток", "кормилА"]
list_of_strings_with_a = list(find_strings_with_a(list_of_strings))
print(list_of_strings_with_a)


############################################

# Задание 5
# Напишите генератор, который на вход получает список строк и возвращает только те строки, которые содержат букву "a".

class Iterator_2:
    def __init__(self, list_):
        self.list_ = list_
        self.index = 2  # начал с индекса 2, чтобы сразу получить 3-й элемент и не включать 1-й

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.list_):
            raise StopIteration
        result = self.list_[self.index]  # получаем текущий элемент списка и сохраняем в result
        self.index += 3
        return result


list_of_objects = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list_of_3rd_objects = Iterator_2(list_of_objects)
for obj in list_of_3rd_objects:
    print(obj)
