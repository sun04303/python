import sys
a = []
for i in range(int(sys.stdin.readline().rstrip())):
    s = list(map(str, sys.stdin.readline().split()))
    if s[0] == "push" : a.append(int(s[1]))
    elif s[0] == "pop" : 
        try: print(a.pop(0))
        except IndexError: print(-1)
    elif s[0] == "size" : print(a.__len__())
    elif s[0] == "empty" :
        if a : print(0)
        else : print(1)
    elif s[0] == 'front' : 
        try: print(a[0])
        except IndexError: print(-1)
    else :
        try: print(a[-1])
        except IndexError: print(-1)