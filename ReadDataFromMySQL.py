import pymysql

db = pymysql.connect("localhost", "root", "123456", "trux")
cursor = db.cursor()
query = ('select Longitude, Latitude from tablename')
cursor.execute(query)
for (Longitude, Latitude) in cursor:
    print(Latitude+1000000)
cursor.close()
db.close()