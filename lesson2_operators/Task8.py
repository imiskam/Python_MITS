import random

rand = random.randint(100, 999)
print(rand)

int1 = rand // 100
print(int1)
int2 = (rand // 10) % 10
print(int2)
int3 = rand % 10
print(int3)
result = int1 + int2 + int3
print(result)