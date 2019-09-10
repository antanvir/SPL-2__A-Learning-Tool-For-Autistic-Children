from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QPushButton, QLabel
import tkinter as tk



class QuestionWindow(QWidget):
    def __init__(self, objectID, select, parent=None):
        super(QuestionWindow, self).__init__(parent)

        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.left = 0
        self.top = 0

        self.title = 'Updated Question Panel'
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")

        self.objectID = objectID
        self.select = select

        self.setupUI()


    def setupUI(self):
        horUnit = int(self.width / 12)
        verUnit = int(self.height / 12)

        self.lblQuestion = QLabel(self)
        self.pixmap = QPixmap("question/chamoch.png")
        self.lblQuestion.setPixmap(self.pixmap)
        self.lblQuestion.setGeometry(3*horUnit, 0*verUnit, 6*horUnit, 3*verUnit)
        self.lblQuestion.setAlignment(QtCore.Qt.AlignCenter)

        self.rButton1 = QtWidgets.QRadioButton(self)
        self.rButton2 = QtWidgets.QRadioButton(self)
        self.rButton3 = QtWidgets.QRadioButton(self)
        self.rButton4 = QtWidgets.QRadioButton(self)

        self.rButton1.setIcon(QIcon("images/bati_2.png"))
        self.rButton1.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton1.setGeometry(0.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton1.name = "bati"
        self.rButton1.toggled.connect(self.onClicked)


        self.rButton2.setIcon(QIcon("images/glass_2.png"))
        self.rButton2.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton2.setGeometry(3.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton2.name = "glass"
        self.rButton2.toggled.connect(self.onClicked)


        self.rButton3.setIcon(QIcon("images/chamoch_1.png"))
        self.rButton3.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton3.setGeometry(6.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton3.name = "chamoch"
        self.rButton3.toggled.connect(self.onClicked)


        self.rButton4.setIcon(QIcon("images/pani_1.png"))
        self.rButton4.setIconSize(QtCore.QSize(2*horUnit, 2*verUnit))
        self.rButton4.setGeometry(9.5*horUnit, 4*verUnit, 2*horUnit, 2*verUnit)
        self.rButton4.name = "pani"
        self.rButton4.toggled.connect(self.onClicked)

        self.lblResult = QLabel(self)
        # self.pixmap = QPixmap("right.png")
        # self.lblResult.setPixmap(self.pixmap)
        self.lblResult.setGeometry(3*horUnit, 6.8*verUnit, 6*horUnit, 4*verUnit)
        self.lblResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblResult.setVisible(False)


    def onClicked(self):
        originalAnswer = "chamoch"
        buttonPressed = self.sender()

        if buttonPressed.isChecked():
            print("Image pressed is: %s" % (buttonPressed.name))

        if buttonPressed.name == originalAnswer:
            self.pixmap = QPixmap("right.png")
            self.lblResult.setPixmap(self.pixmap)
            self.lblResult.setVisible(True)
        else:
            self.pixmap = QPixmap("wrong.png")
            self.lblResult.setPixmap(self.pixmap)
            self.lblResult.setVisible(True)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    display = QuestionWindow(objectID = 1, select = False)
    display.show()
    sys.exit(app.exec_())


# # Learning Module theke call , amartay run hoy na tai test kora gelo na LearningModule theke #
        # self.QuesWindow = QtWidgets.QMainWindow()
        # self.obj = QuestionWindow(self.objectID, select = False) # self.obj hsse class instance
        # self.QuesWindow.show()