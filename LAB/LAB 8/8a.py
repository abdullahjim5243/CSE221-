n, k = map(int, input().split())

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


for _ in range(k):
    a, b = map(int, input().split())

    pa = find(a)
    pb = find(b)

    if pa != pb:
        parent[pb] = pa
        size[pa] += size[pb]

    print(size[find(a)])