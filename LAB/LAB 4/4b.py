n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))

adj = []
for i in range(n + 1):
    adj.append([])  

for i in range(m):
    u = u_list[i]
    v = v_list[i]
    w = w_list[i]
    adj[u].append((v, w))

for i in range(1, n + 1):
    print(f"{i}:", end="")

    for neighbor, weight in adj[i]:
        print(f" ({neighbor},{weight})", end="")
    print()