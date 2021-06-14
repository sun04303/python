import sys
from collections import deque
dq = deque()
for i in range(int(sys.stdin.readline().rstrip())):
    s = deque(map(str, sys.stdin.readline().split()))
    if s[0] == "push" : dq.append(int(s[1]))
    elif s[0] == "pop" : 
        if (not dq) : print(-1)
        else : print(dq.popleft())
    elif s[0] == "size" : print(len(dq))
    elif s[0] == "empty" :
        if dq : print(0)
        else : print(1)
    elif s[0] == 'front' : 
        if (not dq) : print(-1)
        else : print(dq[0])
    else :
        if (not dq) : print(-1)
        else : print(dq[-1])