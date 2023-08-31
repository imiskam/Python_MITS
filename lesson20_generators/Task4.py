# 0 1 1 2 3 5 8 13 21
def fibo(start, end):
    a, b = 0, 1

    for i in range(start, end + 1):
        a, b = b, a + b  # A станет B, в B запишется результат A + B
        print(a)


fibo(1, 8)
