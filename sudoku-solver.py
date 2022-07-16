from cgi import test


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
            zero_positions.append({'x': row,'y': column})
        
# checking functions

for i in zero_positions:

    print(test_sudoku[i['x']][i['y']])

