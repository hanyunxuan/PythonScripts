# import pymysql
#
# db = pymysql.connect("localhost", "root", "123456", "mathematicalmodel")
# cursor = db.cursor()
# query = ('select Longitude, Latitude from polygon1')
# cursor.execute(query)
# for (Longitude, Latitude) in cursor:
#     print(Latitude)
# cursor.close()
# db.close()
import peewee
from peewee import *

db = MySQLDatabase('trux', user='root', passwd='123456')


class Book1(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()
    age = peewee.IntegerField()

    class Meta:
        database = db


Book1.create_table()
a = "me,me1"
b = 'Peewee is cool,socool'
c = 2,3
for i in range(2):
    book = Book1(author=a[i],title=b[i],age=c[i])
book.save()
# for book in Book.filter(author="me"):
#     print(book.title)
# book = ['book1', 'book2', 'book3']
