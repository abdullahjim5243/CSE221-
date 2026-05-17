MOD = 1000000007

def multiply(a,b,c,d, e,f,g,h):
    return (
        (a*e + b*g) % MOD,
        (a*f + b*h) % MOD,
        (c*e + d*g) % MOD,
        (c*f + d*h) % MOD
    )

T = int(input())

for _ in range(T):
    a,b,c,d = map(int,input().split())
    x = int(input())

    r1,r2,r3,r4 = 1,0,0,1

    while x > 0:
        if x % 2 == 1:
            r1,r2,r3,r4 = multiply(r1,r2,r3,r4, a,b,c,d)

        a,b,c,d = multiply(a,b,c,d, a,b,c,d)
        x //= 2

    print(r1, r2)
    print(r3, r4)