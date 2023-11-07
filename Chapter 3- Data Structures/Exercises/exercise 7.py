#Exercise 7: Seeing the World
#Creating a list of places to visit and assigning it to the variable 'places_to_visit'
places_to_visit = ['Texas', 'Maldives', 'Japan', 'Hawaii', 'Canada']

#Printing the original order of the list
print("Original order:", places_to_visit)

#Printing the sorted order of the list using the sorted() function
print("Sorted order:", sorted(places_to_visit))

#Printing the original order of the list
print("Original order:", places_to_visit)

#Printing the reverse sorted order of the list using the sorted() function with the reverse parameter
print("Reverse sorted order:", sorted(places_to_visit, reverse=True))

#Printing the original order of the list
print("Original order:", places_to_visit)

#Reversing the order of the list using the reverse() method
places_to_visit.reverse()
print("Reversed order:", places_to_visit)

#Reversing the order of the list again to revert it to the original order
places_to_visit.reverse()
print("Original order:", places_to_visit)

#Sorting the list in place using the sort() method
places_to_visit.sort()
print("Sorted order:", places_to_visit)

#Sorting the list in reverse order in place using the sort() method with the reverse parameter
places_to_visit.sort(reverse=True)
print("Reverese sorted order:", places_to_visit)
