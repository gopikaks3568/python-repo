#Python Program to Find the Factorial of a Number
#5! = 5*4*3*2*1
enter_num=int(input("Enter the number:"))
mul=1
while enter_num:
    mul=mul*(enter_num-1)
print("The factorial:",mul)
