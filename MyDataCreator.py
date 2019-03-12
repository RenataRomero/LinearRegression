import csv
import random as rnd
import copy
import math


def save_data(filename="airfoil_self_noise_.csv"):

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')

        with open('my_data.csv', 'w') as new_file:

            new_rows = ''
            for row in reader:
                random_number = rnd.random()
                row[-1].rstrip()
                if random_number <= 0.1:  
                    new_rows = new_rows + row[0] + '\n' 
                
            new_file.writelines(new_rows)


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


def get_lines(filename):

    with open(filename, 'r') as new_file:
        row_count = sum(1 for row in new_file)
    
    return row_count

def save_train_and_test():
    with open('my_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')

        with open('my_train.csv', 'w') as new_file_train:
            with open('my_test.csv', 'w') as new_file_test:
                new_rows_train = ''
                new_rows_test = ''
                for row in reader:
                    random_number = rnd.random()
                    if random_number <= 0.75:  
                        new_rows_train = new_rows_train + row[0] + '\n' 
                    else:
                        new_rows_test = new_rows_test + row[0] + '\n'

                new_file_train.writelines(new_rows_train)
                new_file_test.writelines(new_rows_test)

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


def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b

def predict_y(b, x):

    y = b[0][0] + (b[1][0]*float(x[0])) + (b[2][0]*float(x[1])) + (b[3][0]*float(x[2])) + (b[4][0]*float(x[3])) + (b[5][0]*float(x[4]))
    return round(y,4)

def error(y_test, y_prediction):

    y_yp_sum = 0

    i = 0
    for n in y_test:
        dif = n[0] - y_prediction[i]
        y_yp_sum += dif
        i += 1
    
    root = pow(y_yp_sum,2) / (len(y_test))
    error = math.sqrt(root)

    return error


if __name__ == "__main__":
    save_data()
    save_train_and_test()
    a_matrix = build_matrix(6,get_lines('my_train.csv'))
    a_t_matrix = build_t_matrix (get_lines('my_train.csv'), 6)
    y_matrix = build_y_matrix(1,(get_lines('my_train.csv')), 'my_train.csv')

    if can_multiply(a_t_matrix, a_matrix):
        A_AT = multiply_matrix(a_t_matrix, a_matrix)
    else:
        print('Cant multiply a at')

    if can_multiply(a_t_matrix, y_matrix):
        AT_Y = multiply_matrix(a_t_matrix, y_matrix)
        det, b = gauss(A_AT, AT_Y)
        
        print('Este es el vector b:')
        print(b)

        y_predictions = []

        with open('my_test.csv', 'r') as test_file:
            test_reader = csv.reader(test_file, delimiter='\t')
            for n in test_reader:
                y_predictions.append(predict_y(b,n))

            y_test = build_y_matrix(1, (get_lines('my_test.csv')), 'my_test.csv')

            print('\nEste es el error:')
            print(error(y_test, y_predictions))

    else:
        print('Cant multiply at y')

    
