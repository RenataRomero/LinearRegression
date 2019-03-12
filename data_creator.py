import csv
import random as rnd
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

def get_lines(filename):

    with open(filename, 'r') as new_file:
        row_count = sum(1 for row in new_file)
    
    return row_count
