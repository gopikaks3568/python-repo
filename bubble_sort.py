l=[]
n=int(input('Enter the no of elements:'))
for i in range(n):
    l.append(int(input('Enter the lsit element:')))
print('The unsorted list is :',l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
         
            print(l)
print('The sorted list is:',l)

