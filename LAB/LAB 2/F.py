N, K = map(int, input().split())
A = list(map(int, input().split()))
left = 0
max_length = 0
counts = {}
for right in range(N):
    num = A[right]
    counts[num] = counts.get(num, 0) + 1
    
    while len(counts) > K:
        
        left_num = A[left]
        counts[left_num] = counts[left_num] - 1
        
        if counts[left_num] == 0:
            del counts[left_num]
        left = left + 1
    current_length = right - left + 1
    if current_length > max_length:
        max_length = current_length

print(max_length)