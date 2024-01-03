# 13.6
x = 5
if x != 10:
    print('ok')

# 13.7
price = int(input('가격을 입력하세요 : '))
coupon = input('쿠폰을 입력하세요 : ')
if coupon == 'Cash3000':
    print(price - 3000)
else:
    print(price - 5000)

# 14.6

written_test = int(input('필기시험 점수 : '))
coding_test = input('합격이면 아무 문자 입력(True)하고 불합격이면 입력(False)하지 마세요 : ')

if written_test >= 80 and coding_test:
    print('합격')
else:
    print('불합격')

# 14.7
scores = input('점수를 입력하세요 : ')
scores_list = scores.split()
print(scores_list)
scores_list1 = []
scores_list1.append(int(scores_list[0]))
scores_list1.append(int(scores_list[1]))
scores_list1.append(int(scores_list[1]))
scores_list1.append(int(scores_list[2]))
print(scores_list1)

if 0 <= scores_list1[0] <= 100 and 0 <= scores_list1[1] <= 100 and 0 <= scores_list1[2] <= 100 and 0 <= scores_list1[3] <= 100:
    if sum(scores_list1) / 4 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

# 15.3
x = int(input('정수를 입력하세요 : '))
if 11 <= x <= 20:
    print('11~20')
elif 21 <= x <= 30:
    print('21~30')
else:
    print('아무것도 해당하지 않음')

# 15.4
age = int(input('나이를 입력하세요 : '))
balance = 9000

if age < 7:
    print('나이를 다시 입력하세요.')
else:
    if 7 <= age <= 12:
        print(balance - 650)
    elif 13 <= age <= 18:
        print(balance - 1050)
    else:
        print(balance - 1250)