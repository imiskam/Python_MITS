# Задание 1
# Создайте класс Example. В нём пропишите 3 (метода) функции. Две
# переменные задайте статически, две динамически.
# Первая функция: создайте переменную и выведите её
# Вторая функция: верните сумму 2-ух глобальных переменных
# Третья функция: верните результат возведения первой динамической
# переменной во вторую динамическую переменную
# Создайте объект класса.
# Напечатайте обе функции
# Напечатайте переменную a
class Example:
    static_value_1 = 1
    static_value_2 = 2

    def __init__(self, dynamic_value_1, dynamic_value_2):
        self.dynamic_value_1 = dynamic_value_1
        self.dynamic_value_2 = dynamic_value_2

    def print_value(self):
        value = 100500
        print(value)

    def get_sum_of_global_values(self):
        return self.static_value_1 + self.static_value_2

    def get_power_result(self):
        return self.dynamic_value_1 ** self.dynamic_value_2


example_1 = Example(2, 4)
example_1.print_value()
print(example_1.get_sum_of_global_values())
print(example_1.get_power_result())
print(Example.static_value_1)


#################################################################################

# Задание 2
# Создайте класс Калькулятор, где реализованы методы математических операций.
# А также функцию для ввода данных.

class Calculator:
    def __init__(self):
        self.num_1 = int(input("Введите число 1: "))
        self.num_2 = int(input("Введите число 2: "))

    def add(self):
        return self.num_1 + self.num_2

    def subtract(self):
        return self.num_1 - self.num_2

    def multiply(self):
        return self.num_1 * self.num_2

    def divide(self):
        if self.num_2 == 0:
            raise ZeroDivisionError("Деление на 0!")
        else:
            return self.num_1 / self.num_2


calc_operation_1 = Calculator()
calc_operation_1.add()
calc_operation_1.subtract()
calc_operation_1.multiply()
calc_operation_1.divide()

#################################################################################

# Домашнее задание
# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# 1. если произведение гласных и согласных букв меньше или равно длине слова - выводить все гласные.
# 2. иначе согласные.
# 3. если число - то произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Homework:
    def __init__(self):
        self.user_input = input("Введите данные: ")

    def execute_conditions(self):
        if self.user_input.isalpha():
            vowels = "aeiouAEIOU"
            consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
            vowels_list = [i for i in self.user_input if i in vowels]
            consonants_list = [j for j in self.user_input if j in consonants]
            multiplication_result = len(vowels_list) * len(consonants_list)
            if multiplication_result <= len(self.user_input):
                return f"Гласные: {''.join(vowels_list)}"
            elif multiplication_result > len(self.user_input):
                return f"Согласные: {''.join(consonants_list)}"
            else:
                raise ValueError("Неверный ввод данных!")

        elif self.user_input.isdigit():
            digits = [int(i) for i in str(self.user_input) if int(i) % 2 == 0]
            return sum(digits) * len(str(self.user_input))
        else:
            raise ValueError("Неверный ввод данных!")

    def get_length(self):
        if isinstance(self.user_input, str) or isinstance(self.user_input, int):
            return len(str(self.user_input))
        else:
            raise ValueError("Неверный тип данных!")


obj_1 = Homework()
print(obj_1.execute_conditions())
print(obj_1.get_length())
