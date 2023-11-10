#Exercise 1: Alien Colors
#Getting the input for the alien's color
alien_color = (input("Enter the color of the alien: "))

#An If-else chain to check how many points will be gained when it presents a certain color.
if alien_color == 'green':
    
    #If the alien is green, the player gains 5 points
    print("Well done! You have now gained 5 points.")

elif alien_color == 'yellow':
    
    #If the elien is yellow, the player gains 10 points 
    print("Well done! You have now gained 10 points.")

else:
    #If the alien is neither green nor yellow, the player gains no points
    print("Unfortunately, you have not gained any points.")
