#!/usr/bin/python


##################################################
#         functions in tuples
#         name: Jamo 
#         date: 31 / 5 / 2022 Monday



#list
fruits = ['mango', 'banana', 'watermelon', 'apple']
fruits[2]= 'orange'
print(fruits)

# tuple: we cannot edit
fruits2 = ('mango', 'guava', 'banana', 'lime')
#fruits2[2]='apple' # doesn't work

cars = ('audi', 'bmw', 'vw', 'toyota')
cars = ('nissan', 'bmw', 'vw', 'toyota')
print(cars)

# fav_food
fav_food = ('kuku', 'omena', 'ugali', 'githeri')
for fav_food in fav_food:
    print(fav_food)