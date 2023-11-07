#Exercise 3: Print date and Time
#Manipulating the dates and times by importing datetime
import datetime

#Using the datetime.now() method to store the current date and time in the 'now' variable
now = datetime.datetime.now()

#Printing the message "Current date and time :"
print("Current date and time : ")

#Using the the specified format of the strftime() method and printing the current date and time
print (now. strftime("%Y-%m-%d %H:%M:%S"))
