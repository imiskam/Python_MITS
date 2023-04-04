import random

rand = str(random.randint(100, 999))
print("Рандомное число: ", rand)
int_1 = int(rand[0])
int_2 = int(rand[1])
int_3 = int(rand[2])
print(int_1 + int_2 + int_3)