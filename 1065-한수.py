n = input()
if int(n) < 100:
    print(int(n))
else:
    s = 99
    for i in range(100, int(n)+1):
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]): s+=1
    print(s)