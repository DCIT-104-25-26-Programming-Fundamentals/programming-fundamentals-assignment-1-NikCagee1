# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, matrix_number=1):
    matrix = []
    for row_index in range(rows):
        while True:
            row_input = input(f"Enter row {row_index + 1}: ")
            values = row_input.split()
            if len(values) != cols:
                print(f"Error: Please enter exactly {cols} values.")
                continue
            try:
                row = [int(value) for value in values]
                break
            except ValueError:
                print("Error: Please enter only integers.")
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    if not matrix:
        print("Empty matrix")
        return
    width = 0
    for row in matrix:
        for value in row:
            width = max(width, len(str(value)))
    for row in matrix:
        line = " ".join(f"{value:>{width}}" for value in row)
        print(line)


def transpose_matrix(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total
    return result


def get_positive_integer(prompt):
    try:
        value = int(input(prompt))
        if value <= 0:
            print("Error: Value must be a positive integer.")
            return None
        return value
    except ValueError:
        print("Error: Invalid integer input.")
        return None


def main():
    # Part A: Transpose a matrix
    rows = get_positive_integer("Enter number of rows: ")
    if rows is None:
        return
    cols = get_positive_integer("Enter number of columns: ")
    if cols is None:
        return

    print("Enter the matrix values:")
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # Part B: Add two matrices
    print("\n-- Matrix Addition --")
    rows = get_positive_integer("Enter number of rows for both matrices: ")
    if rows is None:
        return
    cols = get_positive_integer("Enter number of columns for both matrices: ")
    if cols is None:
        return

    print("Enter values for matrix A:")
    matrix_a = read_matrix(rows, cols)
    print("Enter values for matrix B:")
    matrix_b = read_matrix(rows, cols)

    sum_matrix = add_matrices(matrix_a, matrix_b)
    print("\nSum Matrix:")
    print_matrix(sum_matrix)

    # Part C: Multiply two matrices
    print("\n-- Matrix Multiplication --")
    rows_a = get_positive_integer("Enter number of rows for matrix A: ")
    if rows_a is None:
        return
    cols_a = get_positive_integer("Enter number of columns for matrix A: ")
    if cols_a is None:
        return
    rows_b = get_positive_integer("Enter number of rows for matrix B: ")
    if rows_b is None:
        return
    cols_b = get_positive_integer("Enter number of columns for matrix B: ")
    if cols_b is None:
        return

    if cols_a != rows_b:
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    print("Enter values for matrix A:")
    matrix_a = read_matrix(rows_a, cols_a)
    print("Enter values for matrix B:")
    matrix_b = read_matrix(rows_b, cols_b)

    product_matrix = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct Matrix:")
    print_matrix(product_matrix)


if __name__ == "__main__":
    main()

