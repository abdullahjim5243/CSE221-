N, M, S, D, K = map(int, input().split())
adj = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)

def bfs_path(start, end):
    visited = [0] * (N + 1)
    parent = [0] * (N + 1)
    queue = [start]
    head = 0
    visited[start] = 1

    while head < len(queue):
        node = queue[head]
        head += 1
        if node == end:
            break
        for nxt in adj[node]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                parent[nxt] = node
                queue.append(nxt)

    if not visited[end]:
        return []

    path = []
    cur = end
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

path1 = bfs_path(S, K)
path2 = bfs_path(K, D)

if not path1 or not path2:
    print(-1)
else:
    full_path = path1 + path2[1:]
    print(len(full_path)-1)
    print(*full_path)
