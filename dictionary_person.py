person= {'name' : 'James', 'Id' : '589000' ,'location' : 'Nairobi', 'gender' : 'male' }
print(person['name'] ,person['Id'] , person['location'] ,person['gender'])
person['age']='21'
person['color']='blue'
person['phone_number']='078654328'
#print(person['name'])
#print(type[person])
#print(person)
del person['location']
print(person)

#looping over dictionaries
for key, value in person.items():
    print(f"{key}:{value}")


color=['blue','green','red','yellow','purple']
i = 0
while i < len(color):
    if(color[1]=='green'):
        print(color[1].upper())  
        i+=1  