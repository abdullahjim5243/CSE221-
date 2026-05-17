from collections import deque

start, target = input().split()
n = int(input())

forbidden = set()
for _ in range(n):
    forbidden.add(input().strip())

if target in forbidden:
    print(-1)
    exit()

# BFS
q = deque()
q.append((start, 0))

visited = set()
visited.add(start)

while q:
    cur, steps = q.popleft()
    
    if cur == target:
        print(steps)
        break
    
    for i in range(4):
        digit = int(cur[i])
        
        for move in [-1, 1]:
            new_digit = (digit + move) % 10
            new_state = cur[:i] + str(new_digit) + cur[i+1:]
            
            if new_state not in visited and new_state not in forbidden:
                visited.add(new_state)
                q.append((new_state, steps + 1))
else:
    print(-1)