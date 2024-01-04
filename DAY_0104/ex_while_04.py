# ---------------------------------------------------------------------
# continue => 계속해서~
# - 키워드 아래 코드 실행 안됨
# - 반복 상단으로 이동
# ---------------------------------------------------------------------

# 1 ~ 30으로 구성된 리스트 생성
numList = list(range(1, 31))

# 리스트의 요소 중에서 짝수만 화면에 출력하기
for data in numList:
    if not data % 2:
        print(data)

for data in numList:
    if data % 2:
        continue
    print(data)

# while
idx = 0
while idx < 30:
    if numList[idx] % 2 == 0:
        print(f'{idx}번째 요소 값 : {numList[idx]}')
    idx += 1

idx = -1
while idx < 29:
    idx += 1
    if numList[idx] % 2:
        continue
    print(f'{idx}번째 요소 값 : {numList[idx]}')