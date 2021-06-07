num = int(input())

numbers = list(map(int, input().split()))
max = max(numbers)
sum = 0

for i in map( lambda x : (x/max) *100 , numbers):
    sum += i

print(sum / num)