
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

#the clear() clears lists of there contence
friends.clear()
print(friends)
