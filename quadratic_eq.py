#Program for Solution of Quadratic equation
#not working
import time as t
import math as m
a=float(input("Enter the cofficient of X^2:"))
b=float(input("Enter the cofficient of X: "))
c=float(input("Enter the contant:"))
print("The entered equation:",a,"x^2+",b,"X+",c,"=0")
print("The solution of the above equation")
for i in range(2):
    t.sleep(1)
x=(-b+m.sqrt(m.pow(b,2)-(4*a*c)))/2*a
print("Solution is:",x)
