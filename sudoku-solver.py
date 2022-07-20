
from math import sqrt



test_sudoku = [
    [3,0,0,0],
    [0,2,0,1],
    [1,0,2,0],
    [0,0,0,3]
]

answer = [
    [3,1,4,2],
    [4,2,3,1],
    [1,3,2,4],
    [2,4,1,3]
]


#TO DO

zero_positions = []

#iterate over array and look for 0's
for row, i in enumerate(test_sudoku):
    for column, j in enumerate(i):
        if j == 0:
            zero_positions.append({'x': column,'y': row})
        
# checking functions

# horizontal checker
# for i in zero_positions:
#     number = 1
#     iterator = 0
#     while iterator < len(test_sudoku):
#         for x in test_sudoku[i['y']]:
#             if x == number:
#                 number +=1
#                 iterator = 0
#                 break
#             iterator +=1
#     test_sudoku[i['y']][i['x']] = number
#     number += 1
#     iterator = 0

#vertical checker
# for i in zero_positions:
#     number = 1
#     iterator = 0
#     while iterator < len(test_sudoku):
#         vertical_list = [row[i['x']] for row in test_sudoku]
#         for x in vertical_list:
#             if x == number:
#                 number +=1
#                 iterator = 0
#                 break
#             iterator +=1
#     test_sudoku[i['y']][i['x']] = number
#     number += 1
#     iterator = 0


# grid checker
mini_grid_size = int(sqrt(len(test_sudoku)))

for i in zero_positions:

    #get coordinates that need to be checked
    x_start = int(i['x']/mini_grid_size) * mini_grid_size
    y_start = int(i['y']/mini_grid_size) * mini_grid_size

    #iterate over mini grids
    mini_grid_numbers = []

    for j in range(mini_grid_size):
        for k in range(mini_grid_size):
            mini_grid_numbers.append(test_sudoku[y_start + j][x_start + k])
    
    number = 1
    iterator = 0
    while iterator < len(test_sudoku):
        for x in mini_grid_numbers:
            if x == number:
                number +=1
                iterator = 0
                break
            iterator +=1
    test_sudoku[i['y']][i['x']] = number
    number += 1
    iterator = 0

print(test_sudoku)