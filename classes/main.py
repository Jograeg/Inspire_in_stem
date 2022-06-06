#!/usr/bin/python

##################################################
#         Main
#         Name : Jamo         
#         date: 6 / 6 / 2022 Monday

import operations
from students import student
from teachers import Teachers

print(operations.add_numbers(3,5))
print(operations.subtract_numbers(7,8))
print(operations.mult_numbers(9,7))
print(operations.div_numbers(4,7))

student = student("Jamo ","cycling ",1940)
student.greet_student()

new_teacher = Teachers(" Mr ofweneke " ,12345 ,"Maths ",1000000 )
print(new_teacher.get_tsc_no())