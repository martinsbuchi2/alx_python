#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    new_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values of the current row
        new_row = []
        # Iterate over each element in the row and square it
        for value in row:
            squared_value = value ** 2
            # Append the squared value to the new row
            new_row.append(squared_value)
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    # Return the new matrix with squared values
    return new_matrix