import tkinter as tk
from sudokusolver import sudokuSolver 

root = tk.Tk()

root.geometry('500x500')
root.title('Sudoku Solver')


inputframe = tk.Frame(root)

# create sudoku grid
for x in range(9):
    inputframe.columnconfigure(x,weight=1)

# create validation to only allow single digits in boxes
def onlyDigit(digit):
    if digit.isdigit() and int(digit) > 0 and int(digit) < 10:
        return True
    elif digit == '':
        return True
    else:
        return False

reg = root.register(onlyDigit)

entries = []
i = 0
for x in range(81):
    if x%9 == 0:
        i +=1
    input = tk.Entry(inputframe)
    input.config(validate='key',validatecommand=(reg,'%P'))
    input.grid(row=i,column=x%9, sticky=tk.W+tk.E)
    entries.append(input)

inputframe.pack(fill='x')

def addEntries(sudoku):
    entries.clear()
    i = 0
    for x in range(81):
        a,b = divmod(x,9)
        if x%9 == 0:
            i +=1
        input = tk.Entry(inputframe)
        input.insert(0,sudoku[a][b])
        input.config(state='readonly')
        input.grid(row=i,column=x%9, sticky=tk.W+tk.E)
        entries.append(input)

# call back function on button click to solve
def solve():
    
    sudoku = []
    temp = []
  
    for count,entry in enumerate(entries):
        
        if count%9 == 0 and count > 0:
            sudoku.append(temp)
            temp = []
        
        if entry.get() == '':
            value = 0
        else:
            value = int(entry.get())
        
        temp.append(value)
    
    sudoku.append(temp)
    x = sudokuSolver(sudoku)
    addEntries(x)

def clear():
    entries.clear()
    i = 0
    for x in range(81):
        if x%9 == 0:
            i +=1
        input = tk.Entry(inputframe)
        input.config(validate='key',validatecommand=(reg,'%P'))
        input.grid(row=i,column=x%9, sticky=tk.W+tk.E)
        entries.append(input)
            

solveButton = tk.Button(root, text='Solve',command=solve)
solveButton.pack()
clearButton = tk.Button(root, text='Clear', command=clear)
clearButton.pack()

root.mainloop()