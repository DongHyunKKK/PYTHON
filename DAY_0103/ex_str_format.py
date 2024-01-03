# ---------------------------------------------------------------------
# 출력되는 문자열 str에서 형식/양식/서식 설정
# 데이터 출력하는 칸 수, 정렬 방향
# 데이터 출력하는 칸 수, 정렬 방향 (왼쪽, 오른쪽, 가운데), 빈 칸수 채우기
# ---------------------------------------------------------------------
count = 1
print(f'파일명 : img_{count:3}.jpg')

count = 21
print(f'파일명 : img_{count:3}.jpg')

count = 101
print(f'파일명 : img_{count:3}.jpg')

print()

count = 1
print(f'파일명 : img_{count:0>3}.jpg')

count = 21
print(f'파일명 : img_{count:0>3}.jpg')

count = 101
print(f'파일명 : img_{count:0>3}.jpg')

print()

count = 1
print(f'파일명 : img_{count:<3}.jpg')

count = 21
print(f'파일명 : img_{count:<3}.jpg')

count = 101
print(f'파일명 : img_{count:<3}.jpg')

print()

count = 1
print(f'파일명 : img_{count:0<3}.jpg')

count = 21
print(f'파일명 : img_{count:0<3}.jpg')

count = 101
print(f'파일명 : img_{count:0<3}.jpg')

print()

count = 1
print(f'파일명 : img_{count:*>3}.jpg')

count = 21
print(f'파일명 : img_{count:*>3}.jpg')

count = 101
print(f'파일명 : img_{count:*>3}.jpg')

avg = 98.1234
print(f'학급 평균 : {avg:.6}점')
print('학급 평균 : % 10.2f점' % avg)