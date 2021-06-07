num = int(input())

for i in range(num):
    numbers = list(map(int, input().split()))
    n = numbers.pop(0)
    svg = (sum(numbers) / len(numbers))
    cnt = 0

    for j in numbers:
        if j > svg: cnt += 1
    result = (cnt/n) * 100

    print('%0.3f' % result + '%')