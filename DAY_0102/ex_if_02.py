# [실습]
# 좋아하는 정수를 하나 저장 한 후 짝수면 '짝수입니다.'
# 홀수면 '홀수입니다.' 출력해 주세요.

myNum = 71

# 숫자 % 2 == 0 : 짝수, 숫자 % 2 == 1 : 홀수
if myNum % 2 == 0:
    print(f'{myNum} 짝수입니다.')
else:
    print(f'{myNum} 홀수입니다.')

if myNum % 2:
    print(f'{myNum} 홀수입니다.')
else:
    print(f'{myNum} 짝수입니다.')

# [실습2]
# 좋아하는 정수를 하나 저장 한 후 양수 이면 '~은 양수입니다.'
# 음수이면 '~은 음수입니다.'
# 0이면 '은 영입니다.'를 출력해 주세요.

if myNum > 0:
    print(f'{myNum} 양수')
elif myNum < 0:
    print(f'{myNum} 음수')
else:
    print(f'{myNum} 영')

# 중첩 조건문
if myNum == 0:
    print(f'{myNum} 양수')
else:
    if myNum > 0:
        print(f'{myNum} 양수')
    else:
        print(f'{myNum} 음수')
