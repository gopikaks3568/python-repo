#pythom program showcase how swapping is done
import time as t
f_var=float(input("Enter the first value:"))
s_var=float(input("Enetr the seconf Value:"))
print("The first variable entered:",f_var)
print("The second variable entered:",s_var)
print("Swaping in progress")
f_var,s_var=s_var,f_var #swapped
print("After swaping")
t.sleep(1)
print("The updated first variable is :",f_var)
print("The updated second variable is :",s_var)
