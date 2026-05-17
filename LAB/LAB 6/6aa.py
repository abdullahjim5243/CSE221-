from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        indegree[b] += 1
    
    q = deque()
    
    # push all nodes with indegree 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    order = []
    
    while q:
        u = q.popleft()
        order.append(u)
        
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    # check for cycle
    if len(order) != n:
        print(-1)
    else:
        print(*order)