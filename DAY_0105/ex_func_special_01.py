# -----------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (1)
# 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명(*data)
#
# -----------------------------------------------------------
# 두 개의 정수를 덧셈하여 합계를 반환하는 함수
def addTwo(x, y):
    return x + y

# 3개의 정수를 덧셈하여 합계를 반환하는 함수
def addThree(x, y, z):
    return x + y + z

# 4개의 정수를 덧셈하여 합계를 반환하는 함수
def addFour(x, y, z, k):
    return x + y + z + k

# -----------------------------------------------------------
# 함수 기능 : 전달 받은 숫자를 모두 덧셈한 결과 반환 기능
# 함수 이름 : addNumber
# 매개 변수 : *nums
# 반 환 값 : 계산 결과
# -----------------------------------------------------------
def addNumber(*data):
    print(type(data))
    ret = 0
    for d in data:
        ret += d
    return ret

# 함수 사용 즉, 함수 호출
print(addNumber(1, 2, 3))
print(addNumber(10))
print(addNumber())
print(addNumber(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# *시퀀스/반복이 가능한 객체 => 내부에 모든 원소를 풀어서 하나씩 전달 : 언팩킹
print(addNumber(*range(1, 11)))

a = [11, 22, 33, 44]
aTuple = 'a', 'b', 'c'
aDict = {'name' : 'Hong', 'age' : 100}

print(a, aTuple, aDict)
print(*aTuple, sep = '-')
print(*aDict, sep ='-')  # *가 한 개이면 키만 출력
