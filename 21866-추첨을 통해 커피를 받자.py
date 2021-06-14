a = list(map(int, input().split()))
s = [100, 100, 200, 200, 300, 300, 400, 400, 500]
for i, v in enumerate(a) :
    if v > s[i] : 
        print("hacker")
        exit()
if sum(a) >= 100 :
    print("draw")
    exit()
print("none")