num = []

for i in range(10):
    num.append(int(input())%42)

print(set(num).__len__())