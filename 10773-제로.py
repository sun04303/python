import sys
from collections import deque
r = int(sys.stdin.readline().rstrip())
li = deque()
for i in range(r) :
    n = int(sys.stdin.readline().rstrip())
    if n == 0: li.pop()
    else : li.append(n)
print(sum(li))