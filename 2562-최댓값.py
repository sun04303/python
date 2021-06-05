max = 0
q = 0

for i in range (1, 10):
    num = int(input())
    if(num > max):
        max = num
        q = i

print(max)
print(q)