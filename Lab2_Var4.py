import math

for i in range(10, 91, 5):
    x = i/100
    y = 5 ** math.asin(x/2) - math.log(x * math.sin(x), 5)
    print(x, y)
