from collections import deque
s = deque(range(1, int(input())+1))

while len(s) > 1 :
    s.popleft()
    s.rotate(-1)
print(s[0])