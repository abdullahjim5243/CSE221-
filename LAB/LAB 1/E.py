N = int(input())
a = list(map(int, input().split()))


ans = 'YES'
operations = []

def reverse_subarray(arr, i):
    arr[i], arr[i+2] = arr[i+2], arr[i]


for i in range(N):
    for j in range(N - 2):
        if a[j] > a[j+1] or a[j] > a[j+2]:
            if a[j] > a[j+2]:
                reverse_subarray(a, j)
                operations.append((j+1, j+3))

for i in range(N - 1):
    if a[i] > a[i+1]:
        ans = 'NO'
        break


print(ans)
if ans == 'YES':
    print(len(operations))
    for op in operations:
        print(op[0], op[1])