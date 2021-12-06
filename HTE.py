"""
In HTE company
Rotate matrix on 90 degree
"""

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
out1 = [[7,4,1],[8,5,2],[9,6,3]]
matrix2 = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16],
          ]
out2 = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
matrix3 = [[1]]
out3 = [[1]]
matrix4 = [[1, 2], [3, 4]]
out4 = [[3, 1], [4, 2]]

matrixs = [matrix1, matrix2, matrix3, matrix4]
outs = [out1, out2, out3, out4]

def rotate(matrix):
    def transpose(matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def reflect(matrix):
        r = len(matrix) - 1
        for i in range(int(len(matrix) / 2)):
            for j in range(len(matrix)):
                matrix[j][i], matrix[j][r - i] = matrix[j][r - i], matrix[j][i]
        return matrix

    matrix = transpose(matrix)
    matrix = reflect(matrix)
    return matrix

for matrix, out in zip(matrixs, outs):
    assert rotate(matrix) == out