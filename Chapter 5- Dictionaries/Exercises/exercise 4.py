#Exercise 4: Rivers
#Creating a dictionary of the major rivers and the countries they run through
major_rivers = {'nile': 'egypt',
                'amazon': 'brazil',
                'Mississippi-Missouri-Red Rock': 'U.S. states'}

#Creating a loop and adding sentence to each one
for river, country in major_rivers.items():
    print(f"The {river.title()} river is one of the longest river and is located in {country.title()}.\n")

#Printin the names of each river in my dictionary
print("\n Names of the rivers:")
for river in major_rivers:
    print(river.title())

#Printing the names of each country included in the dictionary
print("\n Names of the countries:")
for country in major_rivers.values():
    print(country.title())
