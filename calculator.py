print("MENU")
print("""
1.Add
2.Subtract
3.Multiply
4.Divide
5.Exit """)
cont="y"

while (cont):
    ch=int(input("Enter the choie(1/2/3/4/5):"))
    if ch==1:
        print("Add")
        a=float(input("Enter the 1st no:"))
        b=int(input("Enter the 1st no:"))
        print("The sum of",a,"and",b,"is",a+b)
    if ch==2:
        print("Subtract")
        a=int(input("Enter the 1st no:"))
        b=int(input("Enter the 1st no:"))
        print("The difference of ",a,"and",b,"is",a-b)
    if ch==3:
        print("Multiply")
        a=int(input("Enter the 1st no:"))
        b=int(input("Enter the 1st no:"))
        print("The product of ",a,"and",b,"is",a*b)
    if ch==4:
        print("Divide")
        a=int(input("Enter the 1st no:"))
        b=int(input("Enter the 1st no:"))
        print("The division of ",a,"and",b,"is",a/b)
    if ch==5:
        print("Chose to exit")
        break
    cont=input("Do you wish to continue(y/n):")
    if cont !="y":
        break



        


