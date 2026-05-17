N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

adj = [[] for _ in range(N + 1)]
for i in range(M):
    a = u[i]
    b = v[i]
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (N + 1)
stack = [1]
order = []

while stack:
    node = stack.pop()
    if visited[node] == 0:
        visited[node] = 1
        order.append(node)
        for nxt in adj[node]:
            if visited[nxt] == 0:
                stack.append(nxt)

print(*order)
