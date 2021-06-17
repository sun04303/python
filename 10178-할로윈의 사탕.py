r = int(input())

for _ in range(r):
    a, b = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(a//b, a%b))