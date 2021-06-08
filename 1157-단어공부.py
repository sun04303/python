import collections as cl

s = input().upper()
if s.__len__() == 1:
    print(s)
else :
    cnt = cl.Counter(s)
    print("?" if cnt.most_common(1)[0][1] == cnt.most_common(2)[1][1] else cnt.most_common(1)[0][0])