def build_post_order(in_order, pre_order):
    in_index = {val:i for i,val in enumerate(in_order)} 
    n = len(in_order)
    
    res = []
    
    def helper(in_l, in_r, pre_l, pre_r):
        if in_l > in_r:
            return
        
        root = pre_order[pre_l]
        root_idx = in_index[root]
        left_size = root_idx - in_l
  
        helper(in_l, root_idx - 1, pre_l + 1, pre_l + left_size)
   
        helper(root_idx + 1, in_r, pre_l + left_size + 1, pre_r)
      
        res.append(root)
    
    helper(0, n-1, 0, n-1)
    return res


N = int(input())
in_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))

post_order = build_post_order(in_order, pre_order)
print(*post_order)