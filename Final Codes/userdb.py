import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    #passwd = "ant904",
    database = "spl"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()
#myCursor.execute("CREATE database test222")
sql="CREATE TABLE User(UID int auto_increment PRIMARY KEY, username VARCHAR(300), password VARCHAR(300))"
myCursor.execute(sql)
mydb.commit()
myCursor.close()
mydb.close()

