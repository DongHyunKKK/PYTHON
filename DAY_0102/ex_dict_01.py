# ---------------------------------------------------------------
# [질문] 5명 학생에 대한 학점을 저장 하기
# - 학생의 이름과 학점
# ---------------------------------------------------------------
# 방법1) 학생 이름 변수 5개 => stdName1 ~ stdName5
#       학점 변수 5개     => jumsu1 ~ jumsu5

stdName01 = 'std01'
stdName02 = 'std02'
stdName03 = 'std03'
stdName04 = 'std04'
stdName05 = 'std05'

stdJumsu01 = 90
stdJumsu02 = 89
stdJumsu03 = 100
stdJumsu04 = 76
stdJumsu05 = 34

# 방법2) 학생 이름 변수 5개 => stdNames = [학생 이름1, ......, 학생 이름5]
#       학점 변수 5개     => stdJumsus = [점수1, ......, 점수5]

stdNames = ['std01', 'std02', 'std03', 'std04', 'std05']
stdJumsus = [90, 89, 100, 76, 34]

# => 학번03 학생의 학번과 점수를 출력
idx = stdNames.index('std03')

print(f'{stdNames[idx]}학번 학생의 점수 {stdJumsus[idx]}')

# 방법3) 학생 이름 변수 5개 => stdNames = [학생 이름1, ......, 학생 이름5]
#       학점 변수 5개     => stdJumsus = [점수1, ......, 점수5]

stdNumsJumsu = [['std01', 90], ['std02', 89], ['std03', 100], ['std04', 76], ['std05', 34]]

# ---------------------------------------------------------------
# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# - 형태 => 키 : 데이터   (예 : 주민번호 : 이름, 학번 : 전공)
# - 조건 : 키는 중복되면 안됨
# - 문법 : {키1 : 데이터1, 키2 : 데이터2, ......, 키N : 데이터N}
# ---------------------------------------------------------------
stdNumsJumsu = {'std01' : 90, 'std02' : 89, 'std03' : 100, 'std04' : 76, 'std05' : 34}
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {type(stdNumsJumsu)}, {stdNumsJumsu}')

# 원소 읽는 방법 => 변수명[키]
print(f'stdNumsJumsu["std03"] => {stdNumsJumsu["std03"]}')

# 마지막 원소 지정하는 -1 사용 ==> -1에 대한 키가 없으면 ERROR
# print(f'stdNumsJumsus[-1] => {stdNumsJumsu[-1]}')

# ---------------------------------------------------------------
# 원소/요소 추가 방법 => 변수명[새로운 키] = 데이터
# ---------------------------------------------------------------
# 학번 10인 학생의 점수 99.8 저장 즉 추가하기
stdNumsJumsu['std10'] = 99.8
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개 {stdNumsJumsu}')

# 학번 10인 학생의 점수 99로 변경
stdNumsJumsu['std10'] = 99
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개 {stdNumsJumsu}')

# ---------------------------------------------------------------
# 원소/요소 데이터 삭제 => del 변수명[키] 또는 del(변수명[키])
# ---------------------------------------------------------------
del stdNumsJumsu['std10']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개 {stdNumsJumsu}')

del stdNumsJumsu['std02']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개 {stdNumsJumsu}')

