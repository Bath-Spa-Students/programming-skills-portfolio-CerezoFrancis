#Exercise 5: Change Guest List
#Creating a list of guest names and assigning it to the variable 'guest_list'
guest_list = ['To: Tupac', 'To: Eminem', 'To: Kieth Powers', 'To: Tacko Fall']

#Storing the name of the guest who is not available in the variable 'Not_available_guest' and printing a message
Not_available_guest = 'To: Tacko Fall'
print(f"Unfortunately, {Not_available_guest} could not make it to the dinner event.")

#Creating a replacement guest and updating the 'guest_list' with the new guest
Guest_replacement = 'To Drake'
guest_list[guest_list.index(Not_available_guest)] = Guest_replacement

#Printing the updated guest list
print ("Updated Guest List.")
for guest in guest_list:
    print (f"Dear {guest},\n \n Our team would love to formally invite you in this dinner event,\t"
    "\n together with other celebrities like you. Thank you.\n"
    "\n From: Francis Cerezo\n \n")
