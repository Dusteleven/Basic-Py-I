# Write your solution here


def column_correct(sudoku: list, column_no: int):
    fakeRow = []

    for rows in sudoku:
        fakeRow.append(rows[column_no])

    for i in range(1,9,1):
            if fakeRow.count(i) > 1:
                     return False
    return True
        





if __name__ == "__main__":
    go = [[0, 1, 0, 2, 2, 1, 0], [2, 1, 2, 0, 2, 1, 2], [1, 2, 2, 0, 0, 2, 1], [1, 2, 1, 2, 2, 0, 1], [1, 0, 1, 0, 2, 0, 1], [0, 2, 0, 0, 1, 1, 0], [2, 2, 0, 0, 1, 0, 2]]
    print(column_correct(go)) 