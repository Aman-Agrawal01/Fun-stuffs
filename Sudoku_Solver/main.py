#Solving using backtracking 

# Firstly finding the free space 
def find_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==-1:
                return row,col
    # If not found
    return None,None

#If the guessed number is valid (not necessarily be true)
def number_is_valid(puzzle,number,row,col):
    row_values = puzzle[row]

    # If the number is found in row and column return False
    if number in row_values:
        return False
    col_values = [puzzle[i][col] for i in range(9)]
    if number in col_values:
        return False

    # Now check in the square
    start_row = (row//3)*3
    start_col = (col//3)*3
    for r in range(start_row,start_row+3):
        for c in range(start_col,start_col+3):
            if number == puzzle[r][c]:
                return False
    
    # If none of them return False then the number is valid but not necessarily true always
    return True

#Function for returning whether sudoku is solvable or not
def solve(puzzle):
    row , col = find_empty(puzzle)

    if row is None:
        return True 
    
    for number in range(1,10):
        if number_is_valid(puzzle,number,row,col):
            puzzle[row][col]=number
            if solve(puzzle)==True:
                return True
    # If the guessed number comes out to be false then reset it to -1
    puzzle[row][col]=-1
    # If the puzzle is unsolvable after recursion return False 
    return False

if __name__=='__main__':
    sudoku = [
   [5,3,-1,     -1,7,-1,    -1,-1,-1],
   [6,-1,-1,     1,9,5,      -1,-1,-1],
   [-1,9,8,     -1,-1,-1,   -1,6,-1],
   [8,-1,-1,    -1,6,-1,    -1,-1,3],
   [4,-1,-1,    8,-1,3,     -1,-1,1],
   [7,-1,-1,    -1,2,-1,    -1,-1,6],
   [-1,6,-1,    -1,-1,-1,   2,8,-1],
   [-1,-1,-1,   4,1,9,      -1,-1,5],
   [-1,-1,-1,   -1,8,-1,    -1,7,9]]
    if solve(sudoku)==True:
        print("The sudoku is solvable")
        print(sudoku)
    else:
        print("It's impossible to solve it")