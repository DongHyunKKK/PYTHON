# ---------------------------------------------------------------------
# for 요소 in 시퀀스/반복 가능한 객체:
# ==> for 인덱스 in range(len(변수)):
# ==> 내장 함수 enumerate()
# - (번호, 요소) 묶음 으로 반환함
# ---------------------------------------------------------------------

datas = ['Apple', 'Banana', 'Orange']

# 리스트 안에 요소/원소 데이터 추출
for data in datas:
    print(data)

# 리스트 안에 요소/원소 (인덱스, 데이터) 추출
for data in enumerate(datas):
    