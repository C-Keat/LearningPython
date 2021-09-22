#Exponent function allows us to take a number and raise it to a power

#this is 2 to the power of 3
print(2**3)


#if i wanted to create my own id do this
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 5))
