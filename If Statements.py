# how to create an IF statement
is_male = True
is_tall = True

#how to write an IF statement
if is_male:
    print("You are a male")
else:
    print("You are not a male")

#how to create a or statment
if is_male or is_tall:
    print("You are male or tall")
else:
    print("You are not tall or male")

#how to create an AND statement
if is_male and is_tall:
    print("You are a male and tall")
else:
    print("You are not male or not tall or both")

#How to create an elif (else if)
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall female")
else:
    print("You are a short female")