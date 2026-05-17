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
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist


n, m, S, D = map(int, input().split())

adj = [[] for _ in range(n + 1)]
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
    edges.append((u, v, w))


distS = dijkstra(S, adj, n)
distD = dijkstra(D, adj, n)

shortest = distS[D]

if shortest == INF:
    print(-1)
    exit()

ans = INF

for u, v, w in edges:
    if distS[u] != INF and distD[v] != INF:
        val = distS[u] + w + distD[v]
        if shortest < val < ans:
            ans = val

    if distS[v] != INF and distD[u] != INF:
        val = distS[v] + w + distD[u]
        if shortest < val < ans:
            ans = val


print(ans if ans != INF else -1)