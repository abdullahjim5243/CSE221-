n = int(input().strip())

order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rank = {ch: i for i, ch in enumerate(order)}

def custom_key(name):
    return [rank[ch] for ch in name]

trains = []

for idx in range(n):
    line = input().rstrip()
    parts = line.split()
    
    name = parts[0]
    time_str = parts[-1]
    
    hour, minute = map(int, time_str.split(":"))
    total_minutes = hour * 60 + minute
    
    trains.append((name, total_minutes, idx, line))

trains.sort(key=lambda x: (custom_key(x[0]), -x[1], x[2]))

for train in trains:
    print(train[3])
