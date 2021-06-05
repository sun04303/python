len=0
li=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a = int(input())
b = int(input())
c = int(input())

num=a*b*c

for i in range(0, 10):
    li[i]=num%10
    num=num/10
    if(num<1):
        break
    len += 1

for i in range(0, len+1):
    for j in range(0, 10):
        if(li[i]==j):
            count[j]=count[j]+1;

for i in count:
    print(i)