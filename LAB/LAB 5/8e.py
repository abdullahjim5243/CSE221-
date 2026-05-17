n = int(input())

tasks = []

for _ in range(n):
    s, e = map(int, input().split())
    tasks.append((e, s))

tasks.sort()

ans = []
last_end = -1

for e, s in tasks:
    if s > last_end:
        ans.append((s, e))
        last_end = e

print(len(ans))

for s, e in ans:
    print(s, e)
