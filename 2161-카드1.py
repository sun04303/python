from collections import deque
s = deque(range(1, int(input())+1))

while len(s) > 0 :
    print(s.popleft(), end=" ")
    s.rotate(-1)