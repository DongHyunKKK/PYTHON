# ---------------------------------------------------------------
# set 데이터 타입
# - 제일 마지막에 추가된 타입
# - 목적 : 중복 데이터 제거
# - 특징 : 이미 존재하는 데이터는 저장하지 않음!
# - 문법 : {데이터1, 데이터2, ......, 데이터N}
# ---------------------------------------------------------------
# 빈 데이터 타입 생성
alist = []
aTuple = ()
aDict = {}
aSet = set()
aStr = ''

print(f'alist => {type(alist)}, {len(alist)}개')
print(f'aTuple => {type(aTuple)}, {len(aTuple)}개')
print(f'aDict => {type(aDict)}, {len(aDict)}개')
print(f'aSet => {type(aSet)}, {len(aSet)}개')
print(f'aStr => {type(aStr)}, {len(aStr)}개')

print('-' * 50)

# 생성자 함수 => 타입 이름과 동일한 함수명
# - 힙 영역에 메모리 공간을 잡고 데이터 초기화 기능 수행
alist = list()
aTuple = tuple()
aDict = dict()
aSet = set()
aStr = str()

print(f'alist => {type(alist)}, {len(alist)}개')
print(f'aTuple => {type(aTuple)}, {len(aTuple)}개')
print(f'aDict => {type(aDict)}, {len(aDict)}개')
print(f'aSet => {type(aSet)}, {len(aSet)}개')
print(f'aStr => {type(aStr)}, {len(aStr)}개')

# ---------------------------------------------------------------
# set 타입의 데이터 생성
# ---------------------------------------------------------------
a1 = {1, 1, 2, 3, 4, 5, 1, 1, 1, 1}
a2 = [1, 1, 2, 3, 4, 5, 1, 1, 1, 1]

print(f'a1 => {type(a1)}, {len(a1)}개, {a1}')
print(f'a2 => {type(a2)}, {len(a2)}개, {a2}')

# 다른 데이터 타입에서 중복 데이터 제거 시에 활용 => 형변환
a2 = list(set(a2))
print(f'a2 ==> {type(a2)}, {len(a2)}개, {a2}')

# ---------------------------------------------------------------
# set 타입의 연산 수행
# ---------------------------------------------------------------
a1 = {1, 3, 5, 1, 2}
b1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 연산 수행 ==> 형변환 후 수행
a1 = list(a1)
b1 = list(b1)
print(a1*2)

# ---------------------------------------------------------------
# 원소/요소 읽기/수정/삭제/추가 ==> 인덱스 x, 키 x ==> 메서드 제공
# ---------------------------------------------------------------
# 원소/요소 추가  ==> 1개 추가 : add() 메서드
a1 = {1, 3, 5, 1, 2}
a1.add(10)
a1.add(10)
print(f'a1 ==> {type(a1)}, {len(a1)}개, {a1}')

a1.add('A')
print(f'a1 ==> {type(a1)}, {len(a1)}개, {a1}')

# 여러개의 원소/요소 추가 => update() 메서드
a1.update([11, 22, 33, 44])
print(f'a1 ==> {type(a1)}, {len(a1)}개, {a1}')

a1.update('Good Luck!!')
print(f'a1 ==> {type(a1)}, {len(a1)}개, {a1}')

a1.add('Good Luck!!')
print(f'a1 ==> {type(a1)}, {len(a1)}개, {a1}')

# 원소/요소 삭제
a1.remove('G')
print(f'[remove] a1 ==> {type(a1)}, {len(a1)}개, {a1}')

a1.discard('G')
print(f'[discard] a1 ==> {type(a1)}, {len(a1)}개, {a1}')

# 원소/요소 꺼내기
data = a1.pop()
print(f'a1 ==> {data}, {type(a1)}, {len(a1)}개, {a1}')

# ---------------------------------------------------------------
# 집합에 관련된 메서드와 기호 / 연산자
# ---------------------------------------------------------------

# 교집합
# - 여러 개의 집합에 공통으로 존재하는 데이터만 추출
# - 기호 / 연산자 : &
# - 메서드 : intersection()

a1.clear()
a1.update('Happy')
print(f'a1 => {a1}')

a2 = a1.intersection({'a', 'A', 'b', 'B'})
print(f'a2 => {a2}')
print(f'a2 => {a2}', a1 & {'a', 'A', 'b', 'B'})

# 합집합
# - 여러 개의 집합에 공통으로 존재하는 데이터만 추출
# - 기호 / 연산자 : &
# - 메서드 : intersection()

a2 = a1.union({'a', 'A', 'b', 'B'})
print(f'a2 =>{a2}', a1 | {'a', 'A', 'b', 'B'})

# 차집합
# - 여러 개의 집합에서 중복은 1개만 포함한 모든 원소의 집합
# - 기호/연산자 : - 뺄셈 연산다
# - 메서드 : difference()

a2 = a2.difference({'a', 'A', 'b', 'B'})
print(f'a2 => {a2}', a1 - {'a', 'A', 'b', 'B'})

a3 = {'a', 'A', 'b', 'B'}.difference(a1)
print(f'a3 = > {a3}', {'a', 'A', 'b', 'B'} - a1)

# 정렬

# => 원소 값을 서로 비교해서 작은 데이터 >> 큰 데이터 순서로 저장 => 오름차순 정렬
# => 원소 값을 서로 비교해서 큰 데이터 >> 작은 데이터 순서로 저장 => 내림차순 정렬
# => set 타입에는 정렬 메서드 없음 ==> 내장함수 sorted()

a1 = sorted(a1)
print(f'a1 => {type(a1)}, {a1}')