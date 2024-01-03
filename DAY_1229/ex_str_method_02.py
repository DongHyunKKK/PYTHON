# ---------------------------------------------------------------
# [실습 2] 파일명을 입력 받은 후 아래 코드를 작성하세요.
# - 입력 받은 파일이 text 파일 여부 검사  ==> 확장자 txt
# - 입력 받은 파일이 jpg 파일 여부 검사  ==> 확장자 jpg
# - 입력 받은 파일이 py 파일 여부 검사  ==> 확장자 py
# ---------------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index()
# - 왼쪽 ---> 오른쪽, 제일 먼저 발견되는 문자의 인덱스를 반환
# - 존재 하지 않는 str 인덱스 찾으면 Error 발생
# ---------------------------------------------------------------
data = 'Merry Christmas!'
#       012345678901234
print(f"data.index('C') => {data.index('C')}")
print(f"data.index('r') => {data.index('r')}")

first_r = data.index('r')  # 0번 원소부터 하나씩 검사하여 'r'에 해당 하는 인덱스 찾기
second_r = data.index('r', first_r +1)  # 첫 번째 'r' 인덱스 이후 원소부터 하나씩 검사하여 'r'에 해당 하는 인덱스 찾기
third_r  = data.index('r', second_r + 1)  # 두 번째 'r' 인덱스 이후 원소부터 하나씩 검사하여 'r'에 해당 하는 인덱스 찾기
print(f"data.index('r', first_r + 1) => {data.index('r', first_r + 1)}")

# !의 인덱스를 찾기
print(f"data.index('!') => {data.index('!')}")

# ---------------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => find()
# - 왼쪽 ---> 오른쪽, 제일 먼저 발견되는 문자의 인덱스를 반환
# - 존재 하지 않는 str 인덱스 찾으면 -1을 반환
# ---------------------------------------------------------------
# !의 인덱스를 찾기
print(f"data.find('!') => {data.find('!')}")
print()
# ---------------------------------------------------------------
# str 데이터에서 문자열을 분리해 주는 메서드 => split()
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str로 분리
# - 반환값/결과값/리턴값 : 여러 개의 str을 담아서 리스트(List)로 변환
# ---------------------------------------------------------------
data = 'Happy New Year'

# str에서 공백을 기준으로 str 나누기
datas = data.split()
print(type(datas), datas)

# list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
print(f'datas[0] => {datas[0]}')
print(f'datas[1] => {datas[1]}')
print(f'data[-1] => {datas[-1]}')

juminNo = '123456-1234567'
#          01234567890123

birth = juminNo[ :6]
number = juminNo[7: ]
birth = juminNo[ :juminNo.index('-')]
print(birth)
print(number)
number = juminNo[juminNo.index('-') + 1: ]
juminNos = juminNo.split('-')
print(birth)
print(number)
print(juminNos)