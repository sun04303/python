r, n = 0, 0
for _ in range(4):
    a, b = map(int, input().split())
    n = (n + b) - a
    if r < n : r=n
print(r)