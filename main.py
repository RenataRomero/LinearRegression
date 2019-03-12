import math
import matrix
import error
import linear_regression as lr
import data_creator as data
import csv


if __name__ == "__main__":
    data.save_data()
    data.save_train_and_test()
    a_matrix = matrix.build_matrix(6,data.get_lines('my_train.csv'))
    a_t_matrix = matrix.build_t_matrix (data.get_lines('my_train.csv'), 6)
    y_matrix = matrix.build_y_matrix(1,(data.get_lines('my_train.csv')), 'my_train.csv')

    if matrix.can_multiply(a_t_matrix, a_matrix):
        A_AT = matrix.multiply_matrix(a_t_matrix, a_matrix)
    else:
        print('Cant multiply a at')

    if matrix.can_multiply(a_t_matrix, y_matrix):
        AT_Y = matrix.multiply_matrix(a_t_matrix, y_matrix)
        b = lr.gauss(A_AT, AT_Y)

        print('Este es el vector b:')

        for i in range(len(b)):
            print('b' + str(i) + ': ' + str(b[i]))

        y_predictions = []

        with open('my_test.csv', 'r') as test_file:
            test_reader = csv.reader(test_file, delimiter='\t')
            for n in test_reader:
                y_predictions.append(lr.predict_y(b,n))

            y_test = matrix.build_y_matrix(1, (data.get_lines('my_test.csv')), 'my_test.csv')

            print('\nEste es el error(RMSE):')
            print(error.RMSE(y_test, y_predictions))
            print('\nError en porcentaje:')
            print(error.RMSE_percentage(y_test, y_predictions))   

    else:
        print('Cant multiply at y')