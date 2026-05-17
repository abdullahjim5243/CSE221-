count = 0

def merge(a, b):
    global count
    i = 0
    j = 0
    res = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            count += len(a) - i
            j += 1

    while i < len(a):
        res.append(a[i])
        i += 1

    while j < len(b):
        res.append(b[j])
        j += 1

    return res


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


n = int(input())
arr = list(map(int, input().split()))

sorted_arr = mergeSort(arr)

print(count)
print(*sorted_arr)