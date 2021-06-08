arr = [-1] * 26

s = list(map(lambda x : ord(x) - 97, input()))
for i, v in enumerate(s):
    if arr[v] == -1: arr[v] = i

print(" ".join(list(map(str, arr))))