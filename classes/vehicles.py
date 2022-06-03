#!/usr/bin/python

##################################################
#         vehicle classes
#         Name : jamo         
#         date: 3 / 6 / 2022 Friday

class vehicle:
    def __init__(self, _milage, _speed):
        self.milage = _milage
        self.speed = _speed

    def Woah(self):
        print("Woah! that cars milage is " + self.milage,"MPG " "it goes at a speed of " + self.speed, "Km/hr")
vehicle1 = vehicle(str(10000), str(3600))    
vehicle1.Woah()
mercedes = vehicle(str(6007), str(544))
mercedes.Woah()


