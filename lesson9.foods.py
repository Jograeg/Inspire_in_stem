#!/usr/bin/python

# if statements

age = 43
if age >= 18 :
    print("you are allowed to drive")
else:
    print("you are not allowed")


mary_fav_food = ['beef' , 'chicken' , 'vegetables']
jane_fav_food = ['rice' , 'ugali' , 'potatoes']
# dictionary containing the above
food = {
    'mary':['beef','chicken','vegetables'],
    'jane':['rice','ugali','potatoes'],
}
#print(food)

for key , value in food.items():
    print(f"{key}:{value}")