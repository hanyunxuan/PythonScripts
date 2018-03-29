'''
author: Hanyunxuan
date: 2018.3.21

input: a list of data,forecast quantity
output: forecast number

PS:This code is converted from Matlab program
   pay attention that python index starts from 0 if you convert Matlab code

'''
import numpy as np


def GM11(X, forecast_quantity):
    history_quantity = len(X)
    X0 = []
    X0 = [0] * history_quantity
    for i in range(history_quantity):
        for j in range(i, history_quantity):
            X0[i] = X[j] + X0[i]
        X0[i] = X0[i] / (history_quantity - i)
    s1 = 0
    X1 = [0] * history_quantity
    for jj in range(history_quantity):
        X1[jj] = X0[jj] + s1
        s1 = X1[jj]
    B = [0] * (history_quantity - 1)
    for ii in range(history_quantity - 1):
        B[ii] = -(X1[ii] + X1[ii + 1]) / 2
    B = [[B[i], 1] for i in range(len(B))]
    B = np.matrix(B)
    y = np.matrix(X0[1:history_quantity])
    AU = (np.linalg.inv(B.T * B)) * B.T * y.T
    a = AU[0]
    u = AU[1]
    xx1 = [0] * (history_quantity)
    for k in range(history_quantity - 1):
        xx1[k + 1] = (X0[0] - u / a) * np.e ** float(-a * (np.matrix(k + 1))) + u / a
    s = 0
    xx0 = [0] * (history_quantity)
    xx0[0] = np.matrix(X0[0])
    for jj in range(1, history_quantity):
        xx0[jj] = xx1[jj] - xx1[jj - 1]
    # 存储预测值
    Z = [0] * (forecast_quantity)
    for kkk in range(history_quantity + 1, history_quantity + forecast_quantity + 1):
        # for kkk in range(history_quantity+1,history_quantity+1):
        Z[kkk - history_quantity - 1] = (1 - np.e ** float(a)) * (X[0] - u / a) * np.e ** float(
            -a * (np.matrix(kkk - 1)))
    for i in range(len(Z)):
        Z[i] = Z[i].tolist()[0][0]
    return Z


if __name__ == '__main__':
    import pymysql
    db = pymysql.connect("localhost", "root", "123456", "mabfs", charset='utf8')
    cursor = db.cursor()
    # Step1: import data
    cursor.execute("SELECT (Province) FROM historydatabili")
    list_Province = [res[0] for res in cursor]

    X = [7261, 9943, 12625, 13071, 17583, 22579, 22886, 22347, 28004, 30255, 32488, 34190, 34421, 35395, 36169, 35376,
         35390, 34348, 35362, 38181]
    forecast_quantity = 15
    Z = GM11(X, forecast_quantity)
    print(Z)
# X0 = [7261,9943,12625,13071,17583,22579,22886,22347,28004,30255,32488,34190,34421,35395,36169,35376,35390,34348,35362,38181]
# gm11 = GM11(X0)
# gm11.gm11_predict_test(method='Posterior_difference_test')
# print(gm11.gm11Predict(30))
