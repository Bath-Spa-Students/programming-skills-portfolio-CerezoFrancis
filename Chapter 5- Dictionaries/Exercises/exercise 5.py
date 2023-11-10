#Exercise 5: Pets
#Creating a dictionary with different pets and their owners
pet1 = {'animal': 'hamster', 'owner': 'Brian'}
pet2 = {'animal': 'cat', 'owner': 'Naomi'}
pet3 = {'animal': 'parrot', 'owner': 'Logan'}
pet4 = {'animal': 'dog', 'owner': 'Brandon'}

#Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]

#looping through the list and printing everything known about each pet
for pet in pets:
    print(f"This pet {pet['animal']} would fit perfectly with {pet['owner']}.\n")
