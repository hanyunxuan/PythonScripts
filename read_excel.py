import glob
import os
import xlrd

os.chdir('E:\\2016年9月')
# FileList = glob.glob('*.xlsx')
FileList = glob.glob('9月9号.xlsx')
# print(FileList)
workbook = xlrd.open_workbook(FileList[0])
sheet1 = workbook.sheet_by_index(0)
cols0 = sheet1.col_values(0)
cols1 = sheet1.col_values(1)
print(cols0)