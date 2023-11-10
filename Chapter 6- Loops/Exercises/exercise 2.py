#Exercise 2: Movie Tickets
#Prompt for entering the person's age
person_age = ("Enter the person's age: ")

while True:
    #Input the person's age
    person = input(person_age)
    if person =='Done':
        break
    #Converting the input into interger
    person = int(person)

    if person < 3:
        #If the person's age is under 3 it will print the message below
        print("Congratulations, your ticket if free!")

    elif person <13:
        #If the person's age is under 3 to 12 it will print the message below
        print("Your ticket value would be 10$")

    else:
        #If the person's age is above 12 it will print the message below
        print("Your ticket value would be 15$")   
