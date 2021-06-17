r = int(input())

for _ in range(r):
    a, b = map(int, input().split())
    print((a-b) - 2 if  (a-b) > 2 else 2 - (a-b))