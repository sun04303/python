import sys
r = int(sys.stdin.readline().rstrip())
li = []
for _ in range(r):
    li.append(int(sys.stdin.readline().rstrip()))

li.sort(reverse=True)
for i in li:
    print(i)