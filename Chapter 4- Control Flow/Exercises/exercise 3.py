#Exercise 3: Alien Colors
#ENTER THE COLOR OF THE ALIEN VERSION
alien_color = (input("Enter the color of the alien: "))

#If-else-if chain to check the alien's color and provide appropriate points
if alien_color == 'green':
    
    #If the alien's color is green, it will print the message gaining 5 points
    print("Well done! You have now gained 5 points.")

elif alien_color == 'yellow':

    #Elif the alien's color is yellow, it will print the message gaining 10 points
    print("Well done! You have now gained 10 points.")

else:

    #Else if the alien's color is either green nor yellow, it will automatically be red
    print("Well done! You have now gained 15 points.")
