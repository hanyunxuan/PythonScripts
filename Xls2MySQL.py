import xlrd
from PythonScripts.ReadFile import read_file_name
import os
import pymysql

file_suffix = ".xlsx"
# directory = 'E:\WorkPlace\Git\Python35\HiMCMContest'
directory = 'E:\AllData\数据航路数据2016\导出数据'
file_name = read_file_name(directory, file_suffix)

db = pymysql.connect("localhost", "root", "123456", "trux")
cursor = db.cursor()
for num_flie in range(file_name):
    cursor.execute("DROP TABLE IF EXISTS file_name[num_flie]")
    sql = """CREATE TABLE file_name[num_flie] (
           age1 INT,
           age2 INT,
           age3 INT )"""
    cursor.execute(sql)

    workbook = xlrd.open_workbook(os.path.join(directory, file_name[0]))
    sheet1 = workbook.sheet_by_index(0)
    cols0 = sheet1.col_values(0)
    cols1 = sheet1.col_values(2)
    cols2 = sheet1.col_values(3)
    num_row = max(len(cols0), len(cols1), len(cols2))

    for i in range(num_row):
      cursor.execute("INSERT INTO TableName(age1, age2, age3) VALUES(%s, %s, %s)", [cols0[i], cols1[i], cols2[i]])
      db.commit()
