import heapq
import sys
input = sys.stdin.readline

INF = 10**18

n, m, S, D = map(int, input().split())
w = [0] + list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)


# Dijkstra
dist = [INF] * (n + 1)
dist[S] = w[S]

pq = [(dist[S], S)]

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v in adj[u]:
        new_d = d + w[v]

        if new_d < dist[v]:
            dist[v] = new_d
            heapq.heappush(pq, (new_d, v))


# Output
if dist[D] == INF:
    print(-1)
else:
    print(dist[D])