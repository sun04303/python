n = int(input())
s = list(input())
a = []
for i in s:
    if i != "J" and i != "A" and i != "V" : a.append(i)

if a.__len__() == 0 : print("nojava")
else : print("".join(a))