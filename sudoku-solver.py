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

#iterate over array and look for 0's
for row, x in enumerate(test_sudoku):
    for column, y in enumerate(x):
        if y == 0:
            pass
            #print(row,column)
        
#horizontal line checking function
print(test_sudoku[0][2])
#vertical line checking function

#grid line checking function

