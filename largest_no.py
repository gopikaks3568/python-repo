#Python Program to Find the Largest Among Three Numbers
f_num=float(input("Enter the 1st number:"))
s_num=float(input("Enter the 1st number:"))
t_num=float(input("Enter the 1st number:"))
if f_num>s_num and f_num>t_num:
    print("The largest number is:",f_num)
elif s_num>f_num and s_num>t_num:
    print("The largest number is:",s_num)
elif t_num>f_num and t_num>s_num:
    print("The largest number is:",t_num)
else:
    print("nothing much :)")

