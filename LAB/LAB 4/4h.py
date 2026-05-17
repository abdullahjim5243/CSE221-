def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, Q = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and gcd(i, j) == 1:
            adj[i].append(j)
    adj[i].sort()

for _ in range(Q):
    X, K = map(int, input().split())
    if K <= len(adj[X]):
        print(adj[X][K-1])
    else:
        print(-1)
