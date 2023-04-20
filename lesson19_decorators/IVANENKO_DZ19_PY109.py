# Задание 1
# Напишите декоратор, который будет считать, сколько раз была вызвана
# декорируемая функция

def decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@decorator
def return_true():
    return True


return_true()
return_true()
return_true()
return_true()
return_true()

print("Кол-во вызовов функции:", return_true.count)


#########################################################

# Домашнее задание
# Напишите декоратор debug, который при каждом вызове
# декорируемой функции выводит её имя (вместе со всеми
# передаваемыми аргументами), а затем — какое значение
# она возвращает. После этого выводится результат её
# выполнения

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция '{func.__name__}' и ее аргументы {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция '{func.__name__}' возвращает {result}")
        return result

    return wrapper


@debug
def multiply(x, y):
    return x * y


multiply(5, y=10)
multiply(5, 5)
