#python program for finding the area of a triangle
import string as s 
import math as m
print("TYPES OF TRIANGLE")
print("""
1.Isoceleus triangle
2.Euqiateral triangle
3.right angled triangle
4.scalene triangle 
""")

yes="y"
while yes=="y":
    ch=int(input("Enter the choice(1/2/3/4):"))
    if ch==1:
        print("Chose Isoceleus triangle")
        equal_side=float(input("Enter the side:"))
        unequal_side=float(input("Enter the 3rd side:"))
        print("The area of the triangle is :",(1/2)*equal_side*unequal_side)
    elif ch==2:
        print("Chose Equilateral triangle")
        side=float(input("Enter the side:"))
        print("Area of the triangle",side**3)
    elif ch==3:
        print("Chose right angled triangle")
        base=float(input("Enter the base:"))
        ht=float(input("Enter the height :"))
        print("The are of the trianlge is:",(1/2)*base*ht)
    elif ch==4:
        print("Chose scalene triangle ")
        f_side=float(input("Enter the 1st side:"))
        s_side=float(input("Enter the 2nd side:"))
        t_side=float(input("Enter the 3rd side:"))
        s=(f_side+s_side+t_side)/3
        print("The area of the triangle :",m.sqrt(s*(s-f_side)*(s-s_side)*(s-t_side)))
    else:
        print("invalid entery")
    yes=input("Do you wish to continue(y/n):")
    if yes.lower()!="y":
        break





