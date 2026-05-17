def build_pre_order(in_order, post_order):
    in_index = {val:i for i,val in enumerate(in_order)}
    n = len(in_order)
    res = []

    def helper(in_l, in_r, post_l, post_r):
        if in_l > in_r:
            return
        
        root = post_order[post_r]  
        res.append(root)
        root_idx = in_index[root]
        left_size = root_idx - in_l

        helper(in_l, root_idx - 1, post_l, post_l + left_size - 1)
       
        helper(root_idx + 1, in_r, post_l + left_size, post_r - 1)
    
    helper(0, n-1, 0, n-1)
    return res


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pre_order = build_pre_order(in_order, post_order)
print(*pre_order)