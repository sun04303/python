r = int(input())

for i in range(1, r+1):
    a, b = map(int, input().split())
    print('Case #{0}: {1}'.format(i, a+b))