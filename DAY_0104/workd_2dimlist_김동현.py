# 23.6
print([[[0 for col in range(3)] for row in range(4)] for depth in range(2)])

# 23.7

# (1)
col, row = map(int, input('가로 세로 : ').split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

print(matrix[1][1])

for i in range(col):
    for j in range(row):
        if matrix[i][j] != '*':
            mine_list = []
            for s in [-1, 1, 0]:
                for t in [-1, 1, 0]:
                    if 0 <= i+s <= col-1 and 0 <= j+t <= row-1:
                        if matrix[i+s][j+t] == '*':
                            mine_list.append(matrix[i+s][j+t])
            matrix[i][j] = len(mine_list)
        print(matrix[i][j], end = '')
    print()

print(matrix)

print()

# (2)
col, row = map(int, input('가로 세로 : ').split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

matrix.insert(0, [0 for i in range(col+2)])
matrix.append([0 for i in range(col+2)])
for k in range(1, 1+row):
    matrix[k].insert(0, 0)
    matrix[k].append(0)
print(matrix)

for i in range(1, 1+col):
    for j in range(1, 1+row):
        if matrix[i][j] != '*':
            mine_list = []
            for s in [-1, 1, 0]:
                for t in [-1, 1, 0]:
                    if matrix[i+s][j+t] == '*':
                        mine_list.append(matrix[i+s][j+t])
            matrix[i][j] = len(mine_list)
        print(matrix[i][j], end = '')
    print()

print(matrix)