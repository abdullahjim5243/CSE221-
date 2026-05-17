N, M = map(int, input().split())

adj = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    adj.append(row)
for k in range(M):
    u, v, w = map(int, input().split())
    adj[u-1][v-1] = w

for i in range(N):
    for j in range(N):
        print(adj[i][j], end=" ")
    print()
