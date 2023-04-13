import csv
from datetime import datetime

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


#################################################################################

# Дополнительное домашнее задание:
# 1. Создать класс "Сотрудник"
# 2. Определить атрибуты класса: имя, фамилия, должность, зарплата
# 3. Определить конструктор класса для инициализации атрибутов
# 4. Реализовать методы для изменения и получения значений каждого атрибута
# 5. Реализовать метод для вывода информации о сотруднике на экран
# 6. Создать несколько объектов класса "Сотрудник"
# 7. Продемонстрировать работу методов на созданных объектах
#
# Расширение задачи:
# 8. Добавить в класс "Сотрудник" метод для изменения зарплаты на заданное значение
# 9. Добавить в класс "Сотрудник" метод для увеличения зарплаты на заданное процентное значение
# 10. Добавить в класс "Сотрудник" метод для сравнения зарплаты текущего объекта
# с зарплатой другого объекта класса "Сотрудник"
# 11. Продемонстрировать работу новых методов на созданных объектах.
#
# **** реализовать метод, который будет записывать в CSV-файл изменение зарплаты по сотруднику
# (в момент изменения зарплаты - создается запись в CSV)

class Employee:
    def __init__(self, name, surname, position, salary):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        with open("salary_changes_list.csv", "a", encoding="UTF-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            changed_salary_date = datetime.now()
            self.salary = salary
            writer.writerow([self.name, self.surname, self.salary, changed_salary_date])

    # Функция записывает в файл изменение зарплаты в процентах
    def set_salary_by_percents(self, percent):
        with open("salary_changes_list.csv", "a", encoding="UTF-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            changed_salary_date = datetime.now()
            self.salary = self.salary * (1 + percent / 100)
            writer.writerow([self.name, self.surname, self.salary, percent, changed_salary_date])

    def get_full_employee_info(self):
        return self.name, self.surname, self.position, self.salary

    def compare_employees_salary(self, employee):
        # Процентная разница = (a/b-1)*100, где a = Большее число, b = Меньшее число
        salary_difference_in_percent = abs((self.salary / employee.get_salary() - 1) * 100).__round__(1)
        print(f"Зарплата {self.name} - {self.get_salary()}")
        print(f"Зарплата {employee.name} - {employee.get_salary()}")
        if self.get_salary() > employee.get_salary():
            print(f"Зарплата {self.name} больше, чем у {employee.name} на {salary_difference_in_percent}%")
        elif self.get_salary() < employee.get_salary():
            print(f"Зарплата {self.name} меньше, чем у {employee.name} на {salary_difference_in_percent}%")
        else:
            print(f"Зарплата {self.name} такая же, как у {employee.name}")


# Создание экземпляров класса
employee_1 = Employee("George", "Washington", "Senior Python Developer", 1000)
employee_2 = Employee("Abraham", "Lincoln", "Junior PHP Developer", 500)

# Вызовы методов
employee_1.get_salary()
employee_1.set_salary(1300)
employee_1.get_full_employee_info()

employee_2.get_position()
employee_2.set_position("Middle PHP Developer")
employee_2.get_full_employee_info()

employee_1.set_salary_by_percents(15)
employee_1.get_salary()
employee_2.set_salary_by_percents(20)
employee_2.get_salary()

employee_2.compare_employees_salary(employee_1)
