import heapq
import sys
input = sys.stdin.readline

INF = 10**18

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))   # undirected


# modified dijkstra
dist = [INF] * (n + 1)
dist[1] = 0

pq = [(0, 1)]   # (danger, node)

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, w in adj[u]:
        new_d = max(d, w)

        if new_d < dist[v]:
            dist[v] = new_d
            heapq.heappush(pq, (new_d, v))


# output
for i in range(1, n + 1):
    if dist[i] == INF:
        print(-1, end=' ')
    else:
        print(dist[i], end=' ')