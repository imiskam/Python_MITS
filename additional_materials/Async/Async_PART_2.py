import asyncio
import time


# объявляем асинхронную функцию fun1
async def fun1(x):
    print(x ** 2, 'быстрая часть функции fun1')
    # говорим интерпретатору не ждать, пока функция будет спать
    # таким образом эмитируем задержку в выполнении команды
    await asyncio.sleep(3)
    print('fun1 завершена')
    return 1


# объявляем асинхронную функцию fun2
async def fun2(x):
    print(x ** 0.5, 'быстрая часть функции fun2')
    # говорим интерпретатору не ждать, пока функция будет спать
    # таким образом эмитируем задержку в выполнении команды
    await asyncio.sleep(3)
    print('fun2 завершена')
    return 2


# объявляем асинхронную main-функцию для выполнения всех
# функций
async def main():
    """
    asyncio.create_task(coro, *, name=None)
    Параметры:
        coro - асинхронная функция coroutine,
        name=None - имя задачи.
        Функция create_task() модуля asyncio оборачивает сопрограмму coro в задачу task и планирует ее выполнение
        в ближайшее время. Возвращает объект Task. Объект задачи всегда следует запускать с оператором await.

    """
    # планируем выполнение задачи 1
    task1 = asyncio.create_task(fun1(4))
    # планируем выполнение задачи 2
    task2 = asyncio.create_task(fun2(4))

    await task1
    # print(task1)
    await task2
    # print(task2)


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))
