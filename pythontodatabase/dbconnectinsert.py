import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database="pythondecember",
auth_plugin='mysql_native_password',

)
cursor=db.cursor()
sql="insert into movies values(100,'pirates','2004',4)"
cursor.execute(sql)
db.commit()
db.close()