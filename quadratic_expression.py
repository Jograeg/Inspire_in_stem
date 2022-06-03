#!/usr/bin/python

##################################################
#         quadratic_equation
#         name: Jamo
#         date: 31 / 5 / 2022 Monday

import math
a = int(input("enter co-efficient of the first term(a)"))
b = int(input("enter co-efficient of the second term(b)"))
c = int(input("enter the constant(c)"))

#def find_roots(a, b, c):
#    y1 = ((-b + math.sqrt((b**2)-4*a*c)) /(2*a))   
#    y2 = ((+b + math.sqrt((b**2)-4*a*c)) /(2*a)) 
#    print("The roots of the quadratic equation are:",y1,y2)  
#find_roots(a,b,c)

w = math.sqrt((b**2)- 4*a*c)
def find_roots(a, b, c):
    y_1=((-b + w)/(2*a))
    y_2=((+b + w)/(2*a))
    print("The roots of the quadratic equation are:",y_1,y_2) 
find_roots(a,b,c)
