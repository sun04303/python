import collections as cl
li = list(map(int, input().split()))
li.sort()
cnt = cl.Counter(li)

if cnt.most_common(1)[0][1] == 3 : print(10000 + (cnt.most_common(1)[0][0] * 1000))
elif cnt.most_common(1)[0][1] == 2 : print(1000 + (cnt.most_common(1)[0][0] * 100))
else : print(100*li[-1])