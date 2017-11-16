import pymysql

conn = pymysql.connect("localhost","root","123456","trux" )
cursor = conn.cursor()
query = ('select name, age from test')
cursor.execute(query)
for (name, age) in cursor:
    print(name, age)
cursor.close()
conn.close()