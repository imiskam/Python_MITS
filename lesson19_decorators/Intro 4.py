from datetime import datetime


def count_the_time(arg):
    print(f"{arg} - аргумент декоратора count_the_time")

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result

        return wrapper

    return outer

@count_the_time("qweqweqwe")
def create_list_gen(k):
    list_ = [i for i in range(k) if i % 2 == 0]
    return list_

ex = create_list_gen(15)
