#!/usr/bin/python

#program to write numbers in reverse
#input is 700
#output is 007

num = 1234
reversed_num = 0 

while num != 0:
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number: " + str(reversed_num))    




