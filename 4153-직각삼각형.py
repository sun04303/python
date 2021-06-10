while 1:
    li = list(map(lambda x: int(x) ** 2, input().split()))
    if sum(li) == 0 : break
    li.sort()

    if li[0] + li[1] == li[2]:print("right")
    else : print("wrong")