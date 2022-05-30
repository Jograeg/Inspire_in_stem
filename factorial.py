#!/usr/bin/python

# factorial 
#factorial=(number * (number-1))
#n! = n * (n-1)*(n-2)*(n-3)
#6! = 6*5*4*3*2*1 
number = int(input("enter the number"))
factorial = 1
if (number) < 0 :
    print("factorial of negative numbers does not exist")
elif (number) == 1:
    print("factorial of 0 = 1")    
else :
    for i in range( 1,number+1): 
        factorial = factorial * i 
print("factorial of number :",factorial)       