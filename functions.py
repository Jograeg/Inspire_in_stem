#!/usr/bin/python

##################################################
#         functions in python
#         name: James 
#         date: 31 / 5 / 2022 Monday

# functions = it is a block of code put together
# initialising functions 
# calling functions

#def say_hello():
 #   print("Hello from JKUAT")
  #  x = 4
   # y = 7
   # z = x + y
   # print(z)
#say_hello()   

#def barks():
#    print(" dog barks woof woof")
#def meow():    
#    print(" cat meow meow ")
#def neigh ():    
#    print(" donkey neigh neigh")
#barks()
#meow()
#neigh()

#def add_numbers(x,y):
#    sum_numbers = x + y 
#    print ("The sum of numbers:",sum_numbers)
#add_numbers(40,50)
#add_numbers(100,500) 
#add_numbers(1,4) 

#def prod_numbers(x,y):
#    prod_numbers = x * y
#    print("The prod of numbers:",prod_numbers)
#prod_numbers(10,5)
#prod_numbers(100,300)
#prod_numbers(785,90000)

def print_name(name = "James"):
    print(name)
print_name("Grace") 

# return from a function 
def get_sum(num1, num2):
    sum_nums = num1 + num2
    return sum_nums 
print(get_sum(7,12))

# square of numbers
def powers(number, powers):
    powers = number **powers
    return powers
print(powers(6,4))  

def get_full_name(f_name, s_name):
    full_name = f_name + s_name
    return full_name
print(get_full_name("James ", "Kimoda")) 

# returning a dictionary from a function
def create_full_name(first_name, second_name):
    person = {'first':first_name,'second':second_name}
    return person
student = create_full_name("Grace","Kimonjino")
print(student)

# Passing a list in a function
def greet_friends(names):
    for name in names:
        msg = "Hello " +name.title() + "!"
        print (msg)
friends = ['Rebecca', 'Stephanie', 'Kendi', 'Grace']
greet_friends(friends)


