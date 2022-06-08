#!/usr/bin/python

##################################################
#         Palindrome
#         Name : Jamo         
#         date: 8 / 6 / 2022  Wednesday

###########

#program += check 18
#number or letter is
#palyndrome

    #Task
#+ Ask user to select which input to check number or letter
#+ After user enters their input the program it should print based on the input inserted.

my_str = 'oyo'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")    


# another one
num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("Not a palindrome!")       

