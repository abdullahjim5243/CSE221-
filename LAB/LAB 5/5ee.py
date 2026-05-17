import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parent[rootB] = rootA  

N, M, Q = map(int, input().split())

parent = list(range(N + 1))


for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

for _ in range(Q):
    x, y = map(int, input().split())
    if find(x) == find(y):
        print("YES")
    else:
        print("NO")