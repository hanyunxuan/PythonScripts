"""
author:hanyunxuan
date:2018.5.9
version:python2.7

Find a random path in unicom matrix
Input:st,e,len(matrix)
Output:path
"""
import random


def random_path(st, e, len_matrix):
    if (st > len_matrix) or (e > len_matrix):
        print("  st or e error", "st", st, "e", e)

    num = random.randint(1, len_matrix - 2)  # path length
    index = [i + 1 for i in range(len_matrix)]
    index.remove(st)
    index.remove(e)
    path = [st]
    for i in range(num):
        tem_ = random.choice(index)
        path.append(tem_)
        index.remove(tem_)
        # print random.choice(index)
    path.append(e)
    # print(path)
    return path


if __name__ == '__main__':
    st = 1
    e = 4
    len_matrix = 6
    path = random_path(st, e, len_matrix)
