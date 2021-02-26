import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database="pythondecember"
    )

cursor=db.cursor()
sql="create table movies(id int,name varchar(60),year varchar(89),rating int)"
cursor.execute(sql)
print('table created')
db.close()
