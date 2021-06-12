import sys

n = int(sys.stdin.readline().strip())
a = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
a1 = list(map(int, sys.stdin.readline().split()))

for i in a1:
    if i in a:print(1)
    else : print(0)