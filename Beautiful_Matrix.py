matrix = []
pos_row = 0
pos_col = 0
for i in range(5):
    line = input().strip()
    row = list(map(int,line.split()))
    matrix.append(row)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            pos_row = i
            pos_col = j
moves = abs(pos_row - 2) + abs(pos_col - 2)
print(moves)
