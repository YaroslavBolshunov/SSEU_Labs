import math

s = 0
for n in range(1, 21, 1):
    s += (0.5 ** 2 * n) / (n ** 2 + n) * math.sin(n)

print(s)
