def build_matrix(columns, rows):

    matrix = [[0 for x in range(columns)] for y in range(rows)]

    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(input("Enter number in position (row,column) " + str(i) + ", " + str(j) + ":\n"))

    print_matrix(matrix)
    print("Matrix build!")
    return matrix

def can_multiply(a, b):

    a_columns = len(a[0])
    b_rows = len(b)

    print("\nA Columns: " + str(len(a[0])))
    print("B Rows: " + (str(len(b))))

    if a_columns == b_rows:
        return True
    else:
        return False

def multiply_matrix (a, b):
    a_columns = len(a[0])
    a_rows = len(a)
    b_columns = len(b[0])

    matrix = [[0 for x in range(b_columns)] for y in range(a_rows)]
    result = 0

    for i in range(a_rows):
        for k in range(b_columns):
            for j in range(a_columns):
                result += a[i][j]*b[j][k]

            matrix[i][k] = result
            result = 0
    
    return matrix

def print_matrix(matrix):
    longest_len = 1    

    for row in matrix:
        for n in row:
            if len(str(n)) > longest_len:
                longest_len = len(str(n))

    longest_len += 1

    for row in matrix:
        for n in row:
            n_len = len(str(n))
            n_spaces = longest_len - n_len
            print (" " + str(n) + " "*n_spaces + "|", end='', flush=True)
        n_spaces = 1
        print("")

def main():
    print("Enter the number of columns and rows for matrix A:")
    a_n_columns = int(input("Columns:\n"))
    a_n_rows = int(input("Rows:\n"))
    
    a_matrix = build_matrix(a_n_columns, a_n_rows)

    print("Enter the number of columns and rows for matrix B:\n")
    b_n_columns = int(input("Columns:\n"))
    b_n_rows = int(input("Rows:\n"))

    b_matrix = build_matrix(b_n_columns, b_n_rows)  
    
    if can_multiply(a_matrix,b_matrix):
        result_matrix = multiply_matrix(a_matrix, b_matrix)
        print("\nResult:\n")
        print_matrix(result_matrix)
    else:
        print("You can't multiply this matrixes")

main()