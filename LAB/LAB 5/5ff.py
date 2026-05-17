import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, R = map(int, input().split())


adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


subtree = [0] * (N + 1)

def dfs(node, parent):
    subtree[node] = 1  
    for nei in adj[node]:
        if nei != parent:
            dfs(nei, node)
            subtree[node] += subtree[nei]


dfs(R, -1)


Q = int(input())
for _ in range(Q):
    x = int(input())
    print(subtree[x])