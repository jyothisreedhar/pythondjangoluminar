import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database="pythondecember",
auth_plugin='mysql_native_password',

)
cursor=db.cursor()
sql="select * from movies"
cursor.execute(sql)
movie=cursor.fetchall()
for movies in movie:
    print(movie)
