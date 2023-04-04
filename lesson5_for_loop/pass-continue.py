"""
CONTINUE - направляет Python на следующую итерацию цикла, минуя оставшееся тело(!) цикла после continue.
PASS - пропуск или бездействие c конкретным условием в цикле
"""

# CONTINUE
for i in range(5):
    if i < 3:
        continue
    if i % 2 == 0:
        print("C CONTINUE только", i)

# PASS
for i in range(5):
    if i < 3:
        pass
    if i % 2 == 0:
        print("C PASS только", i)

# CONTINUE
for i in range(5):
    if i > 2:
        continue
    print("CONTINUE", i)

# PASS
for i in range(5):
    if i > 2:
        pass
    print("PASS", i)
