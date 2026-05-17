import sys
from collections import deque
input = sys.stdin.readline

R, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

visited = [[False] * H for _ in range(R)]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(sr, sc):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    
    diamonds = 0
    
    while q:
        r, c = q.popleft()
        
        if grid[r][c] == 'D':
            diamonds += 1
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < R and 0 <= nc < H:
                if not visited[nr][nc] and grid[nr][nc] != '#':
                    visited[nr][nc] = True
                    q.append((nr, nc))
    
    return diamonds

max_diamonds = 0

for i in range(R):
    for j in range(H):
        if grid[i][j] != '#' and not visited[i][j]:
            count = bfs(i, j)
            max_diamonds = max(max_diamonds, count)

print(max_diamonds)