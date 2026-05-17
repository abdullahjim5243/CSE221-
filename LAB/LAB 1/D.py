T = int(input())  
results = [] 
for _ in range(T):
    N = int(input())  
    arr = list(map(int, input().split())) 

    flag = "YES"
    for i in range(N - 1):
        if arr[i] > arr[i + 1]:
            flag = "NO"
            break

    results.append(flag) 
for result in results:
    print(result)
