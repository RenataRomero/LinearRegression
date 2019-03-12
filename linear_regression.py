import math
import copy

def predict_y(b, x):

    y = b[0][0] + (b[1][0]*float(x[0])) + (b[2][0]*float(x[1])) + (b[3][0]*float(x[2])) + (b[4][0]*float(x[3])) + (b[5][0]*float(x[4]))
    return round(y,4)

def predict_y_pivot(b, x):

    y = b[0] + (b[1]*float(x[0])) + (b[2]*float(x[1])) + (b[3]*float(x[2])) + (b[4]*float(x[3])) + (b[5]*float(x[4]))
    return round(y,4)

def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
 
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
        for j in range(p):
            b[i][j] *= t
    return  b