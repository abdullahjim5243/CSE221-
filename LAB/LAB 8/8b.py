n, m = map(int, input().split())

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = [i for i in range(n + 1)]


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


total = 0

for w, u, v in edges:
    pu = find(u)
    pv = find(v)

    if pu != pv:
        parent[pv] = pu
        total += w

print(total)