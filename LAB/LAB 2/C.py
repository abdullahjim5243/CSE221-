n, x = map(int, input().split())
a = list(map(int, input().split()))

index_map = {}

for i in range(n):
    for j in range(i + 1, n):
        required = x - a[i] - a[j]
        if required in index_map:
            k = index_map[required]
      
            if k != i and k != j:
                print(k + 1, i + 1, j + 1)  
                exit(0)

    index_map[a[i]] = i
print(-1)