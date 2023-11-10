#Exercise 4: Deli
#A list of various sandwiches
sandwich_orders = ['grilled cheese', 'club', 'submarine', 'wrap', 'ham and cheese']
#Empty the list to store the finished sandwiches
finished_sandwiches = []

#Looping through the list of sandwiches orders
while sandwich_orders:
    #Retrieve and remove the first sandwich order
    current_sandwich = sandwich_orders.pop(0)
    #For all the sandwich that has been made this message will be printed
    print(f"Ma'am/Sir your delightful {current_sandwich} sandwich has been made. We hope you like it!")
    #with every finished sandwich it will be added to the list of finished sandwiches
    finished_sandwiches.append(current_sandwich)

#A list of the finished sandwiches
print("\nSandwiches that have been made:")
for sandwich in finished_sandwiches:
    #Printing each finished sandwich with the fist letter capitalized
    print(sandwich.capitalize())
