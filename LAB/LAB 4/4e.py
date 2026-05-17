n, m = map(int, input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

diff = [0] * (n + 1)
for i in range(m):
    u = u_list[i]
    v = v_list[i]
    diff[u] -= 1
    
    diff[v] += 1
print(*diff[1:])