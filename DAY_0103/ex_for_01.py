# 1 ~ 100 범위 에서 2의 배수로 구성된 리스트 생성
result = list(range(2, 101, 2))

# '24681012141618......100'
result = str(result)
print(result)
print(result[0], result[-6], result[-2], result[-1])

# int ==> str 형변환
# result[0] = str(result[0])
# result[1] = str(result[1])
# :
# result[-1] = str(result[-1])

# ---------------------------------------------------------------------
# 시퀀스 데이터 타입에서 원소/요소를 하나씩 빼서 반복 코드 수행 => for in 반복문
# ---------------------------------------------------------------------
# '24681012141618......100'
strNum = ''
for num in result:
    strNum = strNum + str(num)
print(f'strNum => {type(strNum)}\n{strNum}')

# ---------------------------------------------------------------------
# 리스트 안에 모든 원소를 str 타입으로 변환해서 저장
# ---------------------------------------------------------------------
# 데이터의 인덱스 범위 => 0 ~ len(data) - 1
print(f'[BEFORE] result => {result}')

result = list(range(2, 101, 2))
for idx in range(len(result)):
    result[idx] = str(result[idx])

print(f'[AFTER] result => {result}')