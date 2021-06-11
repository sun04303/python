import datetime as dt
a, b, c = map(int, input().split())
s = int(input())
d = dt.datetime(100,1,1,a,b,c) + dt.timedelta(seconds=s)
re = str(d.time()).split(":")
print(int(re[0]), int(re[1]), int(re[2]))