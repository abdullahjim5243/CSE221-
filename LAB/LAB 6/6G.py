from collections import deque, defaultdict

n, A, B = input().split()
n = int(n)

words = [input().strip() for _ in range(n)]

start_map = defaultdict(list)
for w in words:
    start_map[w[0]].append(w)

# BFS
q = deque([A])
visited = set([A])

while q:
    cur = q.popleft()
    
    if cur == B:
        print("YES")
        break
    
    last_char = cur[-1]
    
    for nxt in start_map[last_char]:
        if nxt not in visited:
            visited.add(nxt)
            q.append(nxt)
    
    start_map[last_char] = []

else:
    print("NO")