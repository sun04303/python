import collections as cl
a, a1 = [], []
r = int(input())
for i in range(r):
    a.append(input()[0])

cnt = cl.Counter(a)
if cnt.most_common(1)[0][1] < 5 : print("PREDAJA")
else :
    for i in cnt.most_common():
        if i[1] >= 5 : a1.append(i[0])
    a1.sort()
    print("".join(a1))