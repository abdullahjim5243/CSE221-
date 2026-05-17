import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

# graph
adj = defaultdict(set)
indegree = [0] * 26

used = [False] * 26
for w in words:
    for c in w:
        used[ord(c) - 97] = True

for i in range(n - 1):
    w1 = words[i]
    w2 = words[i + 1]
    
    min_len = min(len(w1), len(w2))
    
    # check prefix invalid case
    if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
        print(-1)
        exit()
    
    for j in range(min_len):
        if w1[j] != w2[j]:
            u = ord(w1[j]) - 97
            v = ord(w2[j]) - 97
            
            if v not in adj[u]:
                adj[u].add(v)
                indegree[v] += 1
            break

heap = []
for i in range(26):
    if used[i] and indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    u = heapq.heappop(heap)
    result.append(chr(u + 97))
    
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(heap, v)

if len(result) != sum(used):
    print(-1)
else:
    print("".join(result))