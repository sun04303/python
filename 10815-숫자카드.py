import sys

n = int(sys.stdin.readline().strip())
a = set(map(int, sys.stdin.readline().split()))

n1 = int(sys.stdin.readline().strip())
a1 = list(map(int, sys.stdin.readline().split()))

for i in a1:
    if i in a: print(1, end=" ")
    else : print(0, end=" ")



# import sys
# n = int(sys.stdin.readline().strip())
# getNum = set(map(int,sys.stdin.readline().split()))
# m = int(sys.stdin.readline().strip())
# checkNum = list(map(int,sys.stdin.readline().split()))
# for i in checkNum:
#     if i in getNum:
#         print(1)
#     else:
#         print(0)