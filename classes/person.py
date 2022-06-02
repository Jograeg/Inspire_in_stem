#!/usr/bin/python

##################################################
#         Classes
#         Name : jamo         
#         date: 2 / 6 / 2022 Thursday

class person: 
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def sayHi(self):
        print('Hello, my name is '+ self.name,  ' I am ' + self.age + ' years old.')    
person1 = person("James",str(69))    
person1.sayHi()
person2 = person("Kimonjino",str(40))
person2.sayHi()