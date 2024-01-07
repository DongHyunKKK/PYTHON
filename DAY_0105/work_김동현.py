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
        print(chr(2664))
        if str_num == 'Q':
            break
    elif str_num != 'Q' and str_num.isalpha():
        print(chr(2660))
        if str_num == 'q':
            break
    elif str_num.isnumeric():
        print(chr(25CE)*len(int(str_num)))

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
    print(f'{string}의 인코딩 : {hex_incoding}\n{string}의 인코딩 : {binary_incoding}')

string = '가나다'
print(bin_word(string))

# print(hex(ord('가'))+hex(ord('나')))
# print(hex(ord('나')))
# print(hex(ord('다')))

# data = ' 2024 apple '
# s= data.replace(' ', '')
# data = list(s)
# print(s)

# 6

def sort_some(words_list, number):
    sort_list = sorted(word_list)






data = ['askde', 'beach', 'surf']
print(sorted(data))
n = 2

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
    string = string.replace(',','')
    num_list = list(string)
    num_list = list(map(int, num_list))
    print(f'{string}의 합 : {sum(num_list)}, 가장 큰 수 : {max(num_list)}, 가장 작은 수 : {min(num_list)}')

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
    korean_age = 2024 - int(birth[:4]) + 1

    foreign_age
    print(f'당신의 한국 나이는 ')

# 19
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

# 23


# 24
number = input('숫자 입력 (4자리 숫자) :')

def digit_func(number):

    print(f'천의 자리 : {number[0]}')
    print(f'백의 자리 : {number[1]}')
    print(f'십의 자리 : {number[2]}')
    print(f'일의 자리 : {number[3]}')

digit_func(number)

# 25
def addData(*data):
    data = list(data[1])
    print(data)

addData('A', 'BC', 'Good')


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
string = list(string)
string = [letter.lower() for letter in string if letter.isupper()]

print(string)

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

