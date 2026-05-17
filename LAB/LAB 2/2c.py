import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Store value with original index
arr_with_index = sorted((arr[i], i + 1) for i in range(n))

for i in range(n - 2):
    left = i + 1
    right = n - 1
    first_val = arr_with_index[i][0]

    while left < right:
        current_sum = first_val + arr_with_index[left][0] + arr_with_index[right][0]

        if current_sum == k:
            print(arr_with_index[i][1],
                  arr_with_index[left][1],
                  arr_with_index[right][1])
            sys.exit()

        elif current_sum < k:
            left += 1
        else:
            right -= 1

print(-1)