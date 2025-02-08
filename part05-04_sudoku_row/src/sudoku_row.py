# Write your solution here

def row_correct(sudoku: list, row_no: int):

    
    for i in range(1,9,1):
        if sudoku[row_no].count(i)>1:
            return False
    return True    
        

if __name__ == "__main__":
    go = [[0, 1, 0, 2, 2, 1, 0], [2, 1, 2, 0, 2, 1, 2], [1, 2, 2, 0, 0, 2, 1], [1, 2, 1, 2, 2, 0, 1], [1, 0, 1, 0, 2, 0, 1], [0, 2, 0, 0, 1, 1, 0], [2, 2, 0, 0, 1, 0, 2]]
    print(row_correct(go)) 

