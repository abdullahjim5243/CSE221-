N, M, K =map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

i=0
j=M-1

ii = i 
jj = j 
diff= abs(a[i]+b[j]-K)
while i<N and j>=0:
    sum = a[i]+b[j]
    diff_curr = abs(sum - K)

    if diff_curr<diff:
        diff = diff_curr
        ii = i
        jj = j
    if sum<K:
        i+=1
    elif sum>K:
        j-=1
    else:
        break       
print(f'{ii+1} {jj+1}')