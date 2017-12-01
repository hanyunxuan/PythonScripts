"""

"""
import pymysql

db = pymysql.connect("localhost", "root", "123456", "mathematicalmodel")
cursor = db.cursor()
query = ('select Longitude, Latitude from polygon1')
cursor.execute(query)
for (Longitude, Latitude) in cursor:
    print(Latitude)
cursor.close()
db.close()