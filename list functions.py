
#a list
lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#this is printing out a list
print(friends)

#this is an exstend fuction, it allows you to take one list and append another list on the end of it
friends.extend(lucky_numbers)
print(friends)

#append() is used to add another item onto the end of the list
friends.append("Creed")
print(friends)

#insert(index pos, data item) allows you to insert an item of data into a list
friends.insert(1, "Kelly")
print(friends)

#removes spesific elements from a list
friends.remove("Jim")
print(friends)

#pop() gets ride of the top item of the list
friends.pop()
print(friends)

#the index() can be used to find if there is a value inside of the list, tells me the index pos
print(friends.index("Kevin"))

#the count() allows you to find out how many elements in a list have that value
print(friends.count("Karen"))

#sort() allows the list to be sorted in alphabetical order for stings and assending order for ints
lucky_numbers.sort()
print(lucky_numbers)

#reverse() allows you to reverse the items in a list
lucky_numbers.reverse()
print(lucky_numbers)

#copy() allows you to copy a list to another list
friends2 = friends.copy()
print(friends2)

#the clear() clears lists of there contence
friends.clear()
print(friends)
