from collections import deque
import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    x1, y1, x2, y2 = int(data[1])-1, int(data[2])-1, int(data[3])-1, int(data[4])-1
    
    if x1 == x2 and y1 == y2:
        sys.stdout.write("0\n")
        return
    
    moves = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    
    
    from array import array
    dist = array('i', [-1] * (N * N))
    visited = bytearray(N * N)
    
    s = x1 * N + y1
    t = x2 * N + y2
    dist[s] = 0
    visited[s] = 1
    
    queue = deque([s])
    
    while queue:
        pos = queue.popleft()
        x = pos // N
        y = pos - x * N
        d = dist[pos] + 1
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                npos = nx * N + ny
                if not visited[npos]:
                    visited[npos] = 1
                    dist[npos] = d
                    if npos == t:
                        sys.stdout.write(str(d) + "\n")
                        return
                    queue.append(npos)
    
    sys.stdout.write("-1\n")

solve()