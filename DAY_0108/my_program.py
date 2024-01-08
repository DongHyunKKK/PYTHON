import random

# dic = {1 : 100, 2 : 200}
def priceup(ticket_price):
    ticket_price = {key : value + 1000 for key, value in ticket_price.items()}
    return ticket_price
# ticket_price = priceup(dic)
# print(ticket_price)

def pricedown(ticket_price):
    ticket_price = {key : value - 1500 for key, value in ticket_price.items()}
    return ticket_price

Concert_schedule = '1월 9일 (화) 오후 2시'
Concert_venue = '경북대학교 복현회관 1층 교육장 1'
Concert_theme = '김경호 데뷔 30주년 전국투어콘서트 IN 대구'
# Ticket_reservation = '1월 2일 (화) 오후 2시'
song_list = []  # 나중에 작성
ticket_price = {range(6) : 9000, range(6, 12) : 8000, range(12, 18) : 7000, range(18, 24) : 6000, range(24, 30) : 5000}
seat_type = {'regular' : range(24), 'stand' : range(24, 30)}
num_audi = 0
revenue = 0
total_revenue = 0
winning_number = random.randint(1, 30)
k1 = int(input('지뢰 위치(행 개수, 0 ~ 5) : '))
k2 = int(input('지뢰 위치(열 개수, 0 ~ 6) : '))
row_ind = random.sample(range(5), k1)
col_ind = random.sample(range(6), k2)

mine_creation = [[i for i in range(6*(j-1), 6*j)] for j in range(1, 6)]
# print(mine_creation)

for row in row_ind:
    for col in col_ind:
        mine_creation[row][col] = '*'

while True:
    print('1. 공연 일자 : 1월 9일 (화) 오후 2시')
    print('2. 장소 : 경북대학교 복현회관 1층 교육장 1')
    print('3. 김경호 데뷔 30주년 전국투어콘서트 IN 대구')
    name = input('이름을 입력하세요 : ')
    if name.isalpha() is False or len(name) == 1:
        print('이름을 다시 입력 하세요.')
        continue
    # phone_num = input('연락처를 입력하세요 : '))
    age = int(input('나이를 입력하세요 : '))
    if age >= 100 or age <= 8:
        print('죄송하지만 노약자는 콘서트 관람이 불가합니다.')
        continue
    sex = input('성별을 입력하세요 (남/여) : ')

    if sex == '여':
        head = input('해드뱅잉 가능하십니까? (네/아니요) : ')
        if head == '네':
            print('해드뱅잉 할거면 좌석번호 0 ~ 5 중에 선택을 권장합니다.')

    desired_seat = int(input('원하는 좌석 번호를 입력하세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : '))
    if desired_seat not in range(30):
        print('원하는 좌석 번호를 다시 입력해 주세요. (0 ~ 23 : regular, 24 ~ 29 : stand) : ')
        continue
    set_list = input('원하는 콘서트 곡 : ')
    if set_list not in song_list:
        print('원하는 곡을 다시 적어주세요 : ')
        continue
    if desired_seat in range(6):
        print(f'Ticket price => 9000원')
    elif desired_seat in range(6, 12):
        print(f'Ticket price => 8000원')
    elif desired_seat in range(12, 18):
        print(f'Ticket price => 7000원')
    elif desired_seat in range(18, 24):
        print(f'Ticket price => 6000원')
    elif desired_seat in range(24, 30):
        print(f'Ticket price => 5000원')

    for key, value in ticket_price.items():
        if ticket_price in key:
            revenue = value
    if desired_seat == winning_number:
        print('축하드립니다. 이벤트에 당첨되셨습니다. 티켓가격이 50% 할인되었습니다.')

    revenue = int(revenue / 2)
    # 관객수에 따른 티켓 가격 변동
    num_audi += 1
    if 6 < num_audi <= 12:
        ticket_price = priceup(ticket_price)
    if 12 < num_audi <= 18:
        ticket_price = priceup(ticket_price)
    if 19 < num_audi <= 24:
        ticket_price = pricedown(ticket_price)
    if 24 < num_audi <= 30:
        ticket_price = pricedown(ticket_price)

    total_revenue += revenue
    print(f'공연이 시작 되었습니다! {set_list}곡을 열창 중 입니다!')

    for m in row_ind:
        for n in col_ind:
            if desired_seat // 6 == m and desired_seat % 6 == n:
                print(f'{name} 예매자분께서 지뢰를 밟으셨습니다. 공연이 취소 되었습니다.')
                break

if total_revenue >= 150000:
    price(f'콘서트 총 수익은 {total_revenue} 이므로 성공적으로 마무리 했습니다.')
else:
    price(f'콘서트 총 수익은 {total_revenue} 이므로 망했습니다.')



