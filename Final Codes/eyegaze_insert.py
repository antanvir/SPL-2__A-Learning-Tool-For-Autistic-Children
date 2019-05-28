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
sql="insert into  eyegazeContent( video ) values( %s)"
val=("/home/anika/Downloads/cartoon_2.mp4",)
myCursor.execute(sql,val)
mydb.commit()
myCursor.close()
mydb.close()

