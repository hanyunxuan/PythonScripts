"""
author:hanyunxuan
date:2018.4.23
version:python27
"""
# -*- coding: utf-8 -*-
from numpy import array
from mlab.releases import latest_release as matlab

def call_matlab(matrix_dis, st, e):
    matlab.path(matlab.path(), r'E:\Paper\Traffic Assignment ING\Program\Network_33')  # set path
    result = matlab.RandomSearshPath(matrix_dis, st, e)  # call matlab
    result_end = []

    for i in range(len(result)):
        if result[i] != e:
            result_end.append(result[i])
        else:
            break
    result_end.append(e[0])
    return result_end


# st=[17]
# e=[18]
# result = matlab.RandomSearshPath(matrix_dis,st,e)
# result_end=[]
#
# for i in range(len(result)):
#     if result[i]!=e:
#         result_end.append(result[i])
#     else:
#         break
# result_end.append(e[0])
if __name__ == '__main__':
    st=[17]
    e=[18]
    matrix_dis = array([[0, 1, float('inf'), 1, float('inf'), float('inf'), float('inf'), float('inf'), 4, float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 3,
                         float('inf')],
                        [1, 0, 1, 2, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1,
                         float('inf')],
                        [float('inf'), 1, 0, float('inf'), 2, 2, 1, float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1,
                         float('inf')],
                        [1, 2, float('inf'), 0, 1, float('inf'), float('inf'), float('inf'), 1, float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf')],
                        [float('inf'), 1, 2, 1, 0, 1, float('inf'), float('inf'), 3, 1, float('inf'), 3, float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
                        [float('inf'), float('inf'), 2, float('inf'), 1, 0, 1, 2, float('inf'), float('inf'),
                         float('inf'), 2, 4, 3, float('inf'), float('inf'), float('inf'), float('inf')],
                        [float('inf'), float('inf'), 1, float('inf'), float('inf'), 1, 0, 1, float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), 3, 2, 1, 0, float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), 1, 3, float('inf'), float('inf'), float('inf')],
                        [4, float('inf'), float('inf'), 1, 1, float('inf'), float('inf'), float('inf'), 0, 1, 1,
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf'), 1, 0, 1, 2, float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'),
                         float('inf'), 1, 1, 0, 1, float('inf'), float('inf'), float('inf'), 1, float('inf'),
                         float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'),
                         float('inf'), float('inf'), 2, 1, 0, 2, float('inf'), float('inf'), 1, float('inf'),
                         float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 4, float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), 2, 0, 1, 2, 2, float('inf'), 1],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 3, float('inf'), 1,
                         float('inf'), float('inf'), float('inf'), float('inf'), 1, 0, 1, float('inf'), float('inf'),
                         float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), 3, float('inf'), float('inf'), float('inf'), float('inf'), 2, 1, 0, float('inf'),
                         float('inf'), 4],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), 1, 1, 2, float('inf'), float('inf'), 0,
                         float('inf'), 1],
                        [3, 1, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), 0, float('inf')],
                        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'),
                         float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1,
                         float('inf'), 4, 1, float('inf'), 0]])

    result_end=call_matlab(matrix_dis, st, e)
    result_end=[int(i) for i in result_end]
    print result_end

