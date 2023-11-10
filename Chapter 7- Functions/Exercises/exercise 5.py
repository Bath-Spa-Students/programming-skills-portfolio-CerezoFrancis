#Exercise 5: Cities
#Defining the describe_city function with a default country
def describe_city(city, country='Unknown'):
    print(f"{city} is in {country}.")

#Calling the function for three different cities
describe_city("Italy", "Southern Europe")
describe_city("Dubai", "United Arab Emirates")
describe_city("Texas", "United State of America")
#Using a default country
describe_city("California")
