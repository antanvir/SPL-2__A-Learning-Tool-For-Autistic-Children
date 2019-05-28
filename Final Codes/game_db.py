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
sql="CREATE TABLE game(game_id int auto_increment PRIMARY KEY, main_image VARCHAR(300), image_name_1 VARCHAR(300), image_name_2 VARCHAR(300), image_name_3 VARCHAR(300),image_name_4 VARCHAR (300), elapsedTime VARCHAR(80))"
myCursor.execute(sql)
mydb.commit()
myCursor.close()
mydb.close()

