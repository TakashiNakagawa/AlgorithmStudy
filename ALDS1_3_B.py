n, q = map(int, input().split())
name_time = []
for index in range(0, n):
    input_val = input().split()
    name_time.append([input_val[0], int(input_val[1])])

total_time = 0
while(len(name_time) > 0):
    if name_time[0][1] <= q:
        total_time += name_time[0][1]
        print(name_time[0][0], total_time)
        name_time.pop(0)
    else:
        total_time += q
        name_time[0][1] -= q
        val = name_time[0]
        name_time.pop(0)
        name_time.append(val)


