# 11.6
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3: ])
print(population[-3: ])

# 11.7
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

# 11.8
some = input('숫자 또는 문자열 여러개(5개 이상)를 입력하시오.').split()
del some[-5:]
print(tuple(some))

# 11.9
string1 = input('문자열을 입력하세요 : ')
string2 = input('문자열을 입력하세요 : ')
odd_ind = string1[1::2]
even_ind = string2[::2]
print(odd_ind + even_ind)