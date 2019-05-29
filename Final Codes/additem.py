from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import tkinter as tk
class Ui_Form(object):
    def setupUi(self, Form):
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.left = 0
        self.top = 0
        print(self.width, self.height)
        #self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)
        Form.setObjectName("Form")
        Form.resize(self.width, self.height)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QtGui.QColor(188, 196, 195))
        Form.setPalette(p)

        #Form.setStyleSheet("background-color : rgb(47,76,122)");


        self.label= QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, 30, 700, 50))
        self.label.setText("Add images, audios and videos to add object")
        self.label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Black))

        
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(730, 120, 361, 70))
        self.label1.setText("Select imagename ")
        self.label1.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.addName = QtWidgets.QLineEdit(Form)
        self.addName.setGeometry(QtCore.QRect(530, 200, 550, 40))
        self.addName.setObjectName("addName")
        self.addNameButton=QtWidgets.QPushButton(Form)
        self.addNameButton.setGeometry(QtCore.QRect(750,260,93,28))
        self.addNameButton.setObjectName("addNameButton")


        self.line = QtWidgets.QLineEdit(Form)
        self.line.setGeometry(QtCore.QRect(20, 300, 1700, 1))
        self.line.setObjectName("addName")
        

        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(1100, 300, 361, 70))
        self.label2.setText("Select audio ")
        self.label2.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.audlineEdit = QtWidgets.QLineEdit(Form)
        self.audlineEdit.setGeometry(QtCore.QRect(880, 370, 550, 40))
        self.audlineEdit.setObjectName("audlineEdit")
        self.audpushButton = QtWidgets.QPushButton(Form)
        self.audpushButton.setGeometry(QtCore.QRect(1100, 420, 93, 28))
        self.audpushButton.setObjectName("audpushButton")
        


        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(350, 300, 361, 70))
        self.label3.setText("Select video ")
        self.label3.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.vidlineEdit = QtWidgets.QLineEdit(Form)
        self.vidlineEdit.setGeometry(QtCore.QRect(150, 370, 550, 40))
        self.vidlineEdit.setObjectName("vidlineEdit")
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(370, 420, 93, 28))
        self.vidpushButton.setObjectName("vidpushButton")
        

        self.line2 = QtWidgets.QLineEdit(Form)
        self.line2.setGeometry(QtCore.QRect(20, 470, 1700, 1))
        self.line2.setObjectName("addName")
        


        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(350, 480, 361, 70))
        self.label5.setText("Select image1 ")
        self.label5.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit2 = QtWidgets.QLineEdit(Form)
        self.imglineEdit2.setGeometry(QtCore.QRect(150, 550, 550,40))
        self.imglineEdit2.setObjectName("imglineEdit")
        self.imgpushButton2 = QtWidgets.QPushButton(Form)
        self.imgpushButton2.setGeometry(QtCore.QRect(350, 610, 93, 28))
        self.imgpushButton2.setObjectName("imgpushButton2")


        self.label6= QtWidgets.QLabel(Form)
        self.label6.setGeometry(QtCore.QRect(1100, 480, 361, 70))
        self.label6.setText("Select image2")
        self.label6.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit3 = QtWidgets.QLineEdit(Form)
        self.imglineEdit3.setGeometry(QtCore.QRect(880, 550, 550, 40))
        self.imglineEdit3.setObjectName("imglineEdit")
        self.imgpushButton3 = QtWidgets.QPushButton(Form)
        self.imgpushButton3.setGeometry(QtCore.QRect(1120, 610, 100, 30))
        self.imgpushButton3.setObjectName("imgpushButton3")

        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(730, 630, 361, 70))
        self.label4.setText("Select image3")
        self.label4.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit = QtWidgets.QLineEdit(Form)
        self.imglineEdit.setGeometry(QtCore.QRect(530, 700,550, 40))
        self.imglineEdit.setObjectName("imglineEdit")
        self.imgpushButton1 = QtWidgets.QPushButton(Form)
        self.imgpushButton1.setGeometry(QtCore.QRect(750, 770, 93, 28))
        self.imgpushButton1.setObjectName("imgpushButton1")

        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(650, 850, 311, 61))
        self.objpushButton.setObjectName("objpushButton")


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
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.addName.setText(ifileName)
    def setImage2(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit.setText(ifileName)
    def setImage3(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit2.setText(ifileName)
    def setImage4(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit3.setText(ifileName)



    def setVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "/home/anika/Downloads/videos", "*.mp4")
        print(fileName)
        self.vidlineEdit.setText(fileName)

    def setAudio(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Audio", "/home/anika/Downloads/audios", "*.wav")
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
                #passwd = "ant904",
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
