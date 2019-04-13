import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "anika",
    passwd = "hridita123",
    database = "tools"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()

#myCursor.execute("CREATE DATABASE tools")
'''
myCursor.execute("CREATE TABLE object(object_id int primary key auto_increment, \
                  name VARCHAR(80),imageName VARCHAR(200), audioName VARCHAR(200),\
                  videoName VARCHAR(200))")
'''
mydb.commit()

myCursor.close()
mydb.close()