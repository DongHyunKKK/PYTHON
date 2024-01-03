# 1

my_city = '대구'
my_blood = 'A형'
my_season = '봄'
my_height = '180cm'
my_number = '010-9974-1376'
my_nationality = '대한민국'

# 2

mbti = 'INFP'
blood = 'A'
gender = 'M'
height = 171.7
weight = 77

print('[ 신상 정보 ]', '\n', 'MBTI :', mbti, '혈액형 :', blood, '성별 :', gender, '\n', '몸무게 :', weight, '키 :', height)
print()
print('[신상 정보] \n MBTI : %s  혈액형 : %s  성별 : %s \n 몸무게 : %d 키 : %f' %(mbti, blood, gender, weight, height))
print()
print(f'[신상 정보]\nMBTI : {mbti}  혈액형 : {blood}  성별 : {gender}\n몸무게 ; {weight}  키 : {height}')
print()

# 3-1

print(f'데이터 50 ==> {type(50)} 타입')
print(f'데이터 0.91 ==> {type(0.91)} 타입')
print(f'데이터 Winter ==> {type("Winter")} 타입')
print(f'데이터 False ==> {type(False)} 타입')
print()

# 3-2

season = input('[질문] 좋아하는 계절은? ')
print(f'당신은 {season}을 좋아하는 군요!')
print()
english = input('봄은 영어로? ')
print(f'봄은 {english}입니다.')

# 4

'''
힙 영역
스택 영역
'''

# 5-1

'''
int
float
str
bool
'''

# 5-2

'''
2진수
8진수
16진수
'''

# 6

width = int(input('직육면체 가로길이(cm) : '))
length = int(input('직육면체 세로길이(cm) : '))
height = int(input('직육면체 높이길이(cm): '))

print(f'직육면체 겉넓이 : {2 * (width * length + length * height + height * width)}')
print(f'직육면체 부피 : {width * length * height}')