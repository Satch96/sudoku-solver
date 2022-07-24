
from math import sqrt


test_sudoku = [
    [5,0,9,0,0,0,0,0,7],
    [0,8,0,0,1,0,5,2,0],
    [0,0,3,0,8,4,0,0,1],
    [0,9,0,7,0,0,0,0,2],
    [4,0,0,0,5,0,3,9,0],
    [8,0,2,1,0,0,0,0,4],
    [0,0,0,3,0,2,0,0,5],
    [0,4,0,0,0,0,7,0,0],
    [1,0,7,0,9,0,0,8,0]
]


# get size of smaller grids
mini_grid_size = int(sqrt(len(test_sudoku)))


zero_positions = []

#iterate over array and look for 0's
for row, i in enumerate(test_sudoku):
    for column, j in enumerate(i):
        if j == 0:
            zero_positions.append({'x': column,'y': row})
        
# checking functions

def checking(type, number):

    iterator = 0
    #get difference between current number and 1 so you know how much to iterate
    diff = number - 1

    while iterator < len(test_sudoku) - diff:
        for x in type:
            if x == number:
                number +=1
                iterator = 0
                break
            iterator +=1
    
    return number


    

#combine all 3 checking functions:

for i in zero_positions:
    
    horizontal_list = test_sudoku[i['y']]
    vertical_list = [row[i['x']] for row in test_sudoku]

    #get coordinates that need to be checked
    x_start = int(i['x']/mini_grid_size) * mini_grid_size
    y_start = int(i['y']/mini_grid_size) * mini_grid_size

    #iterate over mini grids
    mini_grid_numbers = []

    for j in range(mini_grid_size):
        for k in range(mini_grid_size):
            mini_grid_numbers.append(test_sudoku[y_start + j][x_start + k])
    
    number = 1

    iterator2 = 0

    while iterator2 < 3:

        new_number = checking(horizontal_list, number)
        if new_number != number:
            number = new_number
            iterator2 = 1
        else:
            number = new_number
            iterator2 += 1
        new_number = checking(vertical_list, number)
        if new_number != number:
            number = new_number
            iterator2 = 1
        else:
            number = new_number
            iterator2 += 1
        new_number = checking(mini_grid_numbers, number)
        if new_number != number:
            number = new_number
            iterator2 = 1
        else:
            number = new_number
            iterator2 += 1

    test_sudoku[i['y']][i['x']] = number



print(test_sudoku)