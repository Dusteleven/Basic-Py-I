# Write your solution here



def transpose(matrix:list):

    for r in range(len(matrix)):
        for c in range(r, len(matrix)):
            temp = matrix[r][c]
            matrix[r][c]=matrix[c][r]
            matrix[c][r]=temp
    print()

    










if __name__ == "__main__":

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)