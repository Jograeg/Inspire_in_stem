#!/usr/bin/python

####################
#    Dictionaries
#    Loops : for loops
#    Name : James NJai
#    Date : 23 / 5 / 2022
###################


# Initializing dictionaries 
student = {"Name" : "James", "age" : 25, "gender" : "male"}
print(student)
print(student["Name"])
print(student["age"])
print(student["gender"])

# Adding key value pairs in a dic

student["Id.No"] = "400786"
student["hobby"] = "eating"
student["club"] = "manchester united"
student["favourite_color"] = "blue"
print(student)

# Empty dictionary
student2 = {} 
student2["fav_food"] = "chapati"
student2["home_city"] = "Nairobi"
student2["repair"] = "Laptops"
print(student2)


# Modify values in a dictionary
student = {'Name': 'Ronald'}
print(student)
del student2 ["fav_food"]
print(student2)


for number in range (1,100):
    print(number)
    