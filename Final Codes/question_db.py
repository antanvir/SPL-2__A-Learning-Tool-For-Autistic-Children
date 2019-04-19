import mysql.connector
import datetime
mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    #passwd = "hridita123",
    database = "spl"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()


myCursor.execute("CREATE TABLE questions(qid int primary key auto_increment, \
                  qus_name VARCHAR(200),qus_audio VARCHAR(200),image_name1 VARCHAR(80),\
                  image_name2 VARCHAR(80), image_name3 VARCHAR(80),image_name4 VARCHAR(80),\
                  answer VARCHAR(80),imagePath1 VARCHAR(200), imagePath2 VARCHAR(200),\
                  imagePath3 VARCHAR(200),imagePath4 VARCHAR(200),elapsedTime datetime,result VARCHAR(15))")

#myCursor.execute("ALTER TABLE Users ADD COLUMN Id INT AUTO_INCREMENT PRIMARY KEY")
#myCursor.execute("SHOW TABLES")

#for tables in myCursor:
    #print(tables)

mydb.commit()

myCursor.close()
mydb.close()
