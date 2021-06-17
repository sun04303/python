while 1:
    n = list(map(int, input()))
    if sum(n) == 0 :break
    print("yes" if n == list(reversed(n)) else "no")