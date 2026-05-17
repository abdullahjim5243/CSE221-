import sys
sys.setrecursionlimit(200000)

def merge_sort_count(arr):
    n = len(arr)
    if n <= 1:
        return 0, arr
    
    mid = n // 2
    left_inv, left_sorted = merge_sort_count(arr[:mid])
    right_inv, right_sorted = merge_sort_count(arr[mid:])
    
    merge_inv = 0
    i = 0
    j = 0
    merged = []
    len_left = len(left_sorted)
    len_right = len(right_sorted)
    
    while i < len_left and j < len_right:
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
            merge_inv += (len_left - i)
            
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])
    
    return left_inv + right_inv + merge_inv, merged

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        a = []
        for _ in range(n):
            a.append(int(next(iterator)))
    except StopIteration:
        return

    inv_count, _ = merge_sort_count(a)
    print(inv_count)

if __name__ == '__main__':
    main()