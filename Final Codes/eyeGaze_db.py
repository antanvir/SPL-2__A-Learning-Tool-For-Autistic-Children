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
sql="CREATE TABLE eyegazeContent(content_id int auto_increment PRIMARY KEY, video VARCHAR(300),nTimes INT, eyePositionOutput VARCHAR(300))"
myCursor.execute(sql)
mydb.commit()
myCursor.close()
mydb.close()

