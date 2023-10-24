#Exercise 5: Change Guest List
guest_list = ['To: Tupac', 'To: Eminem', 'To: Kieth Powers', 'To: Tacko Fall']

Not_available_guest = 'To: Tacko Fall'
print(f"Unfortunately, {Not_available_guest} could not make it to the dinner event.")

Guest_replacement = 'To Drake'
guest_list[guest_list.index(Not_available_guest)] = Guest_replacement

print ("Updated Guest List.")
for guest in guest_list:
    print (f"Dear {guest},\n \n Our team would love to formally invite you in this dinner event,\t"
    "\n together with other celebrities like you. Thank you.\n"
    "\n From: Francis Cerezo\n \n")