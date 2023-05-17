# определение метода __next__ в классах
# создадим свой класс range
class Xrange:
    def __init__(self, start=0.0, stop=0.0, step=0.0):
        self.start = start  # начало последовательности
        self.stop = stop  # конец последовательности
        self.step = step  # шаг последовательности
        self.value = self.start - self.step  # получим первое значение последовательности

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


example = Xrange(3, 6, 1)
print(example.__next__())
print(next(example))
print(next(example))
# print(next(example))  # >>> StopIteration

"""
Теперь, давайте попробуем проитерироваться по нашему объекту
"""
for _ in example:
    print(_)

"""
Мы получили ошибку о том, что переданный для цикла for
объект не является итерабельным. 
Связано это с тем, что в нашем классе не определен 
метод __iter__.
"""
