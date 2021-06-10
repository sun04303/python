r = int(input())

for i in range(r):
    a, b = map(int, input().split())
    if pow(a, b, 10): print(pow(a, b, 10))
    else : print(10)