a = list(map(lambda x : int(x), input()))
a.sort(reverse=True)
print("".join(list(map(str, a))))