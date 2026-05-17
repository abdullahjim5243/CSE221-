T = int(input())
for _ in range(T):
  
    k, x = map(int, input().split())
    skipped_count = (k - 1) // (x - 1)
    ans = k + skipped_count
    print(ans)