#Exercise 3: Stripping Names
#Storing the strring with the leading and trailing whitespacr characters in the variable 'name' 
name = "\t Francis Cerezo\n"

#Printing the original string
print ("Unmodified:")
print (name)

#Using the lstrip() method to remove the leading whitespace characters
print ("\nUsing lstrip():")
print (name.lstrip())

#Using the rstrip() method to remove the trailing whitespace characters
print ("\nUsing rstrip():")
print (name.lstrip())

#Using the lstrip() method to remove both the leading and trailing whitespace characters
print ("\nUsing strip():")
print (name.strip())
