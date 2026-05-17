MOD = 107

a, b = map(int, input().split())

result = 1
a = a % MOD

while b > 0:
    if b % 2 == 1:
        result = (result * a) % MOD
    
    a = (a * a) % MOD
    b //= 2

print(result)