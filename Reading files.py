#this allows you to open a file in a read function, it will only allow you to read the file and not change anything
#open("employees.txt", "r")

#this allows you to open the file in a write function, it will allow you to modify the file
#open("employees.txt", "w")

#this will allow you to open the file as an append, it will allow you to append to the end of the file
#open("employees.txt", "a")

#opening it this way allows you to open a file and place it in a variable
employee_file = open("employees.txt", "r")

#printing information about the file, first you make sure that it is readable .readable() returns a boolian telling us
#if it is or not
#print(employee_file.readable())

#print the information inside the file
#print(employee_file.read())

#print a line from the file
#print(employee_file.readline())

#readlines allows each line to be placed in an array, you can spesify the index position you want as well
#print(employee_file.readlines()[1])

#you can create a for loop to ask for a certain amount of lines
for employee in employee_file.readlines():
    print(employee)

#make sure you always close a file after you open it
employee_file.close()
