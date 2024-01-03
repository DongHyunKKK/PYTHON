# [실습 1]
# 알고 싶은 단을 입력 받고 해당 단을 출력 하세요.
# - input()
# - 특정 단의 구구단을 출력 => 반복문 사용 하기

dan = int(input('단 입력 : '))

if dan:
    for i in range(1, 10):
        print(f'{dan} * {i} = {dan * i}')
else:
    print('정확한 단을 입력 하세요.')

print()

# 반대로 출력
if dan:
    for i in range(9, 0, -1):
        print(f'{dan} * {i} = {dan * i}')
else:
    print('정확한 단을 입력 하세요.')


print()

# 타이틀 없는 구구단 (1)
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} * {i} = {j * i:2d}', end = '  ')
    print()

# 타이틀 없는 구구단 (2)
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} * {i} = {j * i:2d}', end = '\n' if j == 9 else '   ')


# 타이틀 있는 구구단
for i in range(10):
    for j in range(2, 10):
        if i:
            print(f'{j} * {i} = {j * i:2d}', end = '\n' if j == 9 else '   ')
        else:
            print(f'---{j}단---', end = '\n' if j == 9 else '     ')