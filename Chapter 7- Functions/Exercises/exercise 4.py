#Exercise 4:  Large Shirts
#Defining the make_shirt function with default values
def make_shirt(size="Large", message="I love Python"):
    print(f"The size of this shirt is {size} with a print on the shirt that says: {message}")

#Calling the function to create a large shirt with the default messaeg
make_shirt()

#Calling the function to create a medium shirt with the default message
make_shirt("medium")

#Calling the function to create a small shirt with a different message
make_shirt("small", "In coding we trust")
