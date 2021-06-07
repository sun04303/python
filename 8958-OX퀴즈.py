num = int(input())

for i in range(num):
    sum = 0
    s = input().split("X")
    while '' in s:
        s.remove('')
    for j in s:
        for k in range(1, len(j) + 1):
            sum += k
    print(sum)