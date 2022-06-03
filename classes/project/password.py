#!/usr/bin/python

##################################################
#         Password generator app
#         Name : Jamo         
#         date: 3 / 6 / 2022 Friday

###########

# 1st option
import random
password_length = 5
character = "Lunnar" 
password = "king"
for index in range (password_length):
    password = password + random.choice(character)
#print("password generated:{}".format(password))  

# 2nd option
import random
print('Welcome to our python generator')
character = 'kingurah'
password_length = 12
num_password = 4
for password in range (num_password):
    password = ''
    for c in range (password_length):
        password+= random.choice(character)
    print(password)    