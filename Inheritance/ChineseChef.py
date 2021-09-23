#this Chinese Chef can do everything that the chef can do and will inherit from the chef class
#this is how to perform inheritance
from Chef import Chef
class ChineseChef(Chef):

    def make_fried_rice(self):
        print("Chef makes fried rice")

#Polymothafis takes place by replacing the same function name with different actions
    def make_special_dish(self):
        print("chef makes yellow chicken")

