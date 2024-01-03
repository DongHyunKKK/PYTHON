# 16.5
x = [49, -17, 25, 102, 8, 62, 21]
for num in (x):
    print(num * 10, end = ' ')

print()
# 16.6
dan = int(input('dan : '))

if dan:
    for i in range(1, 10):
        print(f'{dan} * {i} = {dan * i}')
else:
    print('단을 다시 입력하세요.')

print()

# 19.5
for i in range(5):
    for j in range(5):
        if i > j:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

print()
for i in range(5, 0, -1):
    print(' ' * (5 - i) + '*' * i)

# 19.6
altitude = int(input('산의 높이 : '))
for num in range(1, altitude + 1):
    print(' ' * (altitude - num) + '*' * (2 * num - 1) + ' ' * (altitude - num))