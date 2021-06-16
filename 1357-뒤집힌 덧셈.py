a, b = map(int, input().split())

def r(n):
    return int(str(n) [::-1])
print(r(r(a)+r(b)))