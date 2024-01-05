# -----------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (2)
# 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 키와 값의
# - 형태 : def 함수명(**data):
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ N개
# - 호출 : 함수명(키1=값1)
#         함수명(키1 = 값1, 키2 = 값2, 키3 = 값3)
#         함수명()
# -----------------------------------------------------------
aDict = {'name' : 'Hong', 'age' : 10}
aDict.update(job = '학생')
aDict.update(job = '학생', birth = '1112', blood = 'A')
print(aDict)
aDict.update(점수1 = 100, 점수2 =200, 점수3 = 300, 점수4 = 400, 점수5 = 500, 점수6 = 600, 점수7 = 700)
print(aDict)

# -----------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinNumber
# 매개 변수 : 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ......
#           가변 + 데이터 정보 함께
#           키워드 파라미터 **
# 반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------
def joinMember(**member):
    # print(type(member))
    print(member)
    # members.update(**member)
    # for k, v in member.items():
    #    members.update(k = v)
    members[len(members)+1] = member  # 회원 식별을 위해
# -----------------------------------------------------------
# 함수 사용 즉, 호출
# -----------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}

print(f'[BF] : {members}')
# 회원가입 기능 함수 호출
joinMember(name = 'Hong', age = 17, birth = '2020/10/10')
joinMember(id = 'Hong84', phone = '010-1111-2222', job = 'actor', blood = 'B')
joinMember(id = 'baby', birth = '2001/09/01', job = 'doctor', blood = 'A')

print(f'[AF] : {members}')

# -----------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinNumber2
# 매개 변수 : 필수 => id, pw
#           선택 => **option, 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ......
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------
def joinMember2(id, pw, **option):
    # 멤버 저장소에 멤버 추가하기
    print('ok')

# -----------------------------------------------------------
# 함수 사용 즉, 호출
# -----------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
mList = []

print(f'[BF] {members}')
joinMember2('h', 'ph')
joinMember2('h', 'ph', phone = '010-1111-2222', blood = 'A')

# -----------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinNumber3
# 매개 변수 : 필수 => id, pw, loc, gender
#           선택 => **option, 이름, 전화 번호, 아이디, 이메일, 취미, 주소, 생일, ......
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------
def joinMember3(id, pw, loc = '내국인', gender = '남자', **option):
    # 멤버 저장소에 멤버 추가하기
    print(id, pw, loc, gender, option)
    # 키 => id
    # 값 => pw, loc = '내국인', gender = '남자', **option
    #       {'pw':'123', 'loc':'내국인', 'gender':'남자', 'etc':{option}}
    valueDict = {}
    valueDict['pw'] = pw
    valueDict['loc'] = loc
    valueDict['gender'] = gender
    valueDict['etc'] = option
    members[id] = valueDict
# -----------------------------------------------------------
# 함수 사용 즉, 호출
# -----------------------------------------------------------
# 가입된 회원들 저장 변수
members = {}
mList = []

print(f'[BF] {members}')
joinMember3('h1', 'ph')
joinMember3('h2', 'ph', gender = '여자')
joinMember3('h3', 'ph', phone = '010-1111-2222', blood = 'A')
print(f'[AF] {members}')

print()
