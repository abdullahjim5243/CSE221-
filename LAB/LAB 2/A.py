N, S = map(int, input().split())
a = list(map(int, input().split()))
left = 0       
right = N - 1  
found = False
while left < right:
    current_sum = a[left] + a[right]
    if current_sum == S:
        print(f"{left + 1} {right + 1}")
        found = True  
        break       
        
    elif current_sum < S:
        left = left + 1     
    else: 
        right = right - 1
if not found:
    print("-1")