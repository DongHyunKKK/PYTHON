# ---------------------------------------------------------------------
# 컴프리헨션 (Comprehension)
# list Comprehension, Dict Comprehension, Set Comprehension
# ---------------------------------------------------------------------
# [실습 1] aList의 원소를 제곱한 값을 원소로 가지는 bList 생성
aList = [1, 2, 3, 4]

# for 문
bList = []
for a in aList:
    bList.append(a**2)

print(f'aList => {aList}\nbList => {bList}')

# 컴프리헨션
cList = [a**2 for a in aList]
print(f'cList => {cList}')

# [실습 2] aList의 원소 중에서 짝수만 제곱하여 모은 bList 생성
# for 문
bList2 = []
for a in aList:
    if not a % 2:
        bList2.append(a**2)

print(f'aList => {aList}\nbList2 => {bList2}')

# 컴프리헨션
cList2 = [a**2 for a in aList if not a % 2]
#         ---- -------------- ------------
#          (3)       (1)          (2)
# (2)에서 True인 경우에만 (1) 실행
print(f'cList2 => {cList2}')

# [실습 3] aList의 원소 중에서 짝수인 원소는 제곱, 홀수인 원소는 그대로 저장한 bList3 생성
# 일반적 for 방식

bList3 = []
for a in aList:
    if not a % 2:
        bList2.append(a**2)
    else:
        bList3.append(a)

print(f'aList => {aList}\nbList3 => {bList3}')

# 컴프리헨션
cList3 = [a**2 if not a % 2 else a for a in aList]
#         ---- ------------ ------ --------------
#         (3-T)     (2)     (3-F)       (1)
print(f'cList3 => {cList3}')