# [실습]
# - 문자열 여러 개와 실수 여러 개를 입력 받기 => input() 1개만 사용
# - 첫 번째 입력 받은 값은 key
# - 두 번째 입력 받은 값은 value
# - 딕셔너리로 저장해 주세요.

data = input('문자열과 실수 여러 개 입력\n문자열과 실수 개수 동일 (예 : aa bb cc, 1.1 2.2 3.3) : ')

# 입력 형식이 맞을 경우만 딕셔너리에 저장
# - (1) 입력 ' , ' 문자열 안에 ',' 존재해야 함
# - (2) 문자열과 실수 개수가 동일 해야 함
if ',' in data:
    # dataList = data.split(',')
    # key = dataList[0].split()
    # value = dataList[1].split()
    key, value = data.split(',')
    key = key.split()
    value = value.split()
    dataDict = {}
    if len(key) == len(value):
        for num in range(len(key)):
            dataDict[key[num]] = float(value[num])
        print(f'dataDict : {dataDict}')
    else:
        print('정확한 형식이 아닙니다.')
else:
    print('정확한 형식이 아닙니다.')

# ---------------------------------------------------------------------
# 내장함수 zip()
# ---------------------------------------------------------------------
x = [1, 2, 3, 4, 5]
y = [11, 22, 33, 44, 55]
z = [111, 222, 333, 444, 555]

result = zip(x, y, z)
print(f'result => {type(result)}, {list(result)}')

if ',' in data:
    # dataList = data.split(',')
    # key = dataList[0].split()
    # value = dataList[1].split()
    key, value = data.split(',')
    key = key.split()
    value = value.split()
    dataDict = {}
    if len(key) == len(value):
        dataDict2 = dict(zip(key, value))
        print(f'dataDict2 : {dataDict2}')
    else:
        print('정확한 형식이 아닙니다.')
else:
    print('정확한 형식이 아닙니다.')

# ---------------------------------------------------------------------
# 반복문과 내장 함수 => map(), zip() 
# ---------------------------------------------------------------------

xList = ['1', '3', '5', '7']

# xList 안에 모든 원소를 정수 int로 변환 후 저장하기.
for idx in range(len(xList)):
    xList[idx] = int(xList[idx])

print(f'xList => {xList}')

# ---------------------------------------------------------------------
# 시퀀스 또는 반복이 가능한 객체의 요소/원소에 적용 후 값을 다시 저장 해야 하는 경우
# 자주 사용 되는 기능 으로 내장 함수로 제공 => map()
# - 문법 : map(함수명, 시퀀스 또는 반복이 가능한 객체
# ---------------------------------------------------------------------
# int 요소인 xList를 str 요소 변환
result = list(map(str, xList))
print(f'result => {result}')
print(f'xList => {xList}')

result = list(map(bool, xList))
print(f'result => {result}')
print(f'xList => {xList}')

# ---------------------------------------------------------------------
# list 데이터를 dict 데이터로 생성
# ---------------------------------------------------------------------
x = ['std01', 'std02', 'std03']
y = [90, 100, 99]

# 방법 (1) --> 기호/부호 {}
xyDict = {}
xyDict['std01'] = 90
xyDict['std02'] = 100
xyDict['std03'] = 99

for idx in range(len(x)):
    xyDict[x[idx]] = y[idx]

# 방법 (2) --> dict() 생성자 함수
xyDict2 = dict()
xyDict['std01'] = 90
xyDict['std02'] = 100
xyDict['std03'] = 99

for idx in range(len(x)):
    xyDict2[x[idx]] = y[idx]

# 방법 (3) --> dict() 생성자 함수
xy = []
for idx in range(len(x)):
    xy.append((x[idx], y[idx]))

xyDict3 = dict(xy)
print(xyDict3)

# 방법 (4) --> dict([(키1, 값1), (키2, 값2), ......, (키n, 값n)]) 생성자 함수
# By 내장 함수 zip()
xyDict = dict(zip(x, y))
print(xyDict4)