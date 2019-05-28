from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_FormQ(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1960, 1420)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        
        p = Form.palette()
        p.setColor(Form.backgroundRole(), QtGui.QColor(235, 255, 211))
        Form.setPalette(p)


        self.label= QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, 30, 700, 50))
        self.label.setText("Add images and answers for questions")
        self.label.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Black))

        self.label1= QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(350, 100, 400, 70))
        self.label1.setText("Select question name")
        self.label1.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        self.addName = QtWidgets.QLineEdit(Form)
        self.addName.setGeometry(QtCore.QRect(150, 150,550, 40))
        self.addName.setObjectName("addName")
       	self.addNameButton=QtWidgets.QPushButton(Form)
        self.addNameButton.setGeometry(QtCore.QRect(370,210,93,28))
        self.addNameButton.setObjectName("addNameButton")


        self.label2= QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(1100, 100, 400, 70))
        self.label2.setText("Select audio")
        self.label2.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        self.audlineEdit = QtWidgets.QLineEdit(Form)
        self.audlineEdit.setGeometry(QtCore.QRect(880, 150, 600, 40))
        self.audlineEdit.setObjectName("audlineEdit")
        self.audpushButton = QtWidgets.QPushButton(Form)
        self.audpushButton.setGeometry(QtCore.QRect(1100, 210, 93, 28))
        self.audpushButton.setObjectName("audpushButton")

        self.line = QtWidgets.QLineEdit(Form)
        self.line.setGeometry(QtCore.QRect(20, 250, 1700, 1))
        self.line.setObjectName("addName")
        
        
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(350, 250, 361, 70))
        self.label3.setText("Select option 1 ")
        self.label3.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.vidlineEdit = QtWidgets.QLineEdit(Form)
        self.vidlineEdit.setGeometry(QtCore.QRect(150, 300, 550, 40))
        self.vidlineEdit.setObjectName("vidlineEdit")
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(370, 360, 93, 28))
        self.vidpushButton.setObjectName("vidpushButton")


        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(1050, 250, 361, 70))
        self.label4.setText("Write name of option 1 ")
        self.label4.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))    
        self.imgName = QtWidgets.QLineEdit(Form)
        self.imgName.setGeometry(QtCore.QRect(880, 300,600, 40))
        self.imgName.setObjectName("imgName")

        self.line2 = QtWidgets.QLineEdit(Form)
        self.line2.setGeometry(QtCore.QRect(20, 400, 1700, 1))
        self.line2.setObjectName("addName")
        

        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(350, 400, 361, 70))
        self.label5.setText("Select option 2 ")
        self.label5.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit = QtWidgets.QLineEdit(Form)
        self.imglineEdit.setGeometry(QtCore.QRect(150,450 ,550, 40))
        self.imglineEdit.setObjectName("imglineEdit")
        self.imgpushButton1 = QtWidgets.QPushButton(Form)
        self.imgpushButton1.setGeometry(QtCore.QRect(370, 510, 93, 28))
        self.imgpushButton1.setObjectName("imgpushButton1")


        self.label6= QtWidgets.QLabel(Form)
        self.label6.setGeometry(QtCore.QRect(1050, 400, 361, 70))
        self.label6.setText("Write name of option 2 ")
        self.label6.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imgName1 = QtWidgets.QLineEdit(Form)
        self.imgName1.setGeometry(QtCore.QRect(880, 450, 600, 40))
        self.imgName1.setObjectName("imgName2")

        self.line3 = QtWidgets.QLineEdit(Form)
        self.line3.setGeometry(QtCore.QRect(20, 550, 1700, 1))
        self.line3.setObjectName("addName")
        

        self.label7= QtWidgets.QLabel(Form)
        self.label7.setGeometry(QtCore.QRect(350, 550, 361, 70))
        self.label7.setText("Select option 3")
        self.label7.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit2 = QtWidgets.QLineEdit(Form)
        self.imglineEdit2.setGeometry(QtCore.QRect(150, 600, 550,40))
        self.imglineEdit2.setObjectName("imglineEdit")
        self.imgpushButton2 = QtWidgets.QPushButton(Form)
        self.imgpushButton2.setGeometry(QtCore.QRect(370, 660, 100, 30))
        self.imgpushButton2.setObjectName("imgpushButton2")


        self.label8= QtWidgets.QLabel(Form)
        self.label8.setGeometry(QtCore.QRect(1050, 550, 361, 70))
        self.label8.setText("Write name of option 3")
        self.label8.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imgName2 = QtWidgets.QLineEdit(Form)
        self.imgName2.setGeometry(QtCore.QRect(880, 600, 600, 40))
        self.imgName2.setObjectName("imgName2")

        self.line4 = QtWidgets.QLineEdit(Form)
        self.line4.setGeometry(QtCore.QRect(20, 700, 1700, 1))
        self.line4.setObjectName("addName")
        


        self.label9= QtWidgets.QLabel(Form)
        self.label9.setGeometry(QtCore.QRect(350, 700, 361, 70))
        self.label9.setText("Select option 4")
        self.label9.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imglineEdit3 = QtWidgets.QLineEdit(Form)
        self.imglineEdit3.setGeometry(QtCore.QRect(150, 750, 550, 40))
        self.imglineEdit3.setObjectName("imglineEdit")
        self.imgpushButton3 = QtWidgets.QPushButton(Form)
        self.imgpushButton3.setGeometry(QtCore.QRect(370, 810, 100, 30))
        self.imgpushButton3.setObjectName("imgpushButton3")

        self.label10= QtWidgets.QLabel(Form)
        self.label10.setGeometry(QtCore.QRect(1050, 700, 361, 70))
        self.label10.setText("Write name of option 4")
        self.label10.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.imgName3 = QtWidgets.QLineEdit(Form)
        self.imgName3.setGeometry(QtCore.QRect(880, 750, 600, 40))
        self.imgName3.setObjectName("imgName3")

        self.line5 = QtWidgets.QLineEdit(Form)
        self.line5.setGeometry(QtCore.QRect(20, 850, 1700, 1))
        self.line5.setObjectName("addName")
        

        self.labelp = QtWidgets.QLabel(Form)
        self.labelp.setGeometry(QtCore.QRect(250, 850, 361, 70))
        self.labelp.setText("Write down the answer of the question")
        self.labelp.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Black))
        self.answer = QtWidgets.QLineEdit(Form)
        self.answer.setGeometry(QtCore.QRect(150, 900,550, 51))
        self.answer.setObjectName("answer")

        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(1000, 900, 311, 50))
        self.objpushButton.setObjectName("objpushButton")
        self.addNameButton.clicked.connect(self.setImage1)
        self.imgpushButton1.clicked.connect(self.setImage2)
        self.imgpushButton2.clicked.connect(self.setImage3)
        self.imgpushButton3.clicked.connect(self.setImage4)
        self.vidpushButton.clicked.connect(self.setImage5)
        self.audpushButton.clicked.connect(self.setAudio)
        self.objpushButton.clicked.connect(self.additem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addNameButton.setText(_translate("Form","Add Object"))
        self.vidpushButton.setText(_translate("Form", "Add Image"))
        self.imgpushButton1.setText(_translate("Form", "Add Image"))
        self.imgpushButton2.setText(_translate("Form", "Add Image"))
        self.imgpushButton3.setText(_translate("Form", "Add Image"))
        self.audpushButton.setText(_translate("Form", "Add audio"))
        self.objpushButton.setText(_translate("Form", "Add Object"))

    def setImage1(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "home/anika/Downloads/question", "Image Files (*.png *.jpg *.jpeg *.bmp)")
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

    def setImage5(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "/home/anika/Downloads/images", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.vidlineEdit.setText(ifileName)


    def setVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "/home/anika/Downloads/videos", "*.mp4")
        print(fileName)
        self.vidlineEdit.setText(fileName)

    def setAudio(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Audio", "/home/anika/Downloads/audios/audios", "*.mp3 *.wav")
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
        nameObj=self.imgName.text()
        nameObj1=self.imgName1.text()
        nameObj2=self.imgName2.text()
        nameObj3=self.imgName3.text()
        answer= self.answer.text()
        sql = "INSERT INTO questions(qus_name,qus_audio,image_name1,image_name2,image_name3,image_name4,answer,imagePath1,\
        imagePath2, imagePath3, imagePath4) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s,%s)"
        val = (name,audfileName, nameObj,nameObj1,nameObj2,nameObj3,answer,vfileName,ifileName1,ifileName2,ifileName3 ) 
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
