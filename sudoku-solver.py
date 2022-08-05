
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

    if len(type) == 0:
        pass
    else:
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

# need to add something adds number for a particular zero position. so during the checks can also check that number
numbers_tried = []

# goes through all zero positions and checks to see if number already used
zero_positions_length = len(zero_positions)

for i in range(zero_positions_length):
    numbers_tried.append([])


count = 0
while count < zero_positions_length:

    i = zero_positions[count]
    
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

    #this makes sure it does all of the checking functions at least once
    while iterator2 < 4:

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
        new_number = checking(numbers_tried[count], number)
        if new_number != number:
            number = new_number
            iterator2 = 1
        else:
            number = new_number
            iterator2 += 1

    if number > 9:
        test_sudoku[i['y']][i['x']] = 0
        numbers_tried[count] = []
        count-=1
    else:
        test_sudoku[i['y']][i['x']] = number
        numbers_tried[count].append(number)
        count +=1


print(test_sudoku)