#Exercise 3: T-Shirt
#Defining the make_shirt function
def make_shirt(size, message):
    print(f"The size of this shirt is {size} with a print on the shirt that says: {message}")

#Calling the function using positional arguments
make_shirt("medium", "I love Python")

#Calling the function using keyword arguments
make_shirt(size="large", message="In coding we trust")
