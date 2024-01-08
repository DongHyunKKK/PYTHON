# -----------------------------------------------------------
# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# - 함수 내에서 전역 변수 값을 변경하고자 하는 경우 추가 코드 필요
# - 추가 코드  :global 전역 변수명
# -> 주의 : 전역 변수 값이 언제든지 함수로 변경이 될 수 있는 상황
#          사용 시에 주의 필요함
# -----------------------------------------------------------
# 사용자 정의 함수
def currentDate(todays):
    # todays => 년, 월, 일을 원소로 담고 있는 데이터 타입, 리스트
    todays[0] = todays[0] + 100
    print(f'Today : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}')

# 전역 변수
year, month, day = 2024, 1, 8
todayList = [year, month, day]

print(f'year : {year}, month : {month}, day : {day}')
currentDate(todayList)
print(f'year : {year}, month : {month}, day : {day}')
