# -----------------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# -----------------------------------------------------------
# 함수 기능 : 팩토리얼 계산 후 계산 결과를 반환하는 기능
#           팩토리얼이란 3! = 3 * 2 * 1
# 함수 이름 : factorial
# 매개 변수 : n
# 반 환 값 : 계산 결과
# -----------------------------------------------------------
def factorial(n):
    fact = 1
    if fact:
        for i in range(1, n+1):
            fact *= i
    return fact

print(factorial(8))

print()
def factorial2(n):
    ret = 1
    if n:
        for i in range(n, 0 , -1):
            ret *= i
    return ret

print(factorial2(10))
print()
# -----------------------------------------------------------
# 함수 기능 : 팩토리얼 계산 후 계산 결과를 아래와 같이 반환하는 기능
#           예시 결과 3! = 3 * 2 * 1 = 6
# 함수 이름 : factorial3
# 매개 변수 : n
# 반 환 값 : 계산 str
# -----------------------------------------------------------
def factorial3(n):
    val = 1
    print(f'{n}! =', end = ' ')
    if n:
        for i in range(n, 0, -1):
            val *= i
            if i != 1:
                print(f'{i} *', end = ' ')
            else:
                print(f'{i} = {val}')

print(factorial3(5))
print()
def factorial4(n):
    strRet = f'{n}! = '
    intRet = 1
    if n:
        for i in range(n, 0, -1):
            intRet *= i
            strRet += str(i)
            strRet += ' * ' if i != 1 else ' = '

    strRet += str(intRet)
    return strRet

print(factorial4(1))
print(factorial4(7))

