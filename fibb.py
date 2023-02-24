n=int(input('Enter the range:'))
a=0
b=1
for i in range(n):
    print(a,' ',' ',end='')
    c=a
    a=b
    b=a+c
