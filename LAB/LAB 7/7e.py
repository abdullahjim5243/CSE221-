import heapq
import sys
input = sys.stdin.readline

INF = 10**18

n, m = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]

for i in range(m):
    adj[u[i]].append((v[i], w[i]))



dist = [[INF, INF] for _ in range(n + 1)]

pq = []


dist[1][0] = 0
dist[1][1] = 0
heapq.heappush(pq, (0, 1, -1))  

while pq:
    cost, node, last = heapq.heappop(pq)

    for nxt, wt in adj[node]:
        p = wt % 2

        if last == p:
            continue

        new_cost = cost + wt

        if new_cost < dist[nxt][p]:
            dist[nxt][p] = new_cost
            heapq.heappush(pq, (new_cost, nxt, p))



ans = min(dist[n][0], dist[n][1])

print(ans if ans != INF else -1)