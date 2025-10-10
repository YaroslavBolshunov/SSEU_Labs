n = int(input("N = "))
s = 0

while n != 0:
    x = int(input("число: "))
    if x > 0:
        s += x
    n -= 1

print(s)
