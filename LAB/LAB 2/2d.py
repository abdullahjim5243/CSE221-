import sys

def main():
    input = sys.stdin.readline
    
    N = int(input())
    A = list(map(int, input().split()))
    
    M = int(input())
    B = list(map(int, input().split()))
    
    i = j = 0
    merged = []
    merged_extend = merged.extend  # local binding (faster)
    
    while i < N and j < M:
        if A[i] <= B[j]:
            merged.append(str(A[i]))
            i += 1
        else:
            merged.append(str(B[j]))
            j += 1
    
    # append remaining in one step (faster than loop)
    if i < N:
        merged_extend(map(str, A[i:]))
    if j < M:
        merged_extend(map(str, B[j:]))
    
    sys.stdout.write(" ".join(merged))

if __name__ == "__main__":
    main()