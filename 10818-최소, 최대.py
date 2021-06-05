a = int(input())

arr = [1000001, -1000001]

num = list(map(int, input().split()))

for i in num:
    if(i < arr[0]):
        arr[0] = i
    if(i > arr[1]):
        arr[1] = i

print(str(arr).replace(",", "").replace("[", "").replace("]", ""))