n = int(input())
matrix = []
for i in range(n):
    matrix.append([0] * n)

for i in range(n):
    line = list(map(int, input().split()))
    neighbors = line[1:]

    for node in neighbors:
        matrix[i][node] = 1

for row in matrix:
    print(*row)