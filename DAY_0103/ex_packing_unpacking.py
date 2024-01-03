# ---------------------------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
# ---------------------------------------------------------------
msg = 'Happy New Year'

# 팩킹(Packing) 방식
msgList = msg.split()
print(msgList[0], msgList[-1])

# 언팩킹(Unpacking) 방식
# 데이터 수와 변수 수가 동일 해야 한다.
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 데이터 수와 변수 수가 다르므로 Error 발생
# m1, m2 = msg.split()
# print(m1, m2)

# 변수를 여러 개 생성 하는 경우
age = 12
name = 'Hong'
job = '학생'

age, name, job = 12, 'Hong', '학생'
info = (12, 'Hong', '학생')
info2 = 12, 'Hong', '학생'
age1 = info2[0]
name1 = info2[1]
job1 = info2[2]

age1, name1, job1 = 12, 'Hong', '학생'