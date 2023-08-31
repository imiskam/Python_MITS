# Пример 2

def decorator(func):
    def wrapper():
        print("Идет поиск кандидата...")
        print("Кандидат найден")
        print("Идет собеседование...")
        print("Собеседование пройдено")
        func()
        print("Кандидат нанят")

    return wrapper


@decorator
def hire():
    print("Нанимаем кандидата...")


hire()

# Вариант 2 без синтаксического сахара
# f = decorator(hire)
# f()