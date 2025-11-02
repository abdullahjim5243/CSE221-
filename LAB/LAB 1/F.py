N = int(input())

inp_list= input().split()

arr = [0]*N
for i in range(N):
    arr[i] = int(inp_list[i])
for i in range(N):
    for j in range(N-1):
        if arr[j]%2 == arr[j+1]%2:
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
print(*arr)