from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import tkinter as tk
from StartingPage import StartingPage
import mysql.connector

class App(QWidget):

    trial = 0
    UID = None
    username = None

    def __init__(self):
        super().__init__()
        '''
        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        '''
        self.width = 700
        self.height = 720
        self.left = 500
        self.top = 50
        #print(self.width, self.height)
        self.title = 'Sign Up/Sign In'
        self.initUI()

    def initUI(self):
        horUnit = int(self.width / 12)
        verUnit = int(self.height / 12)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: rgb(54, 75, 109);");

        self.lbl_heading = QLabel("USER AUTHENTICATION", self)
        self.lbl_heading.setStyleSheet("font-size: 22px; font-weight: bold; color: white;")
        self.lbl_heading.setGeometry(3.5*horUnit, 1*verUnit, 4.5*horUnit, 0.6*verUnit)

        self.lbl_username = QLabel("Username", self)
        self.lbl_username.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
        self.lbl_username.setGeometry(1*horUnit, 3*verUnit, 1.5*horUnit, 0.6*verUnit)

        self.txt_username = QLineEdit(self)
        self.txt_username.setPlaceholderText("username")
        self.txt_username.setStyleSheet("background-color: white")
        self.txt_username.setGeometry(3.5*horUnit, 3*verUnit, 7*horUnit, 0.6*verUnit)

        self.lbl_pwd = QLabel("Password", self)
        self.lbl_pwd.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")
        self.lbl_pwd.setGeometry(1*horUnit, 4.5*verUnit, 1.5*horUnit, 0.6*verUnit)

        self.txt_pwd = QLineEdit(self)
        self.txt_pwd.setPlaceholderText("Password")
        self.txt_pwd.setEchoMode(QLineEdit.Password)
        self.txt_pwd.setStyleSheet("background-color: white")
        self.txt_pwd.setGeometry(3.5*horUnit, 4.5*verUnit, 7*horUnit, 0.6*verUnit)

        self.btn_signUp = QPushButton('Sign Up', self)
        self.btn_signUp.setStyleSheet("background-color: lightgray; font-size: 16px; font-weight: bold;")
        self.btn_signUp.setGeometry(5*horUnit, 8*verUnit, 1.5*horUnit, 0.6*verUnit)
        self.btn_signUp.clicked.connect(self.on_click_signUp)

        self.btn_signIn = QPushButton('Sign In', self)
        self.btn_signIn.setStyleSheet("background-color: lightgray; font-size: 16px; font-weight: bold;")
        self.btn_signIn.setGeometry(8*horUnit, 8*verUnit, 1.5*horUnit, 0.6*verUnit)
        self.btn_signIn.clicked.connect(self.on_click_signIn)

        self.btn_reset = QPushButton('Reset', self)
        self.btn_reset.setStyleSheet("background-color: lightgray; font-size: 16px; font-weight: bold;")
        self.btn_reset.setGeometry(2*horUnit, 8*verUnit, 1.5*horUnit, 0.6*verUnit)
        self.btn_reset.hide()
        self.btn_reset.clicked.connect(self.on_click_reset)

        self.lbl_reset = QLabel("Want to reset password?", self)
        self.lbl_reset.setGeometry(2*horUnit, 6.5*verUnit, 5*horUnit, 0.5*verUnit)
        self.lbl_reset.hide()
        self.lbl_reset.setStyleSheet("font-size: 18px; font-weight: bold; color: lightgray; color: blue;")
        

        self.lbl_error = QLabel("Wrong Password. Try again!", self)
        self.lbl_error.setGeometry(4*horUnit, 5.5*verUnit, 5*horUnit, 0.5*verUnit)
        self.lbl_error.hide()
        self.lbl_error.setStyleSheet("font-size: 18px; font-weight: bold; color: lightgray; color: red;")

        self.show()


    def on_click_signUp(self):
        self.storeIntoDatabase()

        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Sign Up")
        messageBox.setText("Sign Up Successful!")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        messageBox.exec_()
       
        self.loadStartingPage()


    def on_click_signIn(self):
        
        App.trial +=1

        mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              #passwd="yourpassword",
              database="spl"
            )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT username, password FROM User")
        myresult = mycursor.fetchall()

        mycursor.close()
        mydb.close()

            
        name = self.txt_username.text()
        pwd = self.txt_pwd.text()
        print(name, " ", pwd, " ", App.trial)
        flag = False

        for row in myresult:
            if name == row[0] and pwd == row[1]:
                flag = True 
                self.loadStartingPage()
                break;
            elif name == row[0] and App.trial >= 5 :
                App.username = name
                self.txt_pwd.setText("");
                self.lbl_reset.show()
                self.btn_reset.show()
            
            #elif flag == False:
                #self.lbl_error.show()
            
        


    def on_click_reset(self):
        
        App.trial = 0
        self.lbl_error.hide()

        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            #passwd = "ant904",
            database="spl"
        )
        myCursor = mydb.cursor(buffered=True)

        #name = self.txt_username.text()
        pwd = self.txt_pwd.text()
        #print(name, " ", pwd)

        sql = "UPDATE User SET password = %s WHERE username = %s"
        val = (pwd, App.username)
        myCursor.execute(sql, val)
        mydb.commit()
        #print(myCursor.rowcount, "record inserted.")
        myCursor.close()
        mydb.close()
        
        
        
        if self.txt_pwd.text() != "":
            messageBox = QtWidgets.QMessageBox()
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            messageBox.setWindowTitle("Password Reset")
            messageBox.setText("Password Reset Successful!")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
            messageBox.exec_()

            self.loadStartingPage()
        else:
            messageBox = QtWidgets.QMessageBox()
            messageBox.setIcon(QtWidgets.QMessageBox.Information)
            messageBox.setWindowTitle("Input Not Found")
            messageBox.setText("Please fill up the password field.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
            messageBox.exec_()
        


    def storeIntoDatabase(self):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            #passwd = "ant904",
            database="spl"
        )
        myCursor = mydb.cursor(buffered=True)

        name = self.txt_username.text()
        pwd = self.txt_pwd.text()
        print(name, " ", pwd)

        sql = "INSERT INTO User (username, password) VALUES (%s, %s)"
        val = (name, pwd)
        myCursor.execute(sql, val)
        mydb.commit()
        #print(myCursor.rowcount, "record inserted.")
        myCursor.close()
        mydb.close()


    def loadStartingPage(self):
        name = self.txt_username.text()
        pwd = self.txt_pwd.text()
        print(name, " ", pwd)
        self.start = StartingPage()
        self.start.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = App()
    sys.exit(app.exec_())
