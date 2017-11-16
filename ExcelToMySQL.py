import xlrd
from PythonScripts.ReadFile import read_file_name
import peewee
from peewee import *
import os

file_suffix = ".xls"
directory = 'E:\WorkPlace\Git\Python35\HiMCMContest'
file_name=read_file_name(directory, file_suffix)
workbook = xlrd.open_workbook(os.path.join(directory,file_name[1]))
sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
cols0 = sheet1.col_values(0)
print(cols0)




# db = MySQLDatabase('alldata', user='root', passwd='123456')
#
#
# class Book(peewee.Model):
#     author = peewee.CharField()
#     title = peewee.TextField()
#
#     class Meta:
#         database = db
#
#
# Book.create_table()
# book = Book(author="me", title='Peewee is cool')
# book.save()
# for book in Book.filter(author="me"):
#     print(book.title)