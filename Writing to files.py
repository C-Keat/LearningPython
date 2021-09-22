#this allows us to open a file so that we can append it/add another element to the end of the file
employee_file = open("employees.txt", "a")
#how to add - in order to add a new element at the end of a file you must use the \n to make sure it creates a new line
employee_file.write("\nKelly - customer service")
#close the file
employee_file.close()

#employee_file = open("employees.txt","w") this will delete all the elements in this file and rewrite it with new