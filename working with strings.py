phrase = "This is a string variable"

print("This is a string\n"
      "This creates a new line\n"
      "\" this adds a quote to strings")

print(phrase)

print(phrase + "This is how you concatenate with strings")

#this changes phrase variable to lower case, .functions
print(phrase.lower())

#this checks to see if the string is lower or upper case only
print(phrase.islower())
print(phrase.isupper())

#this will change phrase to uppercase then check to see if that has happened, functions move left to right
print(phrase.upper().isupper())

#this figures out how many characters are in a string (includes spaces)
print(len(phrase))

#grabs characters from strings [index position]
print(phrase[0])

#this finds the index position of an character spesifide (grabs the first one it finds)
print(phrase.index("a"))

#This replaces words from varaibles
print(phrase.replace("string", "replaced"))


