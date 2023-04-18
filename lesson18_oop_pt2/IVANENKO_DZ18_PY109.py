# TOMATO
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1)
# _index - передается параметром и 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
# TOMATOBUSH
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его
# основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри
# динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап
# созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
#
# GARDENER
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name -
# передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является
# protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться
# более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

class Tomato:
    states = {1: "Молочная зрелость", 2: "Розовая зрелость", 3: "Красная зрелость"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f"Томат №{self._index} в стадии: {self.states[self._state]}")

    def is_ripe(self):
        return self._state == 3


class TomatoBush:

    def __init__(self, tomatoes_quantity):
        self.tomatoes = []
        for tomato in range(1, tomatoes_quantity + 1):
            self.tomatoes.append(Tomato(tomato))

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
            else:
                return True

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Садовник работает")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Все томаты созрели. Идет сбор...")
            self._plant.give_away_all()
            print("Плодов для сбора не осталось.")
        else:
            print("Не все томаты созрели!")

    @staticmethod
    def knowledge_base():
        print(f"""
Справочник садовода {gardener.name}:
1. Рано вставайте
2. Поливайте помидоры
3. Проверяйте, достаточно ли помидорам тепла и солнечного света
4. Держите свой серп в заточенном состоянии
5. Терпеливо ждите зрелости помидоров
Текущее количество томатов на кусте: {len(gardener._plant.tomatoes)} шт.
        """)


if __name__ == "__main__":
    tomato_bush = TomatoBush(3)
    gardener = Gardener("Bob", tomato_bush)
    Gardener.knowledge_base()

    gardener.harvest()

    gardener.work()
    gardener.work()
    gardener.work()

    gardener.harvest()

    gardener.work()

    gardener.harvest()

    Gardener.knowledge_base()
