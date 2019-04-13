import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    #passwd = "",
    database = "spl"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()
#myCursor.execute("CREATE database test222")
sql="CREATE TABLE object (object_id int auto_increment PRIMARY KEY, image_name_1 VARCHAR(300), image_name_2 VARCHAR(300),image_name_3 VARCHAR(300),\
video_name VARCHAR(300), object_image VARCHAR(300), audio_name VARCHAR(300))"
myCursor.execute(sql)
mydb.commit()
myCursor.close()
mydb.close()

