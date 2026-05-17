import heapq

t = int(input())

for _ in range(t):

    n, m, s, d = map(int, input().split())

    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        graph[u[i]].append((v[i], w[i]))
        graph[v[i]].append((u[i], w[i]))

 
    best = [0] * (n + 1)

    pq = [(-10**18, s)]
    best[s] = 10**18

    while pq:

        val, node = heapq.heappop(pq)
        val = -val

        if node == d:
            break

        for nxt, wt in graph[node]:

            new_val = min(val, wt)

            if new_val > best[nxt]:
                best[nxt] = new_val
                heapq.heappush(pq, (-new_val, nxt))

    print(best[d])