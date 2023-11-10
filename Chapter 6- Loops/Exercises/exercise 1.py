#Exercise 1: Pizza Toppings
#Prompt the user to enter pizza toppings 
print("Enter the pizza toppings you want to add. Enter 'done' to finish.")

#Initializing an empty list to store the selected pizza toppings
pizza_toppings = []

#Continuosly prompt the user to enter toppings until 'done' is entered
while True:
    topping = input("Enter a pizza topping: ")
    
    #If 'done' is entered break out of the loop
    if topping.lower() == 'done':
        break
    else:
        #Add the entered topping to the list
        pizza_toppings.append(topping)
        #Printing a message for eac topping added
        print(f"Adding {topping} to your pizza.")

#Printing the final list of the pizza toppings or inform the user if no toppings were selected
if pizza_toppings:
    print("\n Your pizza will have the following toppings:")
    for topping in pizza_toppings:
        print(topping)
else:
    print("You didn't select any toppings for your pizza.")
