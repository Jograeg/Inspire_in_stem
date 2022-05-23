# learning about listing
motorcycle_owner = "mojo jojo"
plate_number = ['H1234','Z1234','S1234']
motorcycle = ['honda', 'yamaha', 'suzuki']
# accessing list items using index
#print(motorcycle)
#print(motorcycle[0])
# motorcycle[1]= 'bugati' #changing element in alist
#print ("i love "+str(motorcycle[2]))
#motorcycle.append ('bugatti')
#adding element into a list
#motorcycle.append('Bugatti')#adding item into a list
#task --- print the plate number of motorcycles separately
motorcycle_number = motorcycle + plate_number
print(motorcycle_number)
print(motorcycle[0], plate_number[0])
print(motorcycle[1], plate_number[1])
print(motorcycle[2], plate_number[2])
#deleting an item from a list --del
#del motorcycle[0] #deleting an item from a list
print(motorcycle)
popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)
#task print a statement:
#my name is Mojo Jojo and I own a motorcycle plate number:
#print(("my name is ") + str(motorcycle_owner) + " and I own a " + (motorcycle[1]))
print("my name is {} and i own a motorcycle {} with plate number {}" . format(motorcycle_owner,motorcycle[1],plate_number[1]))

#removing an item from a list
motorcycle.remove('honda')
print(motorcycle)

print(motorcycle[-1])
print(motorcycle)
