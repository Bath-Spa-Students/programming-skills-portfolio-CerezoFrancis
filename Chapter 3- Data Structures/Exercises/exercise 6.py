#Exercise 6: Shrinking Guest List
#Creating a list of guest names and assigning it to the variable 'guest_list'
guest_list = ['To: Tupac', 'To: Eminem', 'To: Kieth Powers', 'To: Tacko Fall']

#Printing a message about the shortage of table space and the need to limit the number of invites
print("Unfortunately there has been a shoratage of table space, therefor we can only invite two people for the dinner event.")

#Removing guests from the list until only two guests remain
while len(guest_list) > 2:
    removed_guest= guest_list.pop()
    print(f"Our apologies {removed_guest}, for the sudden changes but we are not able to invite you to dinner.")

#Printing the remaining guests who are still invited
for guest in guest_list:
    print(f"\n Fortunately Mr.{guest}, we would still want to invite you to our dinner event.\n"
          "\n -Francis Cerezo \n")
    
#Deleting the remaining elements in the list
del guest_list[0]
del guest_list[0]
