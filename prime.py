#Python Program to Check Prime Number
count=0
num=int(input("Enter the number:"))#23
for i in range(1,num+1):#1,23
    if num%i==0:
        count+=1
        
    else:
        continue
if count==2:
    print("prime no:")
else:
    print("not prime")


