#Exercise 3: Glossary 2
#Creating a glossary with words that I have learned from previous chapters 
glossary =  {
    'variable': 'A named reference to a value that can be changed.',
    'string': 'A collection of alphabets, words orother characters.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'import': 'To make a code in one module available in another.',
    'concatenation': 'Joining two or more strings to create a single new string.'
}

#Printing each word and its meaning
print("Original glossary:")
print(f"Variable: \t{glossary['variable']}\n")
print(f"String: \t{glossary['string']}\n")
print(f"Function: \t{glossary['function']}\n")
print(f"Import: \t{glossary['import']}\n")
print(f"Concatenation: \t{glossary['concatenation']}\n")

#Adding new python terms to my glossary
glossary['List'] = 'A collection of items in a particular order.'
glossary['Elif'] = 'A short term for "else if" and used when the first statement is not true .'
glossary['Loop'] = 'A programming construct that repeats a group of statements.'
glossary['Integer'] = 'A whole number that does not include a decimal point.'
glossary['Float'] = 'A function that will convert any value into a decimal or fractional number.'

#Printing the updated glossary with new terms
print("Updated glossary:")
for word, meaning in glossary.items():
    print(f"{word.title()}: \t{meaning}\n")
