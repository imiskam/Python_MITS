from functools import total_ordering


@total_ordering
class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            # если введенное слово содержит пробел
            # обрезаем символы до него
            word = word[:word.index(' ')]  # Теперь Word это все символы до первого пробела
            # с учетом того, что это строка
            # вызываем __new__ у класса str
        return str.__new__(cls, word)

    # определяет поведение оператора >
    def __gt__(self, other):
        return len(self) > len(other)


example = Word('Один два')
print(example > 'два')
print(example < 'два')
print(example == 'два')
print(example != 'два')
