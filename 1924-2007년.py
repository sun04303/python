import datetime as dt
t=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
a, b = map(int, input().split())
c = dt.datetime(2007,a,b,0,0,0)
print(t[c.weekday()])