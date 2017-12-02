"""
input
point_x: a list of longitudes
point_y: a list of latitudes
polygon_x: a list of longitudes
polygon_y: a list of latitudes
output
judgement:if point inside polygon,1,else 0
"""

import matplotlib.path as mplPath
import numpy as np


def judge_point(point_x, point_y, polygon_x, polygon_y):
    # first data and last data must be same
    if polygon_x[0] == polygon_x[-1]:
        pass
    else:
        polygon_x.append(polygon_x[0])
        polygon_y.append(polygon_y[0])
    num_x = []
    num_y = []
    list_x = []
    list_y = []
    unlist_x = []
    unlist_y = []
    polygon = np.zeros((len(polygon_x), 2))
    for i in range(len(polygon_x)):
        polygon[i, 0] = polygon_x[i]
        polygon[i, 1] = polygon_y[i]
    for i in range(len(point_x)):
        # for j in range(len(point_y)):
        bbPath = mplPath.Path(polygon)
        if bbPath.contains_point((point_x[i], point_y[i])):
            num_x.append(i + 1)
            num_y.append(i + 1)
            list_x.append(point_x[i])
            list_y.append(point_y[i])
        else:
            unlist_x.append(point_x[i])
            unlist_y.append(point_y[i])
    return num_x, num_y, list_x, list_y, unlist_x, unlist_y


if __name__ == '__main__':
    import xlrd
    import os
    import glob
    import matplotlib.pyplot as plt

    os.chdir('E:\WorkPlace\Git\python36\PythonScripts')
    FileList = glob.glob('polygon1.xls')
    # file_suffix = ".xls"
    # directory = 'E:\WorkPlace\Git\python36\PythonScripts'
    # All_file = read_file_name(directory, file_suffix)
    workbook = xlrd.open_workbook(FileList[0])
    sheet1 = workbook.sheet_by_index(0)
    cols0 = sheet1.col_values(0)
    cols1 = sheet1.col_values(1)
    # num_row = 1770
    # num_col = 778
    # Coordinate_x = np.zeros((num_col, 1))
    # Coordinate_y = np.zeros((num_row, 1))
    # x_length = 111.8538666 - 111.7793655
    # y_length = 41.13521576 - 41.00509644
    # x0 = -1 * (111.7793655 + x_length / num_col / 2)
    # y0 = 41.00509644 + y_length / num_row / 2
    # for i in range(num_col):
    #     Coordinate_x[i, 0] = x0 - (x_length / num_col) * i
    # for i in range(num_row):
    #     Coordinate_y[i, 0] = y0 + (y_length / num_row) * i
    Coordinate_x = [-111.826, -111.818, -111.817, -111.821]
    Coordinate_y = [41.0214, 41.0224, 41.019, 41.0207]
    [num_x, num_y, list_x, list_y, unlist_x, unlist_y] = judge_point(Coordinate_x, Coordinate_y,
                                                                                           cols0, cols1)

    plt.plot(cols0, cols1)
    plt.plot(list_x, list_y, 'o')
    plt.plot(unlist_x, unlist_y, 'ro')
    plt.show()
