"""
author:hanyunxuan
date:2018.1.22

deg2deg_min_sec:input degree ,output degree minute second
deg_min_sec2deg:input degree minute second ,output degree
"""

from math import *


def deg2deg_min_sec(input_number=0.0):
    if type(input_number) != 'float':
        try:
            input_number = float(input_number)
        except:
            print('\nERROR: Could not convert %s to float.' % (type(input_number)))
            return 0
    minutes = input_number % 1.0 * 60
    seconds = minutes % 1.0 * 60

    # return '\n%s°%s\'%s"\n' % (int(floor(input_number)), int(floor(minutes)), seconds)
    output_number = int(floor(input_number)) * 10000 + int(floor(minutes)) * 100 + int(floor(seconds))
    return output_number


def deg_min_sec2deg(input_number=0):
    if type(input_number) != 'int':
        try:
            input_number = int(input_number)
        except:
            print('\nERROR: Could not convert %s to int.' % (type(input_number)))
            return 0
    tem = str(input_number)
    second = int(tem[-2] + tem[-1])
    minute = int(tem[-4] + tem[-3])
    degress = int(tem[:-4])
    output_number = degress + minute / 60 + second / 3600
    return output_number


if __name__ == '__main__':
    import glob
    import os
    import xlrd
    import pandas as pd

    os.chdir('E:\空域分类')
    # FileList = glob.glob('*.xlsx')
    FileList = glob.glob('成都管制区边界_simple.xlsx')
    # print(FileList)
    workbook = xlrd.open_workbook(FileList[0])
    sheet1 = workbook.sheet_by_index(0)
    cols0 = sheet1.col_values(0)
    cols1 = sheet1.col_values(1)
    cols2 = sheet1.col_values(2)
    # print(cols1)
    # print(cols2)

    list_all1 = [(cols1[i], cols2[i]) for i in range(len(cols1))]
    labels1 = ['cols1', 'cols2']
    df1 = pd.DataFrame.from_records(list_all1, columns=labels1)

    Longitude = [deg_min_sec2deg(i) for i in cols1]
    Latitude = [deg_min_sec2deg(i) for i in cols2]

    list_all2 = [(Longitude[i], Latitude[i]) for i in range(len(Longitude))]
    labels2 = ['Longitude', 'Latitude']
    df2 = pd.DataFrame.from_records(list_all2, columns=labels2)

    print('转换前========================', '\n', df1, '\n', '转换后===========================', '\n', df2, '\n', '边界范围',
          '\n', max(df2.Longitude), max(df2.Latitude), '\n', min(df2.Longitude), min(df2.Latitude))

