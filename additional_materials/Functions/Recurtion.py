def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(5) - factorial(4) - factorial(3) - factorial(2) - factorial(1))

"""

# на вход в нашу функцию подается атрибут в виде числа 5
# далее, условный оператор нам даёт True
# после чего функция переходит к нашему Return
# в return происходит операция
factorial(5):
    return n * factorial(n-1)
#   5 * factorial(4) # 120 (т.е. 5 * на результат factorial (4))
#   4 * factorial(3) # 24 (т.е. 4 * на результат factorial (3))
#   3 * factorial(2) # 6 (т.е. 3 * на результат factorial (2))
#   2 * factorial(1) # 2 (т.е. 2 * на результат factorial (1)
#   1 * factorial(0) # 1

"""
