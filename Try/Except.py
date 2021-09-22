#try and except allows you to handle errors
try:
    number = int(input("Enter a number: "))
    print(number)
#this except is too broad it will catch any and all errors inside of the try
#this could be made more spesific to be more useful
except:
    print("Exception thrown")

try:
    fail = 1/0
    number = int(input("Enter a number: "))
    print(number)
#this except methord allows you to catch spesific types of errors that could accure
except ZeroDivisionError:
    print("Divided by zero error")
except ValueError:
    print("Wrong value error")
