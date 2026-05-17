N = int(input())
train = [None] * N

for i in range(N):
    inp = input()
    inp_list = inp.split()
    tr_name = inp_list[0]
    dep_time = inp_list[-1]
    train[i] = [tr_name, dep_time, i, inp]  

for j in range(N):
    for k in range(N - 1):
        tr_1 = train[k]
        tr_2 = train[k + 1]
        name_1, time_1, idx_1 = tr_1[0], tr_1[1], tr_1[2]
        name_2, time_2, idx_2 = tr_2[0], tr_2[1], tr_2[2]

        flag = False

        if name_1 > name_2:
            flag = True
        elif name_1 == name_2:
            if time_1 < time_2:
                flag = True
            elif time_1 == time_2:
           
                if idx_1 > idx_2:
                    flag = True
        if flag:
            train[k], train[k + 1] = train[k + 1], train[k]
for i in train:
    print(i[3])