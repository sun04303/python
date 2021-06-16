a, b = sorted(map(int, input().split()))
    
li = list(range(a+1, b))
print(li.__len__())
for i in li :
    print(i, end=" ")