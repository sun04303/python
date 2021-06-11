r = int(input())
for _ in range(r):
    a = list(map(str, input().split()))
    s = float(a[0])
    for i in range(1, a.__len__()):
        if a[i] == "@" : s *= 3
        elif a[i] == "%": s += 5
        else: s-=7
    print("{:.2f}".format(s))