#Exercise 5: No Pastrami
#A list of various sandwiches 
sandwich_orders = ['pastrami','grilled cheese', 'pastrami', 'club', 'pastrami', 'submarine', 'wrap', 'ham and cheese', 'pastrami']
finished_sandwiches = []

#A notification that the deli has run out of partrami
print("Our apologies, but unfortunately the deli has run out of pastrami.")

#Removing all the occurance of 'pastrami' from the list 'sandwich_orders'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#loop through the list of sandwich orders and move them to finished_sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Ma'am/Sir your delightful {current_sandwich} sandwich has been made. We hope you like it!")
    finished_sandwiches.append(current_sandwich)

#A list of the finished sandwiches
print("\nSandwiches that havebeen made:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())
