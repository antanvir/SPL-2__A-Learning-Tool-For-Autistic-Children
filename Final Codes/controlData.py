import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    #passwd = "ant904",
    database = "spl"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()
qusTimeList=list()
qusTimeList.append("0:00:03")
qusTimeList.append("0:00:02")
qusTimeList.append("0:00:05")
qusTimeList.append("0:00:06")
qusTimeList.append("0:00:08")
qusTimeList.append("0:00:02")
qusTimeList.append("0:00:03")
qusTimeList.append("0:00:03")
qusTimeList.append("0:00:04")
qusTimeList.append("0:00:05")
qusTimeList.append("0:00:08")

gameTimeList=list()
gameTimeList.append("0:00:13")
gameTimeList.append("0:00:19")
gameTimeList.append("0:00:24")
gameTimeList.append("0:00:08")
gameTimeList.append("0:00:09")
gameTimeList.append("0:00:13")
gameTimeList.append("0:00:08")
gameTimeList.append("0:00:09")
gameTimeList.append("0:00:13")
gameTimeList.append("0:00:14")
gameTimeList.append("0:00:12")
         
#myCursor.execute("CREATE database test222")
sql="INSERT into  controlGroup(questionTime , gameTime) VALUES (%s, %s)"
val=(qusTimeList[9],gameTimeList[9])

myCursor.execute(sql,val)
mydb.commit()
myCursor.close()
mydb.close()

