n = int(input())
if n == 0:
    print(0)
    exit()
arr = [1] * 2
for i in range(2, n):
    arr.append(arr[i-2] + arr[i-1])
print(arr[-1])