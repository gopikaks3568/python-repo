#convert the kilogram to pound
# 1 kilo = 2.20
# 1 pound=0.45
weight=input("Enter the weight in kilo(K)or pound(P) ?:")
if weight.lower()=="k":
    print("Chose to enter the weight in kilograms")
    weight_object=float(input("Enter the weight(kg):"))
    print("The weight in pounds:",weight_object*2.20)
elif weight.lower()=="p":
    print("Chose to enter the weight in pounds")
    weight_object=float(input("Enter the weight(lb):"))
    print("The weight in kilograms :",weight_object*0.45)
else:
    print("Invalid entry for the above")
    
 