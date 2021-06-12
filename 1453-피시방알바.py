r = int(input())
a = list(map(int, input().split()))
s = set(a)
print(a.__len__() - s.__len__())