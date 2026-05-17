N, K = map(int, input().split())
a = list(map(int, input().split()))
left = 0
current_sum = 0
max_length = 0

for right in range(N):
    current_sum = current_sum + a[right]
    while current_sum > K:
        current_sum = current_sum - a[left]
        left = left + 1
    current_length = right - left + 1
    if current_length > max_length:
        max_length = current_length
print(max_length)