#a basic list - with lists inside the list
number_grid = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [0]
]
#how to print from a 2D list
print(number_grid[0][0])

#nested for loops - how to print the whole 2D list
for row in number_grid:
    for col in row:
        print(col)
