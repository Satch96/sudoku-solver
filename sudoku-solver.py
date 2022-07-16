
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

# horizontal checker
for i in zero_positions:
    number = 1
    iterator = 0
    while iterator < len(test_sudoku):
        for x in test_sudoku[i['x']]:
            if x == number:
                number +=1
                iterator = 0
                break
            iterator +=1
    test_sudoku[i['x']][i['y']] = number
    number += 1
    iterator = 0


print(test_sudoku)