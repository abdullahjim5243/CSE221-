from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    indegree[v] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

count = 0

while q:
    node = q.popleft()
    count += 1
    
    for nei in adj[node]:
        indegree[nei] -= 1
        if indegree[nei] == 0:
            q.append(nei)

if count == N:
    print("NO")   
else:
    print("YES")  