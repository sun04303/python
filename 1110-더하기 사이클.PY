num1 = 0
num2=0
sum=0

arr = [0, 0]
arr1 = [0, 0]

num = int(input())

if(num<10):
    arr[0]=0
    arr[1]=num

else:
    arr[0]=(num%100) - (num%10)
    arr[0]=arr[0]/10
    arr[1]=num%10

while(1):
    sum += 1
    num1 = arr[0] + arr[1];
    if(num1<10):
        arr1[0]=0;
        arr1[1]=num1;
    
    else:
        arr1[0]=(num1%100) - (num1%10);
        arr1[0]=arr1[0]/10;
        arr1[1]=num1%10;
    
    num2 = (arr[1]*10) + arr1[1];
    
    if(num==num2):
        break
    
    else:
        arr[0]=(num2%100) - (num2%10);
        arr[0]=arr[0]/10;
        arr[1]=num2%10;
    
print(sum)