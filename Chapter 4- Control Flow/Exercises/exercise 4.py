#Exercise 4: Stages of Life
#Getting the input of the person's age
age = int(input("enter the age of the person:"))

#If-elif-else chain to determine the person's stage of life based on the value of the age variable
if age < 2:

    #If the person is less than 2, the printed message would identify as a baby
    print("This person is a baby.")

elif age < 4:

    #ELif if the persn if atleast 2 but less than 4, the printed message would identify as a toddler
    print("The person is a toddler.")

elif age < 13:

    #ELif if the persn if atleast 4 but less than 13, the printed message would identify as a kid
    print("The person is a kid.")

elif age < 20:

    #ELif if the persn if atleast 13 but less than 20, the printed message would identify as a teenager
    print("The person is a teenager.")

elif age < 65:

    #ELif if the persn if atleast 20 but less than 65, the printed message would identify as a adult
    print("The person is an adult.")

else:

    #Else if the age is 65 or older, the printed message would identify as an elder
    print("The person is an elder")
