# 1
msg = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']

def string_sort(word_list):
    sort_word = sorted(word_list, reverse = True)
    print(f'정렬 결과 : {sort_word}')
    print(f'가장 높은 문자열 : {sort_word[0]}, 가장 낮은 문자열 : {sort_word[-1]}')

string_sort(msg)

# 2
data_input = input('데이터 입력 : ')
data_list = data_input.split()
num_list = [data for data in data_list if data.isnumeric()]

num_list = list(map(int, num_list))
print(f'합계 : {sum(num_list)}, 최댓값 : {max(num_list)}, 최솟값 : {min(num_list)}')

# 3
while True:
    str_num = input('알파벳 혹은 숫자를 입력하세요 : ')
    if str_num != 'q' and str_num.isalpha():
        print('♤')
        if str_num == 'Q':
            break
    elif str_num != 'Q' and str_num.isalpha():
        print('♠')
        if str_num == 'q':
            break
    elif str_num.isnumeric():
        print('◎'*int(str_num))

# 4
multiples_3 = [num for num in range(3, 101, 3)]
multiples_7 = [num for num in range(7, 101 ,7)]
multiples_8 = [num for num in range(8, 101, 8)]

print(set(multiples_3 + multiples_7 + multiples_8))

# 5
def bin_word(string):
    string = string.replace(' ', '')
    letter_list = list(string)
    hex_incoding = ''
    binary_incoding = ''
    for letter in letter_list:
        hex_incoding += hex(ord(letter))
        binary_incoding += bin(ord(letter))
    print(f'"{string}"의 인코딩 : {hex_incoding}\n"{string}"의 인코딩 : {binary_incoding}')

string = '가나다'
bin_word(string)

# print(hex(ord('가'))+hex(ord('나')))
# print(hex(ord('나')))
# print(hex(ord('다')))

# data = ' 2024 apple '
# s= data.replace(' ', '')
# data = list(s)
# print(s)

# 6
def sort_list(datas, n):
    n_letters = []
    for data in datas:
        if len(data) <= n:
            print('데이터를 다시 입력하세요.')
        else:
            n_letters.append(data[n])
    print(n_letters)
    sort_letters = sorted(n_letters)
    print(sort_letters)
    sort_datas = []
    ind = 0
    for letter in sort_letters:
        if datas[n_letters.index(letter)] in sort_datas:
            sort_datas.append(datas[n_letters.index(letter, ind, len(n_letters) + 1)])
            ind += 1
        else:
            sort_datas.append(datas[n_letters.index(letter)])

    for i in range(len(sort_datas)):
        for j in range(i + 1, len(sort_datas)):
            if sort_datas[i][n] == sort_datas[j][n]:
                if sort_datas[i] > sort_datas[j]:
                    sort_datas[i], sort_datas[j] = sort_datas[j], sort_datas[i]

    print(sort_datas)


sort_list(['askde', 'beach', 'surf'], 2)


# 7
def my_list(int_list):
    if 2 not in int_list:
        print([-1])
    else:
        # pos = [i for i in range(len(int_list)) if int_list[i] == 2]
        pos = [i for i, x in enumerate(int_list) if x == 2]
        print(int_list[pos[0] : pos[-1] + 1])


nums = [0, 1, 2, 4, 5, 2, 9, 3, 2, 8, 1]
#nums = [0, 0, 0]
#nums = [0, 1, 2, 4, 5, 3, 1, 7]
my_list(nums)

# 8
# num = [0, 1, 2]
# def my(*number):
#
#     print(number)  # (number,) : 원소 하나인 튜플
#     print(type(number))  # 튜플
# my(num)

nums = [-2, 3, 0, 2, -5]


# nums = [-3, -2, 1, 0, 1, 2, 3]

def zero_combination(nums):

    posi_nums = [num for num in nums if num >= 0]
    nega_nums = [num for num in nums if num < 0]
    # print(posi_nums)
    # print(nega_nums)

    posi_twoadd = [posi_nums[i] + posi_nums[j] for i in range(len(posi_nums)) for j in range(i + 1, len(posi_nums))]
    # print(posi_twoadd)

    nega_twoadd = [nega_nums[i] + nega_nums[j] for i in range(len(nega_nums)) for j in range(i + 1, len(nega_nums))]
    # print(nega_twoadd)

    num_combi = 0
    for add in posi_twoadd:
        if -add in nega_nums:
            num_combi += 1

    for add in nega_twoadd:
        if -add in posi_nums:
            num_combi += 1

    print(num_combi)


zero_combination(nums)

# 다른문제
def combi(num_list):
    if len(num_list) != 3:
        print('정수 리스트의 길이는 3이어야 합니다.')
    else:
        combi_num = 0
        if 0 in num_list:
            combi_num += 1
            for num in num_list:
                if num != 0:
                    if -num in num_list:
                        combi_num += 2
                        break
        else:
            for num in num_list:
                if num != 0:
                    if -num in num_list:
                        combi_num += 1
                        break

            if sum(num_list) == 0:
                    combi_num += 1

    print(combi_num)

print(combi([-7,0,7]))

# 9
dan = int(input('단 : '))

def gugudan(dan):


# 10
def sum_maxmin(string):
    string1 = string
    string = string.replace(',','')
    num_list = list(string)
    num_list = list(map(int, num_list))
    print(f'"{string1}"의 합 : {sum(num_list)}, 가장 큰 수 : {max(num_list)}, 가장 작은 수 : {min(num_list)}')

sum_maxmin('1,234')

# 11
import random
def biggo_game():
    ran_num = random.randint(1, 100)
    while True:
        biggo_num = int(input('빙고 넘버 : '))
        if ran_num == biggo_num:
            print('정답 - *~ 빙고 ~*')
            break
        else:
            if biggo_num > ran_num:
                print(f'힌트 - {biggo_num}보다 작은 수')
            else:
                print(f'힌트 - {biggo_num}보다 큰 수')

biggo_game()


# 12
def num_game():
    num = int(input('게임 정수 입력 : '))

    for i in range(1, num + 1):
        print('#', end = '') if i % 10 in [2, 4, 8] else print(i, end = '')
        if i in list(range(20, num+1, 20)):
            print('\n')

num_game()

# 13
ms_dict = {1 : 'January Winter', 2 : 'February Winter', 3 : 'March Spring',
              4 : 'April Spring', 5 : 'May Spring', 6 : 'June Summer',
              7 : 'July Summer', 8 : 'August Summer', 9 : 'September Fall',
              10 : 'October Fall', 11 : 'Nomember Fall', 12 :
         'December Winter'}

my_month = int(input('좋아하는 월 입력 : '))
if my_month not in list(range(1, 13)):
    print('존재하지 않는 월입니다.')
else:
    print(ms_dict[my_month])


# 14
amount_unit = input('숫자 입력 : ')
amount_unit = amount_unit.split(', ')
print(f'{int(amount_unit[0]):,}{amount_unit[1]}')

# 15

def trans():
    Month = input('좋아하는 월')
    month_dict = {'1' : 'January 삼월', '2' : 'February 이월', '3' : 'March 삼월',
                  '4' : 'April 사월', '5' : 'May 오월', '6' : 'June 육월',
                  '7' : 'July 칠월', '8' : 'August 팔월', '9' :'Setember 구월',
                  '10' : 'October 십월', '11' : 'Nomember 십일월', '12' : 'December 12월'}
    print(month_dict[Month])

trans()

# 16
def common_divisor():
    m, n = map(int, input('공약수를 구하고 싶은 두 수 : ').split())
    m_divisor = [i for i in range(1, m+1) if m % i == 0]
    n_divisor = [i for i in range(1, n+1) if n % i == 0]
    common_divisor = set(m_divisor) & set(n_divisor)
    common_divisor = sorted(list(common_divisor))

    print(f'{m}과 {n}의 공약수 :', end = '')
    for cd in common_divisor:
        print(cd, end = ', ') if cd != common_divisor[-1] else print(cd)

common_divisor()

# 17
input_msg = input('메시지 입력 : ')

def find_num(msg):
    msg = msg.replace(' ', '')
    letter_list = list(msg)
    letter_list = list(dict.fromkeys(letter_list))
    num_list = []
    for letter in letter_list:
        if letter.isnumeric():
            num_list.append(letter)

    for num in num_list:
        print(num, end = ', ') if num != num_list[-1] else print(num)


find_num(input_msg)

# print(list(dict.fromkeys([3, 1, 2, 2, 2])))
# print(dict.fromkeys([3,1,1,3, 3, 2,2, 1, 2, 2, 2]))

# 18
birthday = input('생년월일 입력 : ')

def my_age(birthday):

    today_date = '2024.01.07'

    if birthday[0] in ['0', '1', '2']:
        if birthday[5:7] == '01':
            if int(birthday[-1]) >= 7:
                foreign_age =  2024 - int(birthday[:4])
            else:
                foreign_age = 2024 - int(birthday[:4]) - 1
        else:
            foreign_age = 2024 - int(birthday[:4])
        korean_age = 2024 - int(birthday[:4]) + 1
    else:
        if birthday[5:7] == '01':
            if int(birthday[-1]) >= 7:
                foreign_age =  2024 - int(birthday[:4])
            else:
                foreign_age = 2024 - int(birthday[:4]) - 1
        else:
            foreign_age = 2024 - int(birthday[:4])
        korean_age = 2024 - int(birthday[:4]) + 1


    print(f'당신의 한국 나이는 {korean_age}세 입니다.\n당신의 만 나이는 {foreign_age}세 입니다.')

my_age(birthday)

# 19
# 풀이 1
num = int(input('팩토리얼 수 입력 : '))
fact = 1
i = 0
expre = f'{num}! = '
if num:
    while i <= num:
        expre += ''
        expre += str(num - i) if i != num else ''
        expre += ' * ' if i != num - 1 and i != num else ''

        i += 1
        if i != num + 1:
            fact *= i

    expre += ' = ' + str(fact)
    print(expre)
else:
    print(f'{num}! => {num}')


# 풀이 2
num = int(input('팩토리얼 수 입력 : '))
fact = 1
i = 0
expre = f'{num}! = '
if num:
    while num > 0:
        expre += ''
        expre += str(num)
        expre += ' * ' if num != 1 else ''
        fact *= num
        num -= 1

    expre += ' = ' + str(fact)
    print(expre)
else:
    print(f'{num}! => {num}')


# 20
end = int(input('범위 숫자 입력 : '))
def prime_num(end):
    if end == 1:
        print('숫자를 다시 입력하세요.')
    else:
        prime_list = []
        for n in range(2, end+1):
            divisors = []
            for k in range(1, n+1):
                if n % k == 0:
                    divisors.append(k)
            if len(divisors) == 2:
                prime_list.append(n)

        print(f'1 ~ {end} 범위에서 소수 : ')
        for prime in prime_list:
            print(prime, end = ', ') if prime != prime_list[-1] else print(prime)

prime_num(end)

# 21

scores = {'배트맨' : {'국어' : 90, '수학' : 89, '윤리' : 98, '국사' : 99},
          '마징가' : {'국어' : 82, '수학' : 71, '윤리' : 80, '국사' : 91},
          '슈퍼맨' : {'국어' : 77, '수학' : 100, '윤리' : 92, '국사' : 90},
          '슈렉' : {'국어' : 94, '수학' : 82, '윤리' : 93, '국사' : 71},
          '피오나' : {'국어' : 78, '수학' : 99, '윤리' : 91, '국사' : 82}}

for subject in scores['배트맨'].keys():
    all_scores = [scores[key][subject] for key in scores.keys()]
    print(f'[{subject}] 최고 점수 : {max(all_scores)}, 최저 점수 : {min(all_scores)}')


# 22

start_end = input('시작 구구단, 종료 구구단 입력 : ')
start = int(start_end[0])
end = int(start_end[-1])

unit = '단'
for i in range(10):
    for j in range(start, end + 1):
        if i:
            print(f'{j} * {i} = {j * i:2d}', end = '\n' if j == end else '   ')
        else:
            print(f'{j:->5}{unit:-<5}', end = '  ')
    if i == 0:
        print()

# 23 --> 20번과 같은 문제

# 24
number = input('숫자 입력 (4자리 숫자) :')

def digit_func(number):

    print(f'천의 자리 : {number[0]}')
    print(f'백의 자리 : {number[1]}')
    print(f'십의 자리 : {number[2]}')
    print(f'일의 자리 : {number[3]}')

digit_func(number)

# 25
datas = input('입력 데이터')
datas = list(map(int, datas.split()))


def addData(*datas):

    if type(datas[0]) is str:
        add = ''
        for word in datas[0]:
            add += word
        print(add)
    else:
        datas = list(map(int, datas[0]))
        print(sum(datas))


addData(datas)


# 26

col = int(input('가로 길이 : '))
row = int(input('세로 길이 : '))

for i in range(col):
    if i <= int((row-1)/2):
        print(f'{"*"*(int((col-1)/((row-1)/2))*(i+1) + 1 - int((col-1)/((row-1)/2))):^{col}}')
    else:
        print(f'{"*"*(int(-(col-1)/((row-1)/2))*(i-int((row-1)/2)) + col):^{col}}')



# 27
string = 'Merry Christmas HaPPy New YEaR'
string1 = list(string)
# string = [letter.lower() if letter.isupper() else letter.islower() letter.upper() for letter in string]
string1 = [letter.lower() if letter.isupper() else letter.upper() for letter in string1]
print(f"'{string}' => {''.join(string1)}")

# 28
def six_operation():
    a, b = map(int, input('숫자 2개 입력 : ').split(', '))
    print(f'덧셈 결과 : {a+b}')
    print(f'뺄셈 결과 : {a-b}')
    print(f'곱셈 결과 : {a*b}')
    if b != 0:
        print(f'나누기 결과 : {a/b}')
        print(f'몫 결과 : {a//b}')
        print(f'나머지 결과 : {a%b}')
    else:
        print(f'나누기 결과 : {0}')
        print(f'몫 결과 : {0}')
        print(f'나머지 결과 : {0}')

six_operation()

# 29
def personal_data(**datas):
    for key, value in datas.items():
        print(f" 개인 정보 : {key} - {value}", end = ' ')

personal_data(age = 12, id = 'mm1004', name = '마징가')

# 30

def Constellation():

    con_dict = {range(120, 219) : '물병', range(219, 321) : '물고기',
                    range(321, 420) : '양' , range(420, 521) : '황소',
                    range(521, 622) : '쌍둥이', range(622, 723) : '게',
                    range(723, 823) : '사자' , range(823, 924) : '처녀',
                    range(924, 1023) : '천칭', range(1023, 1123) : '전갈',
                    range(1123, 1225) : '궁수', range(1225, 1319) : '염소'}

    citizen_num = input('주민번호 입력 (000000-0000000) : ')
    citizen_num = citizen_num.split('-')
    birthday = citizen_num[0]
    if int(birthday[3]) == 1:
        if int(birthday[4:6]) >= 20:
            print('물병자리')
        else:
            print('염소자리')
    else:
        for key, value in con_dict.items():
            if int(birthday[2]) == 0:
                if int(birthday[3:6]) in key:
                    print(f'{value}자리')
                    break
            else:
                if int(birthday[2:6]) in key:
                    print(f'{value}자리')
                    break

Constellation()

# 31

year = int(input('년도 입력 : '))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print(f'{year}년은 평년입니다.')
    elif year % 100 != 0:
        print(f'{year}년은 윤년입니다.')
    elif year % 400 == 0:
        print(f'{year}년은 윤년입니다.')
else:
    print('아무 것도 아닙니다.')

# 32

citizen_num = input('주민번호 입력 (000000-0000000) : ')

def zca(citizen_num):

    con_dict = {range(120, 219) : '물병', range(219, 321) : '물고기',
                        range(321, 420) : '양' , range(420, 521) : '황소',
                        range(521, 622) : '쌍둥이', range(622, 723) : '게',
                        range(723, 823) : '사자' , range(823, 924) : '처녀',
                        range(924, 1023) : '천칭', range(1023, 1123) : '전갈',
                        range(1123, 1225) : '궁수', range(1225, 1319) : '염소'}

    zodiac_dict = {1992 : '원숭이', 1993 : '닭', 1994 : '개', 1995 : '돼지', 1996 : '쥐',
                  1997 : '소', 1998 : '호랑이', 1999 : '토끼', 2000 : '용',
                  2001 : '뱀', 2002 : '말', 2003 : '양'}

    citizen_num = citizen_num.split('-')
    birthday = citizen_num[0]
    if int(birthday[3]) == 1:
        if int(birthday[4:6]) >= 20:
            Constellation = '물병자리'
        else:
            Constellation = '염소자리'
    else:
        for key, value in con_dict.items():
            if int(birthday[2]) == 0:
                if int(birthday[3:6]) in key:
                    Constellation = value + '자리'
                    break
            else:
                if int(birthday[2:6]) in key:
                    Constellationf = value + '자리'
                    break

    if int(birthday[0]) in [3, 4, 5, 6, 7, 8, 9]:
        age = 2024 - int('19' + birthday[0:2])
    elif int(birthday[0]) in [0, 1, 2]:
        age = 2024 - int('20' + birthday[0:2])


    if int(birthday[0]) in [3, 4, 5, 6, 7, 8, 9]:
          year = int('19' + birthday[0:2])
          ind = (year - 1992) % 12
          key = list(zodiac_dict.keys())[ind]
          zodiac = zodiac_dict[key]
    elif int(birthday[0]) in [0, 1, 2]:
          year = int('20' + birthday[0:2])
          ind = (year - 1992) % 12
          key = list(zodiac_dict.keys())[ind]
          zodiac = zodiac_dict[key]

    print(f'띠 : {zodiac}띠, 별자리 : {Constellation}, 나이 : {age}')

zca(citizen_num)