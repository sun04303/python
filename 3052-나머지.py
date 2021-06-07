num = []

for i in range(0, 10):
    n = int(input())
    num.append(n%42)

result = set(num)
print(list(result).__len__())