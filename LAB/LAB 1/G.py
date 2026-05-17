T = int(input()) 

for _ in range(T):
    N = int(input()) 
    student_ids = list(map(int, input().split()))
    student_marks = list(map(int, input().split()))


    students = []
    for i in range(N):
        students.append((student_ids[i], student_marks[i], i))   
    sorted_students = sorted(students, key=lambda x: (-x[1], x[0], x[2]))
    visited = [False] * N
    swaps = 0
    for i in range(N):
        if visited[i] or sorted_students[i][2] == i:
            continue
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = sorted_students[j][2]
            cycle_size += 1
        if cycle_size > 1:
            swaps += cycle_size - 1
    print(f"Minimum swaps: {swaps}")
    for student in sorted_students:
        print(f"ID: {student[0]} Mark: {student[1]}")