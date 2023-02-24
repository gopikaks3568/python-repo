#Python Program to Print all Prime Numbers in an Interval
#i/p =1,2,3,4,5,6,7,8,9,10   o/p= 2,3,5,7
#i/p = 10,11,12,13,14,15,16  o/p=11,13
start_range=int(input("enter the starting of the interval:"))
end_range=int(input("Enter the ending of the interval:"))
l=[]
for i in range(start_range,end_range):
    l.append(i)
    
print(l)
for i in range(1,num+1):#1,23
    if num%i==0:
        count+=1
        
    else:
        continue
if count==2:
    print("prime no:")
else:
    print("not prime")


    
