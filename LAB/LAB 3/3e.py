def solve(a, n, m):
    if n == 0:
        return (1, 0)
    
    p, s = solve(a, n//2, m)

    p2 = (p * p) % m
    s2 = (s + p * s) % m

    if n % 2 == 0:
        return (p2, s2)
    else:
        p3 = (p2 * a) % m
        s3 = (s2 + p3) % m
        return (p3, s3)


T = int(input())

for _ in range(T):
    a, n, m = map(int, input().split())
    print(solve(a, n, m)[1] % m)