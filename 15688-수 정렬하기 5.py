import sys
r = int(input())
li = []
for _ in range(r):
    li.append(int(sys.stdin.readline().rstrip()))
li.sort()
for i in li:
    print(i)