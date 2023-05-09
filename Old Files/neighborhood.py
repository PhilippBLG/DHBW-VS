import random


def create_matrix(height, width):
    smallmatrix = []
    matrix = []
    for row in range(height):
        for cell in range(width):
            smallmatrix.append(random.randint(0, 99))
        matrix.append(smallmatrix)
        smallmatrix = []
    return matrix


def is_largest_neighbor(matrix, row, column):
    is_largest = False
    number = matrix[row][column]
    number_left = 0
    number_right = 0
    number_top = 0
    number_bottom = 0

    if column != 0:
        number_left = matrix[row][column-1]
    if column != len(matrix[row])-1:
        number_right = matrix[row][column+1]
    if row != 0:
        number_top = matrix[row-1][column]
    if row != len(matrix)-1:
        number_bottom = matrix[row+1][column]

    if number > number_left and number > number_right and number > number_top and number > number_bottom:
        is_largest = True
    return is_largest


def find_largest_neighbors(matrix):
    neighbors = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if is_largest_neighbor(matrix, row, column):
                neighbors.append(matrix[row][column])

    return neighbors
