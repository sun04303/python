n = int(input())
r = 0;

while n % 5 != 0:
    if n < 3 :
        print(-1)
        exit()

    r += 1
    n -= 3

r += n//5
print(r)