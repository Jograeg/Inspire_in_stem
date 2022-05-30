#!/usr/bin/python

person= {'name' : 'James', 'Id' : '589000' ,'location' : 'Nairobi', 'gender' : 'male' }
print(person['name'] ,person['Id'] , person['location'] ,person['gender'])
print(person['name'])
print(type[person])
print(person)
del person['location']
print(person)

#looping over dictionaries
#for key, value in person.items():
    #print(f"{key}:{value}")


#color=['blue','green','red','yellow','purple']
#i = 0
#while i < len(color):
    #if(color[3]=='yellow'):
        #print(color[3].upper())  
        #i+=1  

# using get to access the value in a dictionary
print(person.get('age',"location key is is non-existent "))
print(person.get('gender'))