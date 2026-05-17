import sys
from bisect import bisect_left, insort

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        M = int(input_data[idx+1])
        idx += 2
        
        tasks = []
        for _ in range(N):
            s = int(input_data[idx])
            e = int(input_data[idx+1])
            tasks.append((s, e))
            idx += 2
            
        tasks.sort(key=lambda x: (x[1], x[0]))
        
        free_times = [-1] * M
        tasks_completed = 0
        
        for s, e in tasks:
            pos = bisect_left(free_times, s) - 1
            
            if pos >= 0:
                free_times.pop(pos)
                insort(free_times, e)
                tasks_completed += 1
                
        out.append(str(tasks_completed))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()