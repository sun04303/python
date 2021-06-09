a, b, c = map(int, input().split())

r = c - b

if r > 0:
    print((a+r)//r)
else :
    print(-1)