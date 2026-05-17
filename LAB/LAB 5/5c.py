N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

adj = [[] for i in range(N + 1)]
for i in range(M):
    a = u[i]
    b = v[i]
    adj[a].append(b)
    adj[b].append(a)
for neighbors in adj:
    neighbors.sort()

visited = [0] * (N + 1)
parent = [0] * (N + 1)
queue = [S]
visited[S] = 1
head = 0

while head < len(queue):
    node = queue[head]
    head += 1
    for nxt in adj[node]:
        if visited[nxt] == 0:
            visited[nxt] = 1
            parent[nxt] = node
            queue.append(nxt)


if not visited[D]:
    print(-1)
else:
    path = []
    cur = D
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(len(path)-1) 
    print(*path)
