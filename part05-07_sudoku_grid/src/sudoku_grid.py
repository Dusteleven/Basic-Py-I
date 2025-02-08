# Write your solution here


def row_correct(sudoku: list, row_no: int):
    for i in range(1,9,1):
        if sudoku[row_no].count(i)>1:
            return False
    return True    


def block_correct(sudoku: list, row_no: int, column_no: int):
    testList = []
    correct = False
    for i in range(row_no,row_no+3,1):
        for j in range(column_no,column_no+3,1):
            c = (sudoku[i][j])
            if  c!= 0 and testList.count(c) ==0:
                testList.append(c)
            elif c!=0 and testList.count(c) >0:
                return False
    return True

def column_correct(sudoku: list, column_no: int):
    fakeRow = []
    for rows in sudoku:
        fakeRow.append(rows[column_no])
    for i in range(1,9,1):
            if fakeRow.count(i) > 1:
                     return False
    return True



def sudoku_grid_correct(sudoku: list):
     
    for  r in range(0,9,1):
          if not row_correct(sudoku,r): 
               return False

    for c in range(0,9,1):
        if not column_correct(sudoku, c):
             return False

    for i in range(0,9,3):
        for j in range (0,9,3):
             if not block_correct(sudoku,i ,j): 
                  return False

    return True
     



if __name__ == "__main__":

    sudoku = [
        [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
        [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
        [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
        [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
        [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
        [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
        [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
        [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
        [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
        ] 

    print(sudoku_grid_correct(sudoku))

    