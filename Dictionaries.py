#Dictionaries are special stuctures in python which allows us to store information in what are called key value paires

#how to create a dictionary (Keys must be unique)
monthConverstions = {
    #defining the keys "KEY": "Value"
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
#how to print one of the keys
print(monthConverstions["Nov"])

#another way to print some of the keys, this is better practice
print(monthConverstions.get("Jul"))
#best practice due to the printing on None if they key is not found
print(monthConverstions.get("lov", "Not a valid key"))
