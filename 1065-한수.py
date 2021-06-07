n = input()
if int(n) < 100:
    print(int(n))
else:
    s = 99
    for i in range(100, n+1):
        if abs(int(i[0]) - int(i[1])) == abs(int(i[1]) - int(i[2])):
            s+=1
    print(s)