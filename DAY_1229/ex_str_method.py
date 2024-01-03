# ---------------------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드(method) 살펴 보기
# - 메서드(Method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
# - 사용 방법
#   변수명, 메서드명() ==> msg = 'Good'
#                       msg.메서드명()
#   데이터, 메서드명() ==> 'Good'.메서드명()
# ---------------------------------------------------------------
# str을 대문자로 변환 ==> upper() 메서드
print('Good'.upper())

# str을 소문자로 변환 ==> lower() 메서드
print('Good'.lower())

# str이 모두 대문자 인지 검사 후 결과 반환 => isupper() 메서드
print('Good'.isupper())

# str이 모두 소문자 인지 검사 후 결과 반환 => islower() 메서드
print('Good'.islower())

# str이 0~9로 구성되어 있는지 검사 후 결과 반환 => isdecimal() 메서드
print('Good'.isdecimal(), '012'.isdecimal(), '-9'.isdecimal())

# str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메서드
print('Good'.isalpha(), 'Good2024'.isalpha(), '한글'.isalpha())

# str이 문자, 숫자로만 구성되어 있는지 검사 후 결과 반환 => isalnum() 메서드
print('Good'.isalnum(), 'Good2024'.isalnum(), '한글'.isalnum())

# str 문자에서 특정 문자/문자열로 시작하는지 검사 후 결과 반환
# 시작 => ??
print('??Happy New'.startswith('??'))
print('??Happy New'.startswith('!'))

# 끝 => jpg
print('flower.jpg'.endswith('jpg'))
print('flower.png'.endswith('jpg'))
# print('flower.txt'.endswith('jpg', 'png', 'txt'))
print('flower.txt'[-3: ] in ('jpg', 'png', 'txt'))

# str 특정 인덱스 문자를 변경해주는 메서드 => replace() 메서드
name = 'HongGulDong'
# => u ==> i로 변경
print(name[5])

# name[5] = i ==> 인덱싱은 안됨 ==> 메서드 제공
print(name.replace('o','*'))
print(name.replace('o', '*', 1))
print()
# ---------------------------------------------------------------
# [실습 1] 단어를 입력 받은 후 아래 코드를 작성하세요.
# - 입력 받은 단어가 모두 알파벳으로 구성 되어 있는지 검사
# - 입력 받은 단어가 모두 숫자로 구성 되어 있는지 검사
# - 입력 받은 단어가 모두 대문자로 구성 되어 있는지 검사
# - 입력 받은 단어가 모두 소문자로 구성되어 있는지 검사
# ---------------------------------------------------------------

word = input('입력 단어 : ')
print(f'{word}가 모두 알파벳으로 구성? {word.isalpha()}')
print(f'{word}가 모두 숫자로 구성? {word.isnumeric()}')
print(f'{word}가 모두 대문자로 구성? {word.isupper()}')
print(f'{word}가 모두 소문자로 구성? {word.islower()}')
print()

# ---------------------------------------------------------------
# [실습 2] 파일명을 입력 받은 후 아래 코드를 작성하세요.
# - 입력 받은 파일이 text 파일 여부 검사  ==> 확장자 txt
# - 입력 받은 파일이 jpg 파일 여부 검사  ==> 확장자 jpg
# - 입력 받은 파일이 py 파일 여부 검사  ==> 확장자 py
# ---------------------------------------------------------------

file_name = input('파일명 : ')
print(f"입력 받은 파일은 txt 파일? {file_name.endswith('txt')}")
print(f"입력 받은 파일은 jpg 파일? {file_name.endswith('jpg')}")
print(f"입력 받은 파일은 png 파일? {file_name.endswith('png')}")