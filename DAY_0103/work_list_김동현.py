# 22.9
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

# 22.10
m, n = input('정수 두 개 : ').split()
m = int(m)
n = int(n)
power_list = [2**i for i in range(m, n + 1)]
del power_list[1]
del power_list[-2]
print(power_list)