# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dell\Desktop\backend\additem.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 609)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        self.imgLabel = QtWidgets.QLabel(Form)
        self.imgLabel.setGeometry(QtCore.QRect(310, 200, 241, 221))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setLineWidth(3)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.VideoLabel = QtWidgets.QLabel(Form)
        self.VideoLabel.setGeometry(QtCore.QRect(30, 200, 231, 81))
        self.VideoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.VideoLabel.setLineWidth(2)
        self.VideoLabel.setText("")
        self.VideoLabel.setObjectName("VideoLabel")
        self.audioLabel = QtWidgets.QLabel(Form)
        self.audioLabel.setGeometry(QtCore.QRect(590, 200, 191, 71))
        self.audioLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.audioLabel.setLineWidth(2)
        self.audioLabel.setText("")
        self.audioLabel.setObjectName("audioLabel")
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(90, 320, 93, 28))
        self.vidpushButton.setObjectName("vidpushButton")
        self.imgpushButton = QtWidgets.QPushButton(Form)
        self.imgpushButton.setGeometry(QtCore.QRect(390, 450, 93, 28))
        self.imgpushButton.setObjectName("imgpushButton")
        self.audpushButton = QtWidgets.QPushButton(Form)
        self.audpushButton.setGeometry(QtCore.QRect(640, 300, 93, 28))
        self.audpushButton.setObjectName("audpushButton")
        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(270, 520, 311, 61))
        self.objpushButton.setObjectName("objpushButton")
        self.addName = QtWidgets.QLineEdit(Form)
        self.addName.setGeometry(QtCore.QRect(250, 50, 361, 101))
        font = QtGui.QFont()
        font.setFamily("QFontDatabase.Bengali")
        self.addName.setFont(font)
        self.addName.setLocale(QtCore.QLocale(QtCore.QLocale.Bengali, QtCore.QLocale.Bangladesh))
        self.addName.setAlignment(QtCore.Qt.AlignCenter)
        self.addName.setObjectName("addName")

        self.imgpushButton.clicked.connect(self.setImage)
        self.vidpushButton.clicked.connect(self.setVideo)
        self.objpushButton.clicked.connect(self.additem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.vidpushButton.setText(_translate("Form", "Add Video"))
        self.imgpushButton.setText(_translate("Form", "Add Image"))
        self.audpushButton.setText(_translate("Form", "Add audio"))
        self.objpushButton.setText(_translate("Form", "Add Object"))



    def setImage(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        if ifileName:
            pixmap=QtGui.QPixmap(ifileName)
            pixmap=pixmap.scaled(self.imgLabel.width(),
                self.imgLabel.height(), QtCore.Qt.KeepAspectRatio)
            self.imgLabel.setPixmap(pixmap)
            self.imgLabel.setAlignment(QtCore.Qt.AlignCenter)
        return ifileName;

    def setVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "", "*.mp4")
        print(fileName)

    def additem(self):
        ifileName=self.setImage();
        print(ifileName)
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

