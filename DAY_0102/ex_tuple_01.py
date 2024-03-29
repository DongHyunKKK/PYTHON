# ---------------------------------------------------------------
# 튜플(Tuple) : 읽기 전용의 리스트라고 함
# - 저장 후 수정, 삭제, 추가 변경 안됨!
# - 용도 : 변경 되어서는 안되는 데이터를 저장
# - 예시 : 성별, 주민번호, 국가코드, 프로그램 상에서 변경되면 안되는 데이터
# - 문법 : (데이터1, 데이터2, ......, 데이터n)
#          데이터1, 데이터2, ......, 데이터n
#         (데이터1,)        데이터1
# ---------------------------------------------------------------
# 튜플 데이터 생성
# 성별, 주민번호를 저장하기
myInfo = ('F', '123456-1234567')
#
print(f'{type(myInfo)}, {myInfo}')

# 성별 데이터 읽기
print(f'{type(myInfo)}, {myInfo[0]}')
print(f'{type(myInfo)}, {myInfo[-1]}')

# 성별 데이터 변경 ==> 여자 ---> 남자
# myInfo[0] = 'M' 변경 안됨

# 성별 데이터 삭제 안됨
# del myInfo[0]

# 튜플 ==> 리스트 형변환
myInfo = list(myInfo)
myInfo[0] = 'M'
myInfo[1] = myInfo[1].replace('2', '3', 1)

# 리스트 ==> 튜플
myInfo = tuple(myInfo)
print(myInfo)
# ---------------------------------------------------------------
# 1개 원소를 가진 튜플 생성
# ---------------------------------------------------------------
myData = '82'
print(f'type(myData) : {type(myData)}')

myData = ('82')
print(f'type(myData) : {type(myData)}')

myData = '82',
print(f'type(myData) : {type(myData)}')

myData = ('82',)
print(f'type(myData) : {type(myData)}')

a = [1, 2, 1, 1, 5, ['A', 'C'], 1, 1, ['A', 'C']]

print(a.count(1))
print(a.count(['A, C']))