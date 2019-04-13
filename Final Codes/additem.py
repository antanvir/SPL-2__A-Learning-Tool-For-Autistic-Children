# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dell\Desktop\backend\additem2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        self.addNameButton=QtWidgets.QPushButton(Form)
        self.addNameButton.setGeometry(QtCore.QRect(200,120,93,28))
        self.addNameButton.setObjectName("addNameButton")
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(90, 320, 93, 28))
        self.vidpushButton.setObjectName("vidpushButton")
        self.imgpushButton1 = QtWidgets.QPushButton(Form)
        self.imgpushButton1.setGeometry(QtCore.QRect(320, 320, 93, 28))
        self.imgpushButton1.setObjectName("imgpushButton1")
        self.imgpushButton2 = QtWidgets.QPushButton(Form)
        self.imgpushButton2.setGeometry(QtCore.QRect(550, 320, 93, 28))
        self.imgpushButton2.setObjectName("imgpushButton2")
        self.imgpushButton3 = QtWidgets.QPushButton(Form)
        self.imgpushButton3.setGeometry(QtCore.QRect(800, 320, 93, 28))
        self.imgpushButton3.setObjectName("imgpushButton3")
        self.audpushButton = QtWidgets.QPushButton(Form)
        self.audpushButton.setGeometry(QtCore.QRect(700, 120, 93, 28))
        self.audpushButton.setObjectName("audpushButton")
        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(300, 480, 311, 61))
        self.objpushButton.setObjectName("objpushButton")
        self.addName = QtWidgets.QLineEdit(Form)
        self.addName.setGeometry(QtCore.QRect(50, 20, 361, 60))
        self.addName.setObjectName("addName")
        self.imglineEdit = QtWidgets.QLineEdit(Form)
        self.imglineEdit.setGeometry(QtCore.QRect(290, 190,181, 81))
        self.imglineEdit.setObjectName("imglineEdit")
        self.imglineEdit2 = QtWidgets.QLineEdit(Form)
        self.imglineEdit2.setGeometry(QtCore.QRect(520, 190, 181,81))
        self.imglineEdit2.setObjectName("imglineEdit")
        self.imglineEdit3 = QtWidgets.QLineEdit(Form)
        self.imglineEdit3.setGeometry(QtCore.QRect(750, 190, 181, 81))
        self.imglineEdit3.setObjectName("imglineEdit")
        self.audlineEdit = QtWidgets.QLineEdit(Form)
        self.audlineEdit.setGeometry(QtCore.QRect(550, 20, 361, 60))
        self.audlineEdit.setObjectName("audlineEdit")
        self.vidlineEdit = QtWidgets.QLineEdit(Form)
        self.vidlineEdit.setGeometry(QtCore.QRect(50, 190, 181, 81))
        self.vidlineEdit.setObjectName("vidlineEdit")
        self.addNameButton.clicked.connect(self.setImage1)
        self.imgpushButton1.clicked.connect(self.setImage2)
        self.imgpushButton2.clicked.connect(self.setImage3)
        self.imgpushButton3.clicked.connect(self.setImage4)
        self.vidpushButton.clicked.connect(self.setVideo)
        self.audpushButton.clicked.connect(self.setAudio)
        self.objpushButton.clicked.connect(self.additem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addNameButton.setText(_translate("Form","Add Object"))
        self.vidpushButton.setText(_translate("Form", "Add Video"))
        self.imgpushButton1.setText(_translate("Form", "Add Image"))
        self.imgpushButton2.setText(_translate("Form", "Add Image"))
        self.imgpushButton3.setText(_translate("Form", "Add Image"))
        self.audpushButton.setText(_translate("Form", "Add audio"))
        self.objpushButton.setText(_translate("Form", "Add Object"))

    def setImage1(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/SPL-2-master/Demo/spl/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.addName.setText(ifileName)
    def setImage2(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/SPL-2-master/Demo/spl/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit.setText(ifileName)
    def setImage3(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/SPL-2-master/Demo/spl/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit2.setText(ifileName)
    def setImage4(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/SPL-2-master/Demo/spl/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit3.setText(ifileName)



    def setVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "/home/anika/Downloads/SPL-2-master/Demo/spl/videos", "*.mp4")
        print(fileName)
        self.vidlineEdit.setText(fileName)

    def setAudio(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Audio", "/home/anika/Downloads/SPL-2-master/Demo/spl/audios", "*.mp3 *.wav")
        print(fileName)
        self.audlineEdit.setText(fileName)

    def deleting(self):
        #self.imgLabel.clear()
        self.imglineEdit.setText("")
        self.imglineEdit2.setText("")
        self.imglineEdit3.setText("")
        #self.VideoLabel.clear()
        self.vidlineEdit.setText("")
        #self.audioLabel.clear()
        self.audlineEdit.setText("")
        self.addName.setText("")

    def additem(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                #passwd = "hridita123",
                database = "spl"
                #auth_plugin='mysql_native_password'
                )
        ifileName1=self.imglineEdit.text();
        ifileName2=self.imglineEdit2.text();
        ifileName3=self.imglineEdit3.text();
        print(ifileName2)
        vfileName=self.vidlineEdit.text();
        audfileName=self.audlineEdit.text();
        name=self.addName.text()
        myCursor = mydb.cursor()
        sql = "INSERT INTO object(object_image, image_name_1, image_name_2,\
        image_name_3, audio_name, video_name) \
        VALUES(%s, %s, %s, %s,%s,%s)"
        val = (name, ifileName1,ifileName2,ifileName3, audfileName, vfileName) 
        print(name)
        print(audfileName)
        myCursor.execute(sql, val)
        mydb.commit()
        myCursor.close()
        mydb.close()

        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Item")
        messageBox.setText("Item added!")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        messageBox.exec_()
        self.deleting()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
sys.exit(app.exec_())