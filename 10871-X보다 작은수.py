n, x = map(int, input().split())

num = list(map(int, input().split()))
number = []
for i in num:
    if(i < x):
        number.append(i)

print(" ".join(map(str, number)))