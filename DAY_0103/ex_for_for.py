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

# 별표로 구성된 마름모
height = int(input('마름모 높이 : '))
half_height = int((height+1)/2)
for num in range(1, height+1):
    if num <= half_height:
        print(' ' * (half_height - num) + '*' * (2 * num - 1) + ' ' * (half_height - num))
    else:
        print(' ' * (num - half_height) + '*' * ((-2) * (num - half_height) + height) + ' ' * (num - half_height))


# 다른 풀이
col = int(input('가로 길이 : '))
row = int(input('세로 길이 : '))

for i in range(col):
    if i <= int((row-1)/2):
        print(f'{"*"*(int((col-1)/((row-1)/2))*(i+1) + 1 - int((col-1)/((row-1)/2))):^{col}}')
    else:
        print(f'{"*"*(int(-(col-1)/((row-1)/2))*(i-int((row-1)/2)) + col):^{col}}')

