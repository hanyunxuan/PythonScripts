import xlrd
from PythonScripts.ReadFile import read_file_name
import peewee
from peewee import *
import os

file_suffix = ".xls"
directory = 'E:\WorkPlace\Git\Python35\HiMCMContest'
file_name=read_file_name(directory, file_suffix)

db = MySQLDatabase('alldata', user='root', passwd='123456')
class Coordinate(peewee.Model):
    Longitude = peewee.DoubleField()
    Latitude = peewee.DoubleField()

    class Meta:
        database = db


for i in range(len(file_name)):
    file_name[i](peewee.Model)
    file_name[i].create_table()
    workbook = xlrd.open_workbook(os.path.join(directory, file_name[i]))
    sheet1 = workbook.sheet_by_index(0)
    cols0 = sheet1.col_values(0)
    cols1 = sheet1.col_values(1)
    for j in range(len(cols0)):
        book = file_name[i](Longitude=cols0[j], Latitude=cols1[j])
        book.save()
