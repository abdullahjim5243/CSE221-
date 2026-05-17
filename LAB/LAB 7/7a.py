import heapq
import sys
input = sys.stdin.readline

INF = 10**18

n, m, S, D = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]

for i in range(m):
    adj[u[i]].append((v[i], w[i]))


# Dijkstra
dist = [INF] * (n + 1)
parent = [-1] * (n + 1)

dist[S] = 0
pq = [(0, S)]

while pq:
    d, node = heapq.heappop(pq)

    if d > dist[node]:
        continue

    for nxt, wt in adj[node]:
        new_d = d + wt

        if new_d < dist[nxt]:
            dist[nxt] = new_d
            parent[nxt] = node
            heapq.heappush(pq, (new_d, nxt))

if dist[D] == INF:
    print(-1)
else:
    print(dist[D])

    
    path = []
    cur = D
    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    print(*path)