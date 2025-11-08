N = int(input("N = "))
list = list(map(float, input("Введите числа: ").split()))

m = int(input("m = "))

current_sum = sum(list[:m])
max_sum = current_sum


for i in range(1, N - m + 1):
    current_sum = current_sum - list[i - 1] + list[i + m - 1]
    if current_sum > max_sum:
        max_sum = current_sum


print(max_sum)
