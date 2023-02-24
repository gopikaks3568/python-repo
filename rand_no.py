#python program to print random number
import random as r 
n=int(input("Enter the number of random numbers :"))
for i in range(n):
    print(r.random())#random no.s btw 0 and 1 
    print(r.randint(1,100))#random no.s btw given range
    print(r.randrange(1,100,10))#random no.s btw 2 no.s skipping some no.s in btw
    print("______________________________________")

    