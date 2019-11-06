import math
import random
x = 0
y = 0

while y != 5:
    x += 1
    y = math.trunc(random.randrange(0, 25))
print(f'it took {x} itterations to reach 5')