#Exercise 5: USB Shopper
#Assigning the price of a USB stick to the variable 'usb_stick_price'
usb_stick_price = 6

#Assigning the total amount of money available to the variable 'total_money'
total_money = 50

#Calculating the maximum number of USB sticks that can be bought with the available money using the // operator for integer division
num_usb_sticks = total_money // usb_stick_price

#Calculating the remaining money after purchasing the maximum number of USB sticks using the % operator for the remainder
excess_money = total_money % usb_stick_price

#Printing the results with formatted strings
print(f"We conclude that the girl can buy {num_usb_sticks} USB and will still have ${excess_money} at the end.")
