import heapq
import sys
input = sys.stdin.readline

INF = 10**18

def dijkstra(start, adj, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist


# Input
n, m, S, T = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))


# Shortest paths
distS = dijkstra(S, adj, n)
distT = dijkstra(T, adj, n)


# Find best meeting point
best = INF
node = -1

for i in range(1, n + 1):
    if distS[i] == INF or distT[i] == INF:
        continue

    time = max(distS[i], distT[i])

    if time < best:
        best = time
        node = i

# Output
if node == -1:
    print(-1)
else:
    print(best, node)