# 1 - 1
email = 'kim1234@naver.com'
print(email[:7])
print()

# 1 - 2
address = 'http://www.naver.com'
print(address[-9:])
print()

# 1 - 3
name = '홍길동'
print(name[1:])
print()

# 1 - 4
string = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
upper = string[0 : len(string) : 2]
lower = string[1 : len(string) : 2]
print(upper, lower, sep = '\n')
print()

# 1 - 5
string = 'ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
numbers = string[3 : len(string) : 4]
print(numbers)
print()

# 1 - 6
id = '881120-1068234'
birthday = id[ :6]
numbers = id[ :6] + id[7: ]
print(birthday, numbers, sep = '\n')
print()

# 2
num = int(input('정수 입력 : '))

numHex = hex(num)
numOct = oct(num)
numBin = bin(num)

print(f'10진수 : {num}\n16진수 : {numHex}\n8진수 : {numOct}\n2진수 : {numBin}')
print()

# 3
word1 = input('단어를 입력하세요 : ')
word2 = input('단어를 입력하세요 : ')
word3 = input('단어를 입력하세요 : ')

max_word = max(word1, word2, word3)
min_word = min(word1, word3, word3)
print(f'코드 값이 가장 큰 단어 : {max_word}\n코드 값이 가장 작은 단어 : {min_word}')
print()

# 4

msg = 'Happy New Year 2024~!'
word = input('단어 입력 : ')
print(f"'{word}' 단어 메세지 존재 여부 : {word in msg}")
print()

# 5

word = input('단어 입력 : ')

code_value1 = ord(word[0])
code_value2 = ord(word[1])
code_value3 = ord(word[2])

numHex1 = bin(code_value1)
numHex2 = bin(code_value2)
numHex3 = bin(code_value3)

print(f"'{word}' 코드 값 : {numHex1} {numHex2[2: ]} {numHex3[2: ]}")