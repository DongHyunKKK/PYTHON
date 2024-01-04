# 24.4

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)

# 24.5

string = input('')
word_list = string.split()
print(word_list.count('the'))

# 24.6

prices = input('물품 가격 여러 개 : ')
prices_list = prices.split(';')
prices_list = list(map(int, prices_list))
prices_list.sort(reverse = True)
for price in prices_list:
    price = int(price)
    print(f'{price:9,}')