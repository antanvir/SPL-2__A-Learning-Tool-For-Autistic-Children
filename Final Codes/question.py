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
    
    def setupUi(self):
        
        
 
        '''
        #self.photo = tk.PhotoImage(file="right.png")
        self.Artwork = tk.Label(self.frame, image=self.photo)
        self.Artwork.photo = self.photo
        self.Artwork.pack()
        '''
        self.setDB()
        

        
    def setDB(self):
        nameList=list()
        imageList=list()
        qus_nam=""
        audio_nam=""
        #global object_id
        a=datetime.datetime.now().replace(microsecond=0)
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT qus_name,qus_audio,image_name1,image_name2,image_name3,image_name4,imagePath1,imagePath2,imagePath3,imagePath4\
 FROM questions where qid=1"
        #val=(object_id,)
        myCursor.execute(sql)
        row=myCursor.fetchone()
        print(row)
        nameList.append(row[2])
        nameList.append(row[3])
        nameList.append(row[4])
        nameList.append(row[5])

        imageList.append(row[6])
        imageList.append(row[7])
        imageList.append(row[8])
        imageList.append(row[9])

        qus_nam=row[0]
        audio_nam=row[1]
        
        for file in row:
            #print(file)
            ifileName=str(file)
            #print("lol"+ifileName)
            if ifileName:
                self.buttons(ifileName,a,nameList, imageList,qus_nam,audio_nam)
    

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


    def buttons(self,ifileName,a,nameList,imageList,qus_nam,audio_nam):
        
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
                    w = tk.Label(master, text="Correct Answer", font=("Helvetica", 25))   
                    #w.place(x=220, y=500, relwidth=.5, relheight=.5)     
                    w.pack(side="top")
                    img = tk.PhotoImage(file='right.png')
                    #label.image = tk.PhotoImage(file='right.png')
                    select=True
                    label=tk.Label(master,image=img)
                    label.image = img 
                    label.pack(side = "bottom")
                    b=datetime.datetime.now().replace(microsecond=0)
                    c=str(b-a)
                    print(b-a)
                    sql = "update questions set result=%s, elapsedTime=%s where qid=1"
                    val=('correct',c,)
                    #UPDATE products SET ($fields) VALUES ($values) WHERE sku = '$checksku
                    newcur=mydb.cursor()
                    newcur.execute(sql,val)
                    mydb.commit()
        
                else:
                    print("no")
                    w = tk.Label(master, text="Wrong Answer", font=("Helvetica", 25))        
                    w.pack(side="top")
                    img = tk.PhotoImage(file='wrong.png')
                    #label.image = tk.PhotoImage(file='right.png')
                    label=tk.Label(master,image=img)
                    label.image = img 
                    label.pack(side = "bottom")
                    select=True
                    b=datetime.datetime.now().replace(microsecond=0)
                    c=str(b-a)
                    print(b-a)
                    sql = "update questions set result=%s, elapsedTime=%s where qid=1"
                    val=('incorrect',c,)#sql = "UPDATE questions set result='incorrect',time=c.strftime('%Y-%m-%d %H:%M:%S') where qid=1"
                    newcur=mydb.cursor()
                    newcur.execute(sql,val)
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
        #print(x[5])
        test="এটা কি?"
        #test = test.decode('utf8')
        print(test)
        #w = tk.Label(master, text=test, font=("Lohit Bengali", 36))        
        #w.pack()
        #playsound("tee.wav")
        

        #root = Tk()
        img = tk.PhotoImage(file=qus_nam)
        img=img.zoom(1)
        img=img.subsample(1)
        panel = tk.Label(master, image = img, width=50, height=150)
        #panel.place(x=220, y=500, relwidth=.5, relheight=.5)
        panel.image=img
        panel.pack(fill = "both", expand = "no")


        option1 = tk.BooleanVar(value=False)
        #QtGui.QSound.play(audio_nam)
        playsound(audio_nam)
        print(audio_nam)
        photo1 = tk.PhotoImage(file=imageList[0])
        img = Image.open(imageList[0])
        width, height = img.size
        #photo1=photo1.zoom(2)
        photo1 = photo1.subsample(5)
        r1=tk.Radiobutton(master, image=photo1, variable = rb,value= nameList[0],command=change_image)
        
        r1.pack(side = "left")
        print(rb.get())

        photo2 = tk.PhotoImage(file=imageList[1])
        img = Image.open(imageList[1])
        width, height = img.size
        #photo2=photo2.zoom(2)
        photo2 = photo2.subsample(5)
        r2=tk.Radiobutton(master, image=photo2, value=nameList[1] ,variable = rb,command=change_image)
        r2.pack(side = "right")

        photo3 = tk.PhotoImage(file=imageList[2])
        img = Image.open(imageList[2])
        width, height = img.size
        #photo3=photo3.zoom(2)
        photo3 = photo3.subsample(5)
        r3=tk.Radiobutton(master, image=photo3, value=nameList[2],variable = rb,command=change_image)
        r3.pack(side = "left")
        photo4 = tk.PhotoImage(file=imageList[3])
        img = Image.open(imageList[3])
        width, height = img.size
        #photo4=photo4.zoom(2)
        photo4 = photo4.subsample(5)
        r4=tk.Radiobutton(master, image=photo4, value=nameList[3],variable = rb,command=change_image)
        r4.pack(side = "right")
        master.mainloop()
        master.destroy() 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    object_id=int(1)
    select=False
    Ui_MainWindow().setupUi()
    sys.exit(app.exec_())
    '''app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''
    #Ui_MainWindow().buttons()'''
    
