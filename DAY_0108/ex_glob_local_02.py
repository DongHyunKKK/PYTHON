# -----------------------------------------------------------
# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# - 함수 내에서 전역 변수 값을 변경하고자 하는 경우 추가 코드 필요
# - 추가 코드  :global 전역 변수명
# -> 주의 : 전역 변수 값이 언제든지 함수로 변경이 될 수 있는 상황
#          사용 시에 주의 필요함
# -----------------------------------------------------------
# 사용자 정의 함수
def currentDate(month, day):
    # year, month, day => 지역 변수
    print(f'Today : {year}/{month:0>2}/{day:0>2}')

def currentDate2(month, day):
    # year, month, day => 지역 변수
    # year => 전역 변수
    # 함수 내에서 전역 변수 값을 변경하고자 하는 경우 => global 전역 변수명
    global year
    year += 10
    print(f'Today : {year}/{month:0>2}/{day:0>2}')


# 전역 변수
year, month, day = 2024, 1, 8

# 변수의 값 변화를 확인한다.
print(f'year : {year}, month : {month}, day : {day}')
currentDate2(month, day)
print(f'year : {year}, month : {month}, day : {day}')

