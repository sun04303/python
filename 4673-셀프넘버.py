arr = [0] * 10000
for i in range(1, 10000):
    if i < 10:
        s = i + i
        arr[s] = 1
    elif i<100:
        s = i + i//10 + i%10
        arr[s] = 1
    elif i<1000:
        s = i + i//100 + i%100//10 + i%10
        arr[s] = 1
    elif i<10000:
        s = i+i//1000+i%1000//100+i%100//10+i%10
        if s<10000:
            arr[s] = 1

for j in range(1, 10000):
    if arr[j] != 1:
        print(j)
