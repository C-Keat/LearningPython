#calling a class from another file
#from "file name" import "class name"
from Student import Student

#creating objects form a class
student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

#print the output of a function in an object
print(student2.on_honor_roll())
