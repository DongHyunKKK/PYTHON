# 1 ~ 10
nums = list(range(1, 11))
for n in nums:
    print(n, end = ' ' if n != 5 else '\n')

print()

for num in range(1, 6):
    print('*' * num)

for num in range(6, 0, -1):
    print('*' * num)

print()

for num in range(1, 12):
    if num <= 6:
        print('*' * num)
    else:
        print('*' * (12 - num))

print()

for num in range(1, 12):
    if num <= 6:
        print(' ' * (6 - num) + '*' * (2 * num - 1) + ' ' * (6 - num))
    else:
        print(' ' * (num - 6) + '*' * ((-2) * (num - 6) + 11) + ' ' * (num - 6))

