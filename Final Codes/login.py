# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from signup import Ui_SIGNUPFORM
import mysql.connector




class Ui_LOGINFORM(object):

    def showMessage(self, msgType, message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle(msgType)
        messageBox.setText(message)
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messageBox.exec_()

    def signUpCheck(self):
        print("Sign Up Button Clicked.")
        self.SIGNUPFORM = QtWidgets.QDialog()
        self.ui = Ui_SIGNUPFORM()
        self.ui.setupUi(self.SIGNUPFORM)
        self.SIGNUPFORM.show()

    def loginCheck(self):
        print("Log In Button Clicked.")
        uname = self.text_u_name.text()
        upass = self.text_pass.text()
        print(uname, " ", upass)

        mydb = mysql.connector.connect(
            host='localhost',
            user="root",
            passwd="ant904",
            database="loginDB"
            # auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor()
        sql = "SELECT * FROM Users WHERE Username = %s AND Password = %s"
        val = (uname, upass)
        myCursor.execute(sql, val)
        myresult = myCursor.fetchall()
        
        if myCursor.rowcount > 0:
            self.showMessage("Information", 'Log in successful.\nYou\'re welcome.')
        else:
            self.showMessage("Information", 'You have either no account or entered wrong info.\n \
            Sign up if required or try again.')

    def setupUi(self, LOGINFORM):
        LOGINFORM.setObjectName("LOGINFORM")
        LOGINFORM.resize(481, 341)
        LOGINFORM.setStyleSheet("QDialog{\n"
                                "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0    rgba(154, 189, 149, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                "}\n"
                                "\n"
                                "QLineEdit{\n"
                                "    background-color:rgb(239, 239, 179)\n"
                                "}\n"
                                "QPushButton#login{\n"
                                "    background-color:rgb(56, 25, 96);\n"
                                "    border:none;\n"
                                "    color:white;\n"
                                "}\n"
                                "QPushButton#signUp{\n"
                                "    background-color:rgb(56, 25, 96);\n"
                                "    border:none;\n"
                                "    color:white;\n"
                                "}")
        self.log_form = QtWidgets.QLabel(LOGINFORM)
        self.log_form.setGeometry(QtCore.QRect(100, 30, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.log_form.setFont(font)
        self.log_form.setObjectName("log_form")
        self.u_name = QtWidgets.QLabel(LOGINFORM)
        self.u_name.setGeometry(QtCore.QRect(60, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.u_name.setFont(font)
        self.u_name.setObjectName("u_name")
        self.pass1 = QtWidgets.QLabel(LOGINFORM)
        self.pass1.setGeometry(QtCore.QRect(60, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pass1.setFont(font)
        self.pass1.setObjectName("pass")
        self.text_u_name = QtWidgets.QLineEdit(LOGINFORM)
        self.text_u_name.setGeometry(QtCore.QRect(150, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text_u_name.setFont(font)
        self.text_u_name.setObjectName("text_u_name")
        self.text_pass = QtWidgets.QLineEdit(LOGINFORM)
        self.text_pass.setGeometry(QtCore.QRect(150, 170, 261, 31))
        self.text_pass.setObjectName("text_pass")
        self.login = QtWidgets.QPushButton(LOGINFORM)
        self.login.setGeometry(QtCore.QRect(310, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setObjectName("login")

        ############## Button Event#############
        self.login.clicked.connect(self.loginCheck)
        ############################################

        self.signUp = QtWidgets.QPushButton(LOGINFORM)
        self.signUp.setGeometry(QtCore.QRect(150, 250, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signUp.setFont(font)
        self.signUp.setObjectName("signUp")

        ############## Button Event#############
        self.signUp.clicked.connect(self.signUpCheck)
        ############################################

        self.line = QtWidgets.QFrame(LOGINFORM)
        self.line.setGeometry(QtCore.QRect(60, 80, 351, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(LOGINFORM)
        QtCore.QMetaObject.connectSlotsByName(LOGINFORM)

    def retranslateUi(self, LOGINFORM):
        _translate = QtCore.QCoreApplication.translate
        LOGINFORM.setWindowTitle(_translate("LOGINFORM", "SignUp/LogIn","none"))
        self.log_form.setText(_translate("LOGINFORM", "USER AUTHENTICATION"))
        self.u_name.setText(_translate("LOGINFORM", "Username"))
        self.pass1.setText(_translate("LOGINFORM", "Password"))
        self.login.setText(_translate("LOGINFORM", "LogIn"))
        self.signUp.setText(_translate("LOGINFORM", "Sign Up"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LOGINFORM = QtWidgets.QDialog()
    ui = Ui_LOGINFORM()
    ui.setupUi(LOGINFORM)
    LOGINFORM.show()
    sys.exit(app.exec_())

