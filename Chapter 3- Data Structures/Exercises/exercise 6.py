#Exercise 6: Shrinking Guest List
guest_list = ['To: Tupac', 'To: Eminem', 'To: Kieth Powers', 'To: Tacko Fall']

print("Unfortunately there has been a shoratage of table space, therefor we can only invite two people for the dinner event.")

while len(guest_list) > 2:
    removed_guest= guest_list.pop()
    print(f"Our apologies {removed_guest}, for the sudden changes but we are not able to invite you to dinner.")

for guest in guest_list:
    print(f"\n Fortunately Mr.{guest}, we would still want to invite you to our dinner event.\n"
          "\n -Francis Cerezo \n")
    
del guest_list[0]
del guest_list[0]
