from collections import deque

# input
n = int(input())
x1, y1, x2, y2 = map(int, input().split())

# 8 knight moves
moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

# visited array
visited = [[False]*(n+1) for _ in range(n+1)]

# BFS queue: (x, y, steps)
q = deque()
q.append((x1, y1, 0))
visited[x1][y1] = True

while q:
    x, y, d = q.popleft()
    
    # reached target
    if x == x2 and y == y2:
        print(d)
        break
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        
        if 1 <= nx <= n and 1 <= ny <= n and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, d + 1))
else:
    print(-1)