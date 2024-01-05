# 29.7
x = 10
y = 3
def get_quotient_remainder(x, y):
    return x // y, x % y

quotient, remainder = get_quotient_remainder(x, y)
print('몫 : {0}, 나머지 : {1}'.format(quotient, remainder))

# 29.8
x, y = map(int, input('두 숫자를 입력하세요 : ').split())

def calc(x, y):
    return x + y, x - y, x * y, x / y if y != 0 else 'y는 0이 아니어야 합니다.'

a, s, m, d = calc(x, y)
print(f'덧셈 : {a}, 뺄셈 : {s}, 곱셈 : {m}, 나눗셈 : {d}')