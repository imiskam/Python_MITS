class Example:

    def __init__(self, x, y):
        # задаем инициализатор на получение
        # двух свойств x и y
        # указываем, что данные значения будут private
        self.__x = x
        self.__y = y

    # геттер
    # изменим геттер на получение значения x
    def get_x_value(self):
        return self.__x

    # сеттер
    def set_x_value(self, new_x):
        self.__x = new_x

    # используем свойство property для работы с изменением и установкой значений
    # для данного свойства
    # для свойства property имеется 2 основных параметра fget и fset
    # данные параметры нужны для передачи ссылки на методы геттеров и сеттеров
    old_value = property(get_x_value, set_x_value)


examp = Example(18, 24)

"""
# используя property теперь обращаясь к атрибуту old_value мы сможем получить и сразу изменить
# на новое значение свойство x
examp.old_value = 12
print(examp.old_value)
"""
print(examp.old_value)
examp.old_value = 12
print(examp.old_value)

