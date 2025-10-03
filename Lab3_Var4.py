import math

x = -5

while x <= 5:
    if x <= 0:
        y = x ** 3 * math.cos(x)
    if (x > 0) and (x <= (math.pi / 4)):
        y = math.asin(x) ** math.acos(x)
    if x > math.pi/4:
        y = math.log(x + 1, math.e) ** math.log(x + 1, math.e)

    print(x, y)
    x += 0.5



