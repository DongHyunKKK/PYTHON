# 26.8
a = list(range(1, 101))[2::3]
b = list(range(1, 101))[4::5]

print(set(a) & set(b))

# 26.9
int1, int2 = map(int, input('양의 정수 두 개 입력 : ').split())

a = {i for i in range(1, int1+1) if int1 % i == 0}
b = {i for i in range(1, int2+1) if int2 % i == 0}

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
