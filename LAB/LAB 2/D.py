N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
i = 0 
j = 0
result = [] 
while i < N and j < M:
    if A[i] <= B[j]:
        result.append(A[i])
        i = i + 1
    else:
        result.append(B[j])
        j = j + 1

while i < N:
    result.append(A[i])
    i = i + 1

while j < M:
    result.append(B[j])
    j = j + 1

for num in result:
    print(num, end=" ")
print()