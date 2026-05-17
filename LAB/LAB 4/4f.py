n = int(input())
x, y = map(int, input().split())
valid_moves = []

for r in range(x - 1, x + 2):
    for c in range(y - 1, y + 2):
        if 1 <= r <= n and 1 <= c <= n:
            if not (r == x and c == y):
                valid_moves.append((r, c))

print(len(valid_moves))
for move in valid_moves:
    print(*move)