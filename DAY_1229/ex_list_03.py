# ---------------------------------------------------------------
# list의 원소 / 요소 데이터 변경 및 삭제
# ---------------------------------------------------------------
# 'Merry Christmas'를 구성하는 문자를 리스트로 생성
msgList = list('Merry Christmas')

print(f'msgList => {msgList}')

# => ' ' 데이터를 '***'로 변경
print(f'msgList[5] => {msgList[5]}')

msgList[5] = '***'
print(f'msgList[5] => {msgList[5]}')


# 삭제  ==>  del 데이터 또는 del(데이터)
del msgList[5]
print(f'msgList => {msgList}')

del(msgList[5])
print(f'msgList => {msgList}')

del msgList