#!/usr/bin/python

##################################################
#         Password generator app
#         Name : Jamo         
#         date: 3 / 6 / 2022 Friday

###########

class employee:
    def __init__(self, _name, _id, _salary):
        self.name = _name
        self.salary = _salary
        self.id = _id

    def sayHi(self):
        print("Hi,my name is " + self.name, "my ID number is " + self.id, "my salary is " + self.salary)
employee1 = employee("James", str(308769), str(600000))
employee1.sayHi()      