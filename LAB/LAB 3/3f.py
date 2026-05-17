def build_min_height_order(arr):
    res = []
    
    def helper(l, r):
        if l > r:
            return
        mid = (l + r) // 2
        res.append(arr[mid])
        helper(l, mid - 1)
        helper(mid + 1, r)
    
    helper(0, len(arr) - 1)
    return res


n = int(input())
arr = list(map(int, input().split()))

ans = build_min_height_order(arr)
print(*ans)