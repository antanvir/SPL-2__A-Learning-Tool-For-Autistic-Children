from PyQt5 import QtCore, QtGui, QtWidgets

#-*- coding: utf8 -*-
import datetime
import mysql.connector
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import math
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from playsound import playsound
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QImageReader
from PyQt5.QtWidgets import QVBoxLayout
import mysql.connector
from PyQt5.QtMultimedia import QSound
import re

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 604)
        MainWindow.setGeometry(200, 150, 800, 550)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = tk.PhotoImage(file="right.png")
        self.Artwork = tk.Label(self.frame, image=self.photo)
        self.Artwork.photo = self.photo
        self.Artwork.pack()
        

        
    def setDB(self):
        nameList=list()
        imageList=list()
        qus_nam
        audio_nam
        global object_id
        a=datetime.datetime.now().replace(microsecond=0)
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT imagePath1,imagePath2,imagePath3,imagePath4, image_name1,image_name2,image_name3,image_name4,qus_name,\
qus_audio FROM questions where qid=1"
        #val=(object_id,)
        row=myCursor.fetchone()
        myCursor.execute(sql)
        nameList.append(row[4])
        nameList.append(row[5])
        nameList.append(row[6])
        nameList.append(row[7])

        imageList.append(row[0])
        imageList.append(row[1])
        imageList.append(row[2])
        imageList.append(row[3])

        qus_nam=row[8]
        audio_nam=row[9]
        QSound.play(audio_nam)
        for file in row:
            #print(file)
            ifileName=str(file)
            #print("lol"+ifileName)
            if ifileName:
                self.buttons(ifileName,a,nameList, imageList)
    

    def displayAnswer(self, fileName):
        image = Image.open('right.png')
        image.show()
        '''root = tk.Tk()
        label = tk.Label(root)
        label.image = tk.PhotoImage(file='right.png')
        #label['image'] = label.image
        #label.image = immage
        label.pack()
        root.mainloop()'''
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom    


    def buttons(self,ifileName,a,nameList,imageList,qus_nam):
        
        def change_image():
            global select
            response=rb.get()
            mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
            myCursor = mydb.cursor(buffered=True)
            sql = "SELECT answer FROM questions"
            myCursor.execute(sql)
            row=myCursor.fetchone()
            answer=""
            for file in row:
                #print(file)
                answer=str(file)
            print(select)

            if select==False:
                if response==answer:
                    print("yes")
                    w = tk.Label(master, text="Correct Answer", font=("Helvetica", 30))        
                    w.pack(side="top")
                    img = tk.PhotoImage(file='right.png')
                    #label.image = tk.PhotoImage(file='right.png')
                    select=True
                    label=tk.Label(master,image=img)
                    label.image = img 
                    label.pack(side = "bottom")
                    b=datetime.datetime.now().replace(microsecond=0)
                    print(b-a)
                    sql = "UPDATE questions set result='correct' where qid=1"
                    newcur=mydb.cursor()
                    newcur.execute(sql)
                    mydb.commit()
        
                else:
                    print("no")
                    w = tk.Label(master, text="Wrong Answer", font=("Helvetica", 30))        
                    w.pack(side="top")
                    img = tk.PhotoImage(file='wrong.png')
                    #label.image = tk.PhotoImage(file='right.png')
                    label=tk.Label(master,image=img)
                    label.image = img 
                    label.pack(side = "bottom")
                    select=True
                    b=datetime.datetime.now().replace(microsecond=0)
                    c=(b-a)
                    sql = "UPDATE questions set result='incorrect' where qid==1"
                    #sql = "UPDATE questions set result='incorrect',time=c.strftime('%Y-%m-%d %H:%M:%S') where qid=1"
                    newcur=mydb.cursor()
                    newcur.execute(sql)
                    mydb.commit()
                myCursor.close()
                mydb.close()
            
        master = tk.Tk()
        master.overrideredirect(False)
        #master.configure(background="#19476a")
        #master.attributes("-fullscreen", True)
        width_value=master.winfo_screenwidth()
        height_value=master.winfo_screenheight()
        #master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        #master.bind('<Escape>',self.toggle_geom)            
   
        master.geometry(("%dx%d+0+0")%(width_value, height_value))
        
        rb= tk.StringVar()
        x = re.split(",|'| ", ifileName)
        print(x[5])
        test="এটা কি?"
        #test = test.decode('utf8')
        print(test)
        #w = tk.Label(master, text=test, font=("Lohit Bengali", 36))        
        #w.pack()
        #playsound("tee.wav")
        

        #root = Tk()
        img = tk.PhotoImage(file=qus_nam)
        panel = tk.Label(master, image = img, width=50, height=180)
        panel.image=img
        panel.pack(side = "top", fill = "both", expand = "no")


        option1 = tk.BooleanVar(value=False)
        
        
        photo1 = tk.PhotoImage(file=x[1])
        img = Image.open(imageList[0])
        width, height = img.size
        photo1=photo1.zoom(3)
        photo1 = photo1.subsample(8)
        r1=tk.Radiobutton(master, image=photo1, variable = rb,value= nameList[0],command=change_image)
        
        r1.pack(side = "left")
        print(rb.get())

        photo2 = tk.PhotoImage(file=x[5])
        img = Image.open(imageList[1])
        width, height = img.size
        photo2=photo2.zoom(1)
        photo2 = photo2.subsample(12)
        r2=tk.Radiobutton(master, image=photo2, value=nameList[1] ,variable = rb,command=change_image)
        r2.pack(side = "right")

        photo3 = tk.PhotoImage(file=x[9])
        img = Image.open(imageList[2])
        width, height = img.size

        photo3=photo3.zoom(4)
        photo3 = photo3.subsample(8)
        r3=tk.Radiobutton(master, image=photo3, value=nameList[2],variable = rb,command=change_image)
        r3.pack(side = "left")
        photo4 = tk.PhotoImage(file=x[13])
        img = Image.open(imageList[3])
        width, height = img.size

        photo4=photo4.zoom(1)
        photo4 = photo4.subsample(20)
        r4=tk.Radiobutton(master, image=photo4, value=nameList[3],variable = rb,command=change_image)
      
        r4.pack(side = "right")
        master.mainloop()



if __name__ == "__main__":
    import sys
    object_id=int(1)
    select=False
    Ui_MainWindow().setDB()
    '''app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''
    #Ui_MainWindow().buttons()'''
    
