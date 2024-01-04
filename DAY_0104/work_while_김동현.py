# 17.5

i = 2
j = 5
while i <= 32 and j >= 1:
    print(i, j)
    i *= 2
    j -= 1

# 17.6
balance = int(input('금액 : '))
while True:
    balance -= 1350
    if balance < 0:
        break
    print(balance)