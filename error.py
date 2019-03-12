import math

def RMSE(y_test, y_prediction):

    y_yp_sum = 0

    i = 0
    for n in y_test:
        dif = n[0] - y_prediction[i]
        y_yp_sum += (dif)
        i += 1
    
    root = pow(y_yp_sum,2) / (len(y_test))
    error = math.sqrt(root)

    return error

def RMSE_percentage(y_test, y_prediction):

    y_yp_sum = 0

    i = 0
    for n in y_test:
        dif = n[0] - y_prediction[i]
        y_yp_sum += (dif/n[0])
        i += 1
    
    root = pow(y_yp_sum,2) / (len(y_test))
    error = math.sqrt(root)

    return error
