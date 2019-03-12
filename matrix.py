import csv

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

def build_matrix(columns, rows):

    matrix = [[1 for x in range(columns)] for y in range(rows)]
    
    i = 0
    with open('my_train.csv', 'r') as new_file:
        filewriter = csv.reader(new_file, delimiter='\t')
        for row in filewriter:
            for j in range(0, columns):
                if j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = float(row[j-1])
            i += 1


    return matrix

def build_t_matrix(columns, rows):

    matrix = [[1 for x in range(columns)] for y in range(rows)]
    j = 0
    with open('my_train.csv', 'r') as new_file:
        filewriter = csv.reader(new_file, delimiter='\t')
        for row in filewriter:
            for i in range(rows):
                
                matrix[i][j] = float(row[i])
            j += 1

    temp_matrix =  [[1 for x in range(150)] for y in range(1)]

    temp_matrix += matrix

    temp_matrix.pop(-1)
    return matrix

def build_y_matrix(columns, rows, filename):

    matrix = [[0 for x in range(columns)] for y in range(rows)]
    i = 0
    with open(filename, 'r') as new_file:
        filewriter = csv.reader(new_file, delimiter='\t')
        for row in filewriter:
            matrix[i][0] = float(row[5])
            i+=1

    return matrix

def can_multiply(a, b):

    a_columns = len(a[0])
    b_rows = len(b)

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