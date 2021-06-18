import collections as cl
max = 0
r = int(input())
for _ in range(r):
    li = list(map(int, input().split()))
    li.sort()
    cnt = cl.Counter(li)

    if cnt.most_common(1)[0][1] == 3 : 
        if 10000 + (cnt.most_common(1)[0][0] * 1000) > max:max = 10000 + (cnt.most_common(1)[0][0] * 1000)
    elif cnt.most_common(1)[0][1] == 2 : 
        if 1000 + (cnt.most_common(1)[0][0] * 100) > max:max=1000 + (cnt.most_common(1)[0][0] * 100)
    else : 
        if 100*li[-1] > max:max = 100*li[-1]
print(max)