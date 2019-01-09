"""
author:hanyunxuan
date:2018.4.23
version:python27

Input:
path,
individual length
Output:
individual

worked 12.14.2018:individual2
"""
import numpy as np
from collections import Counter

# convert path to individual
def convert_path(path, ind_length):
    ind = np.zeros(ind_length)
    for i in range(len(path) - 1):
        st = path[i]
        e = path[i + 1]
        add_one = (st - 1) * np.sqrt(ind_length) + e
        ind[int(add_one) - 1] = 1

    ind.tolist()
    for i in range(len(ind)):
        # print(ind[i])
        ind[i] = int(ind[i])
    return ind


# convert individual to path:individual is matrix
def convert_individual1(ind, st, e):
    matrix_row = []
    matrix_column = []
    for i in range(len(ind)):
        # print(ind[i])
        if ind[i] == 1:
            add_one = i + 1
            # add_one=234
            # print(add_one)
            matrix_length = np.sqrt(len(ind))
            # find the row and column of add_one
            for j in range(int(matrix_length)):
                if add_one <= matrix_length * (j + 1):
                    row = j + 1
                    column = add_one - j * matrix_length
                    matrix_row.append(row)
                    matrix_column.append(int(column))
                    break
    path = []
    path.append(st)
    num_row = matrix_row.index(st)
    path.append(matrix_column[num_row])
    while True:
        for i in matrix_row:
            if i == path[-1]:
                num_row = matrix_row.index(i)
                path.append(matrix_column[num_row])
            if path[-1] == e:
                return path


# convert individual to path:individual is edge
def convert_individual2(ind, st, e, list_edge_num):
    edge1 = []
    edge2 = []
    for i in range(len(ind)):
        if ind[i] == 1:
            if list_edge_num[i][0] > list_edge_num[i][1]:
                edge1.append(list_edge_num[i][0])
                edge2.append(list_edge_num[i][1])
            else:
                edge1.append(list_edge_num[i][1])
                edge2.append(list_edge_num[i][0])
    path = []
    edge=edge1+edge2
    if edge.count(st)!=1 or edge.count(e)!=1:
        return path
    if max(list(Counter(edge).values()))>2:
        return path
    path.append(st)
    while True:
        if path[-1] in edge1:
            index_del = edge1.index(path[-1])
            path.append(edge2[edge1.index(path[-1])])
            del edge1[index_del] ,edge2[index_del]
        elif path[-1] in edge2:
            index_del = edge2.index(path[-1])
            path.append(edge1[edge2.index(path[-1])])
            del edge1[index_del], edge2[index_del]
        else:
            return []
        if path[-1] == e:
            return path


if __name__ == '__main__':
    # path = [1, 2, 6, 6]  # 1-2,2-4,4-6
    # ind_length = 36
    #
    # ind = convert_path(path, ind_length)
    # st = 17
    # e = 18
    # ind = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    #        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    # path = convert_individual(ind,st,e)
    # ind = [0, 1, 0, 1,1, 0]
    import random
    ind = [random.randint(a, b) for a, b in zip([0] * int(6), [1] * int(6))]
    st = 1
    e = 4
    list_edge_num = []
    Node_list = ["e", "b", "a", "d"]
    for i in range(len(Node_list) - 1):
        for j in range(i + 1, len(Node_list)):
            if Node_list[i] > Node_list[j]:
                list_edge_num.append((i + 1, j + 1))
            else:
                list_edge_num.append((j + 1, i + 1))
    path = convert_individual2(ind, st, e, list_edge_num)
