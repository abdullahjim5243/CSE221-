N, M, K = map(int, input().split())
positions = set()
for i in range(K):
    x, y = map(int, input().split())
    positions.add((x, y))
moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

for x, y in positions:
    for xx, yy in moves:
        nx, ny = x + xx, y + yy
        if (nx, ny) in positions:  
            print("YES")
            exit()

print("NO")
