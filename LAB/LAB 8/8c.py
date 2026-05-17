def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return False

    parent[b] = a
    return True


n, m = map(int, input().split())

edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v, i))

edges.sort()

parent = list(range(n + 1))
mst_cost = 0
cnt = 0
used = [False] * m
tree = [[] for _ in range(n + 1)]

for w, u, v, idx in edges:
    if union(parent, u, v):
        mst_cost += w
        cnt += 1
        used[idx] = True

        tree[u].append((v, w))
        tree[v].append((u, w))

if cnt != n - 1:
    print(-1)
else:
    ans = 10**30

    for w, u, v, idx in edges:
        if used[idx]:
            continue

        stack = [(u, 0, -1)]
        best_remove = -1

        while stack:
            node, par, best = stack.pop()

            if node == v:
                best_remove = best
                break

            for nxt, edge_w in tree[node]:
                if nxt == par:
                    continue

                new_best = best
                if edge_w < w:
                    new_best = max(new_best, edge_w)

                stack.append((nxt, node, new_best))

        if best_remove != -1:
            new_cost = mst_cost + w - best_remove

            if new_cost > mst_cost:
                ans = min(ans, new_cost)

    if ans == 10**30:
        print(-1)
    else:
        print(ans)
