s = list(input())
s.insert(0, "a")
for i in range(1, s.__len__()):
    print(s[i], end="")
    if(i != 0 and i%10 == 0) : print()