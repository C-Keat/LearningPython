#from the student file, import the student class
from Student import Student

#above is how you import a class
#below is how you create an object of a class

student1 = Student("Jim", "Business", 3.1, False)

#this will print out differnet attributes of the object/class
print(student1.major)
#this will print out the name of the student
print(student1.name)
print(student1.gpa)


student2 = Student("Pam", "Art", 3.3, False)

