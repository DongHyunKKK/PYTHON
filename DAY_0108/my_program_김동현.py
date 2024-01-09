import random
import time

# dic = {1 : 100, 2 : 200}
def priceup(x):
    for key in x.keys():
        x[key] += 1000

def pricedown(x):
    for key in x.keys():
        x[key] -= 1500

# Concert_schedule = '1월 9일 (화) 오후 2시'
# Concert_venue = '경북대학교 복현회관 1층 교육장 1'
# Concert_theme = '복현회관 합동 콘서트 IN 대구'
# Ticket_reservation = '1월 2일 (화) 오후 2시'

# 좌석당 가격
ticket_price = {range(6) : 9000, range(6, 12) : 8000, range(12, 18) : 7000, range(18, 24) : 6000, range(24, 30) : 5000}
num_audi = 0
revenue = 0
total_revenue = 0

# 당첨 번호
winning_number = random.sample(range(30), 3)

# 발작 버튼
k1 = int(input('발작 버튼 위치(행 개수, 0 ~ 5) : '))
k2 = int(input('발작 버튼 위치(열 개수, 0 ~ 6) : '))
mine_creation = [[i for i in range(6*(j-1), 6*j)] for j in range(1, 6)]
row_ind = random.sample(range(5), k1)
for row in row_ind:
    globals()['col_ind{}'.format(row)] = random.sample(range(6), k2)
    for col in globals()['col_ind{}'.format(row)]:
        mine_creation[row][col] = '*'
print(mine_creation)
singer_list = []
attendees_list = []
set_list = []
nam_yeo = []
reserved_seats = []
start = True
while True:
    if start:
        print('1. 공연 일자 : 1월 9일 (화) 오후 2시')
        print('2. 장소 : 경북대학교 복현회관 1층 교육장 1')
        print('3. 복현회관 합동 콘서트 IN 대구')
        name = input('이름을 입력하세요 : ')
        if name.isalpha() is False or len(name) == 1:
            print('이름을 다시 입력 하세요.')
        attendees_list.append(name)

        # phone_num = input('연락처를 입력하세요 : '))
        age = int(input('나이를 입력하세요 : '))
        if age >= 100 or age <= 8:
            print('죄송하지만 노약자는 콘서트 관람이 불가합니다.')
            break
        sex = input('성별을 입력하세요 (남/여) : ')
        nam_yeo.append(sex)
        want_singer = input('초청 가수 입력하세요 : ')
        singer_list.append(want_singer)
        if sex == '여' and want_singer == '김경호':
            head = input('해드뱅잉 가능하십니까? (네/아니요) : ')
            if head == '네':
                print('해드뱅잉 할거면 좌석번호 0 ~ 5 중에 선택을 권장합니다.')

        desired_seat = int(input('원하는 좌석 번호를 입력하세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : '))

        if desired_seat not in range(30):
            print('원하는 좌석 번호를 다시 입력해 주세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : ')
            desired_seat = int(input('원하는 좌석 번호를 입력하세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : '))

        if desired_seat in reserved_seats:
            print('이미 예매된 좌석 번호입니다. 다시 입력해 주세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : ')
            desired_seat = int(input('원하는 좌석 번호를 입력하세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : '))

        if desired_seat in range(24):
            print('일반 좌석을 예매하였습니다.')
        else:
            print('스탠딩 좌석을 예매하였습니다.')
        reserved_seats.append(desired_seat)
        want_song = input('원하는 콘서트 곡 : ')

        for key, value in ticket_price.items():
            if desired_seat in key:
                revenue = value
                print(f'티켓 가격 => {value:,}원 입니다.')

        # 관객수에 따른 티켓 가격 변동 (동적 가격)
        num_audi += 1
        if num_audi == 6:
            priceup(ticket_price)
        elif num_audi == 12:
            priceup(ticket_price)
        elif num_audi == 18:
            pricedown(ticket_price)
        elif num_audi == 24:
            pricedown(ticket_price)

        if desired_seat in winning_number:
            print('축하드립니다. 이벤트에 당첨되셨습니다. 티켓가격이 50% 할인되었습니다.')
            revenue = int(revenue / 2)

        # 총 수익
        total_revenue += revenue

        print(f'콘서트가 시작합니다!🙂')
        time.sleep(1)
        for person in attendees_list:
            print(f'{person} 관객이 환호 합니다!🥰')
            time.sleep(1)
        print(f'가수 {want_singer}가 가요"{want_song}"을 열창하고 있습니다!👍')
        set_list.append(want_song)
        if want_singer == '김경호':
            for ind, sex in enumerate(nam_yeo):
                if sex == '여':
                    time.sleep(1)
                    print(f'{attendees_list[ind]}👧님이 머리를 흔들고 있습니다!!!')
        res = True
        start = True
        for m in row_ind:
            if res:
                for n in globals()['col_ind{}'.format(m)]:
                    if desired_seat // 6 == m and desired_seat % 6 == n:
                        time.sleep(1)
                        print(f'{name} 관객이 라이브가 마음에 안들어서 발작 버튼🤬을 눌렀습니다. 콘서트가 종료 되었습니다.😠')
                        res = False
                        start = False
                        break
            else:
                break
    else:
        break
    print()

print(f'콘서트 관객 명단 : {attendees_list}')
print(f'남자 관객수 : {nam_yeo.count("남")}\n여자 관객수 : {nam_yeo.count("여")}')
print(f'예매된 좌석 번호 : {reserved_seats}')
print(f'이날 부른 가요 : {set_list}')
if total_revenue >= 50000:
    print(f'콘서트 총 수익은 {total_revenue:,}원이고 성공적으로 마무리 했습니다.👏👏👏')
    print('다음 콘서트에서 봐요~!🙂')
else:
    print(f'콘서트 총 수익은 {total_revenue:,}원이고 망했습니다.😭😭😭')

for singer in set(singer_list):
    for attendee in attendees_list:
        print(f'가수 {singer}님이 {attendee} 관객님에게 싸인을 주며 같이 사진을 찍고 있습니다.')

