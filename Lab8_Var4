num_list = list(map(int, input("Введите числа: ").split()))
count = 0
max_len = []

for el in num_list:
    if el > 0:
        count += 1
    else:
        max_len.append(count)
        count = 0

if count > 0:
    max_len.append(count)

print(max(max_len))
