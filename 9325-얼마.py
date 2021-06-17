import sys
input = sys.stdin.readline
r = int(input())

for _ in range(r):
    s = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        s += q*p
    print(s)