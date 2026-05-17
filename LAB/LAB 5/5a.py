N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (N + 1)
queue = []
head = 0
order = []

visited[1] = 1
queue.append(1)

while head < len(queue):
    u = queue[head]
    head += 1
    order.append(u)

    for v in adj[u]:
        if visited[v] == 0:
            visited[v] = 1
            queue.append(v)

print(*order)
