r = int(input())

for _ in range(r):
    s = list(map(lambda y : "".join(y), list(map(lambda x : list(reversed(x)), input().split()))))
    print(" ".join(s))