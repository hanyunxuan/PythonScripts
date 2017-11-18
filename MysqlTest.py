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

db = MySQLDatabase('alldata', user='root', passwd='123456')


class Book(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db


Book.create_table()
book = Book(author="me", title='Peewee is cool')
book.save()
for book in Book.filter(author="me"):
    print(book.title)
book = ['book1', 'book2', 'book3']
