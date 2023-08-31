# 1. Создайте класс Human.
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и
# age. Для этих параметров задайте значения по умолчанию, используя свойства
# default_name и default_age. В методе __init__() определите четыре свойства:
# Публичные - name и age. Приватные - money и house.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, house и
# money.
# 5. Реализуйте справочный статический метод default_info(), который будет выводить
# статические поля default_name и default_age.
# 6. Реализуйте метод earn_money(), увеличивающий значение свойства money.

class Human:
    default_name = "Joe"
    default_age = 30

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = False

    def info(self):
        return self.name, self.age, self.__money, self.__house

    @staticmethod
    def default_info():
        return Human.default_name, Human.default_age

    def earn_money(self, money):
        self.__money += money


human_1 = Human("John", "50")
human_1.earn_money(500)
Human.default_info()

