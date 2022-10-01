
from math import sqrt

test_sudoku = []

print("Please enter each line of your sudoku as a list of numbers, then hit enter. For blank spaces use 0")

for i in range(9):
    x = input()
    arr = [int(n) for n in x]
    test_sudoku.append(arr)


# get size of smaller grids
mini_grid_size = int(sqrt(len(test_sudoku)))


#find all positions where there are zeroes
zero_positions = []

for row, i in enumerate(test_sudoku):
    for column, j in enumerate(i):
        if j == 0:
            zero_positions.append({'x': column,'y': row})


# number of zero positions in sudoku
zero_positions_length = len(zero_positions)


# checking function
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

# array for al numbers tried for a certain position. needed for backtracking
numbers_tried = []

for i in range(zero_positions_length):
    numbers_tried.append([])

# main function
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
    
    # array of lists that need checking
    list_of_lists = [horizontal_list, vertical_list, mini_grid_numbers, numbers_tried[count]]
    
    number = 1
    iterator2 = 0

    #this makes sure it does all of the checking functions at least once
    while iterator2 < 4:

        for t in list_of_lists:
            new_number = checking(t, number)
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


for x in test_sudoku:
    print(x)