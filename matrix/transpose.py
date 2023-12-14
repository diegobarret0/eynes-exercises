def transpose(matrix):

    transpose_matrix = []

    for i in range(len(matrix[0])):
        transpose_matrix.append([row[i] for row in matrix])
    
    return transpose_matrix

matrix = [[5, 6, 3],[2 ,3 ,4]]
print(transpose(matrix))
