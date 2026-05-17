import sys
from collections import deque
input = sys.stdin.readline

n, m, s, q = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

sources = list(map(int, input().split()))
queries = list(map(int, input().split()))

dist = [-1] * (n + 1)

dq = deque()

for src in sources:
    dist[src] = 0
    dq.append(src)

while dq:
    u = dq.popleft()
    
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            dq.append(v)

result = []
for node in queries:
    result.append(str(dist[node]))

print(" ".join(result))