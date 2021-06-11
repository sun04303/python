import datetime as dt
a, b = map(int, input().split())
p = int(input())
c = dt.datetime(100,1,1,a,b,0) + dt.timedelta(minutes=p)
re = str(c.time()).split(":")
print(int(re[0]), int(re[1]))