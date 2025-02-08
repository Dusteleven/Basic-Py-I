# Write your solution here


def row_sums(my_matrix: list):

    for rows in my_matrix:
        s=0
        for cols in rows:
            s+= cols
        rows.append(s)




if __name__ == "__main__":    
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)