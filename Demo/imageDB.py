import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "anika",
    passwd = "hridita123",
    database = "imageDB"
    #auth_plugin='mysql_native_password'
    )
myCursor = mydb.cursor()

#myCursor.execute("CREATE DATABASE imageDB")
'''
myCursor.execute("CREATE TABLE ImagePath(Image_ID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(35),\
                Path VARCHAR(80))")
sql = "INSERT INTO ImagePath(Name, Path) VALUES(%s, %s)"
val = [
  ('mango tree',  r"C:/Users/dell/Downloads/Python-master/Python-master/ImageShow/mango-tree.jpg"),
  ('mango in tree',  "C:/Users/dell/Downloads/Python-master/Python-master/ImageShow/slice_mango.jpg"),
  ('green mango',  "C:/Users/dell/Downloads/Python-master/Python-master/ImageShow/green_mango.jpg"),
  ('single mango',  "C:/Users/dell/Downloads/Python-master/Python-master/ImageShow/mango_in_tree.jpg")  
]
'''
myCursor.executemany(sql, val)

mydb.commit()
print(myCursor.rowcount, "row was inserted.") 

#myCursor.execute("SELECT * FROM ImagePath")

#myresult = myCursor.fetchall()

#for records in myresult:
 # print(records)

myCursor.close()
mydb.close()
