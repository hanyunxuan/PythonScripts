"""

"""

import pymysql

db = pymysql.connect("localhost", "root", "123456", "trux")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS AGE")

sql = """CREATE TABLE TableName (
         age1 INT,
         age2 INT,
         age3 INT )"""
cursor.execute(sql)
a=20
b=33
c=40
cursor.execute("INSERT INTO TableName(age1, age2, age3) VALUES(%s, %s, %s)", [a, b, c])
db.commit()