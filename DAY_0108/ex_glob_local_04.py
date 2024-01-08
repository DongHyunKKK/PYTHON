# -----------------------------------------------------------
# 주의! 꼭 전역 변수가 아니더라도 list, tuple, set, dict의 경우
# 함수의 매개 변수로 전달 후 원소 값 변경 시 모두 적용됨!
# ==> 해결 : 깊은 복사 deepcopy로 복사본 전달한다.
# -----------------------------------------------------------
def one(number):
    print(number)

def datas(nums, value):
    # nums : 리스트
    # value : 정수
    nums[-1] = 1004
    print(nums, value, sep = ' - ')

# 전역 변수 선언
value = 'Good'
dataList = [11, 22, 33]
num = 7

# 함수 호출
print(f'전역 변수 값 => value : {value}, dataList : {dataList}, num : {num}')

one(num)
datas(dataList, value)

print(f'전역 변수 값 => value : {value}, dataList : {dataList}, num : {num}')