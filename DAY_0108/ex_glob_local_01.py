# -----------------------------------------------------------
# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# # 전역 변수(Global Variable)
# - 파이썬(py) 파일에 존재 하는 변수
# - 파일 내부 모든 곳에서 사용 가능한 변수
# - 파일실행을 종료하면 메모리에서 사라진다
# # 지역 변수(Local Variable)
# - 함수에 존재하는 변수
# - 함수에서만 사용 가능한 변수
# - 함수가 종료 되면 변수들은 메모리에서 사라진다
# -----------------------------------------------------------
# 사용자 정의 함수
def currenrDate(month, day):
    # year, month, day => 지역 변수
    print(f'Today : {year}/{month:0>2}/{day:0>2}')

def currenrDate2(month, day):
    # year, month, day => 지역 변수
    # year => 전역 변수
    print(f'Today : {year}/{month:0>2}/{day:0>2}')

def currentDate3(month, day, week):
    # month, day, week => 지역 변수
    # year => 전역 변수
    print(f'Today : {year}/{month:0>2}/{day:0>2}/{week}요일')


# 전역 변수
year,  month, day = 2024, 1, 8

# 함수 사용 즉 함수 호출
currentDate3(month, day, week = 'Friday')

print(f'year : {year}, month : {month}, day : {day}')

# 함수의 변수인 지역 변수는 함수 밖에서 사용 불가
print(f'week : {week}')