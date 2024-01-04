# 25.7
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)

# 25.8
key_str = input('키들 입력 : ')
value_str = input('값들 입력 : ')

key_list = key_str.split()
value_list = value_str.split()
value_list = list(map(int, value_list))
x = dict(zip(key_list, value_list))

x = {key:value for key, value in x.items() if key != 'delta'}
x = {key:value for key, value in x.items() if value != 30}
print(x)




