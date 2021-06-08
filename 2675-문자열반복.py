r = int(input())

for i in range(r):
    n, s = input().split()
    for j in s:
        print(j*int(n), end='')
    print()