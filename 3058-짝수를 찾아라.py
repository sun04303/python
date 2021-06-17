r = int(input())

for _ in range(r):
    li = sorted(list(filter(lambda x: x%2 == 0, list(map(int, input().split())))))
    print(sum(li), li[0])