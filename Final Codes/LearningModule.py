import sys
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage, QImageReader
from PyQt5.QtWidgets import QVBoxLayout
import mysql.connector
from PyQt5.QtMultimedia import QSound
import tkinter as tk
from new_qus import Ui_MainWindow


class App(QWidget):

    curFileId = 1
    ObjectID = 1
    total = 3
    img1 = None
    img2 = None
    img3 = None
    video = None
    audio = None
    objNameImg = None
    img = list()
    alreadyLearned = list()

    def __init__(self):
        super().__init__()

        root = tk.Tk()
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        self.left = 0
        self.top = 0
        print(self.width, self.height)

        self.title = 'WELCOME TO AUDIO-VISUAL LEARNING'


        self.initUI()

    def initUI(self):
        horUnit = int(self.width / 12)
        verUnit = int(self.height / 12)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # INITIAL DATABASE 
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "ant904",
            database="spl"
        )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT image_name_1, image_name_2, image_name_3, \
               object_image, audio_name, video_name FROM object where object_id = %s"
        val = (App.ObjectID,)
        myCursor.execute(sql, val)
        myresult = myCursor.fetchone()

        App.img.clear()
        App.img.append(myresult[0]) 
        App.img.append(myresult[1])
        App.img.append(myresult[2])
        App.objNameImg = myresult[3]
        App.audio = myresult[4]
        App.video = myresult[5]


        myCursor.close()
        mydb.close()


    #=========================================Video Part===============================================#

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(App.video)))     # NECESSARY
        self.playButton.setEnabled(True)

        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)


        # ===============================Image  widget========================================#
        

        self.imglabel = QLabel(self)
        self.imglabel.setGeometry(0.5*horUnit, 3*verUnit, 4.5*horUnit, 6*verUnit)
        # self.pixmap = QPixmap('C:/Users/dell/Downloads/Python-master/Python-master/ImageShow/mango.jpg')
        self.pixmap = QPixmap(App.img[0])
        self.pixmap = self.pixmap.scaled(self.imglabel.width(), self.imglabel.height(), QtCore.Qt.KeepAspectRatio)
        self.imglabel.setPixmap(self.pixmap)
        self.imglabel.setStyleSheet("background-color: lightgray;")
        self.imglabel.setAlignment(QtCore.Qt.AlignCenter)
        
        # audio button widget
        self.audioButton = QPushButton('\t PLAY AUDIO \t', self)
        self.audioButton.setToolTip('play audio')
        self.audioButton.setStyleSheet("background-color: lightgray; font-size: 12px; font-weight: bold;")
        self.audioButton.setGeometry(7*horUnit, 9.5*verUnit, 4.5*horUnit, 0.5*verUnit)
        self.audioButton.clicked.connect(lambda: self.play_audio(App.audio))                # NECESSARY

        # Previous button widget
        self.buttonP = QPushButton('\t PREVIOUS IMAGE \t', self)
        self.buttonP.setToolTip('Go to previous picture')
        self.buttonP.setStyleSheet("background-color: lightgray; font-size: 12px; font-weight: bold;")
        self.buttonP.setGeometry(0.5*horUnit, 9.5*verUnit, 1.2*horUnit, 0.5*verUnit)
        self.buttonP.clicked.connect(self.on_click_prev)

        # Skip button widget
        self.buttonS = QPushButton('\t SKIP THIS OBJECT \t', self)
        self.buttonS.setToolTip('Skip this object')
        self.buttonS.setStyleSheet("background-color: lightgray; font-size: 12px; font-weight: bold;")
        self.buttonS.setGeometry(2*horUnit, 9.5*verUnit, 1.5*horUnit, 0.5*verUnit)
        self.buttonS.clicked.connect(self.on_click_skip)

        # Next button widget
        self.buttonN = QPushButton('\t NEXT IMAGE \t', self)
        self.buttonN.setToolTip('Go to next picture')
        self.buttonN.setStyleSheet("background-color: lightgray; font-size: 12px; font-weight: bold;")
        self.buttonN.setGeometry(3.8*horUnit, 9.5*verUnit, 1.2*horUnit, 0.5*verUnit)
        self.buttonN.clicked.connect(self.on_click_next)


        # OBJECT NAME LABEL
        self.lblObjName = QLabel(self)
        self.pixmap = QPixmap(App.objNameImg)
        self.lblObjName.setPixmap(self.pixmap)
        self.lblObjName.setGeometry(3*horUnit, 0*verUnit, 6*horUnit, 2*verUnit)
        self.lblObjName.setAlignment(QtCore.Qt.AlignCenter)


        # Create a widget for window contents    
        self.wid = QWidget(self)
        self.wid.setGeometry(7*horUnit, 3*verUnit, 4.5*horUnit, 6*verUnit)
        self.wid.setStyleSheet("background-color: lightgray;")
        self.wid.setLayout(layout)
        self.wid.show()
        self.show()


    # ================== All User Defined Functions ====================== #

    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def showImage(self, filepath):
        self.imglabel.clear()
        pixmap = QtGui.QPixmap(filepath)
        pixmap = pixmap.scaled(self.imglabel.width(), self.imglabel.height(), QtCore.Qt.KeepAspectRatio)
        self.imglabel.setPixmap(pixmap)
        self.imglabel.setAlignment(QtCore.Qt.AlignCenter)


    def showObjectNameImage(self, filepath):
        print(filepath)
        self.lblObjName.clear()
        pixmap = QPixmap(filepath)
        pixmap = pixmap.scaled(self.imglabel.width(), self.imglabel.height(), QtCore.Qt.KeepAspectRatio)
        self.lblObjName.setPixmap(pixmap)
        self.imglabel.setAlignment(QtCore.Qt.AlignCenter)

    def play_audio(self, path):
        QSound.play(path)


    def on_click_prev(self):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "ant904",
            database="spl"
        )
        myCursor = mydb.cursor()

        if (App.curFileId - 1) < 1:
            if App.ObjectID - 1 < 1:
                self.buttonP.hide()
            else:
                sql = "SELECT image_name_1, image_name_2, image_name_3, \
                        object_image, audio_name, video_name FROM object where object_id = %s"
                val = (App.ObjectID - 1,)

                myCursor.execute(sql, val)
                myresult = myCursor.fetchone()
                myCursor.close()
                mydb.close()

                App.img.clear()
                App.img.append(myresult[0]) 
                App.img.append(myresult[1])
                App.img.append(myresult[2])
                App.objNameImg = myresult[3]
                App.audio = myresult[4]
                App.video = myresult[5]


                App.ObjectID -= 1
                App.curFileId = 1
                self.showImage(App.img[App.curFileId - 1])

                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(App.video)))     # NECESSARY
                self.playButton.setEnabled(True)

                self.showObjectNameImage(App.objNameImg)
            # self.buttonP.hide()
        else:
            self.buttonN.show()
            App.curFileId -= 1
            self.showImage(App.img[App.curFileId - 1])

    def on_click_next(self):
        if (App.curFileId + 1) > App.total:
            mydb = mysql.connector.connect(
                host = 'localhost',
                user = "root",
                passwd = "ant904",
                database="spl"
            )
            myCursor = mydb.cursor()
            sql = "SELECT image_name_1, image_name_2, image_name_3, \
                        object_image, audio_name, video_name FROM object where object_id = %s"
            val = (App.ObjectID + 1,)

            myCursor.execute(sql, val)
            myresult = myCursor.fetchone()
            myCursor.close()
            mydb.close()

            App.img.clear()
            App.img.append(myresult[0]) 
            App.img.append(myresult[1])
            App.img.append(myresult[2])
            App.objNameImg = myresult[3]
            App.audio = myresult[4]
            App.video = myresult[5]

            App.curFileId = 1
            App.ObjectID += 1

            if (App.ObjectID - 1) in App.alreadyLearned:
                self.showImage(App.img[App.curFileId - 1])

                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(App.video)))     # NECESSARY
                self.playButton.setEnabled(True)

                self.showObjectNameImage(App.objNameImg)
                # self.buttonN.hide()
            else:
                App.alreadyLearned.append(App.ObjectID - 1)

                self.showImage(App.img[App.curFileId - 1])

                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(App.video)))     # NECESSARY
                self.playButton.setEnabled(True)

                self.showObjectNameImage(App.objNameImg)

                self.showQuestionWindow(App.ObjectID - 1)
        else:
            self.buttonP.show()
            App.curFileId += 1
            self.showImage(App.img[App.curFileId - 1])

    def on_click_skip(self):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            passwd = "ant904",
            database="spl"
        )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT image_name_1, image_name_2, image_name_3, \
               object_image, audio_name, video_name FROM object where object_id = %s"
        val = (App.ObjectID + 1,)
        myCursor.execute(sql, val)
        myresult = myCursor.fetchone()

        App.img.clear()
        App.img.append(myresult[0]) 
        App.img.append(myresult[1])
        App.img.append(myresult[2])
        App.objNameImg = myresult[3]
        App.audio = myresult[4]
        App.video = myresult[5]

        myCursor.close()
        mydb.close()

        App.curFileId = 1
        App.ObjectID += 1

        self.showImage(App.img[App.curFileId - 1])

        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(App.video)))     # NECESSARY
        self.playButton.setEnabled(True)

        self.showObjectNameImage(App.objNameImg)


    def showQuestionWindow(self,objectID):
        self.QuesWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        #self.ui.setupUi()
        select=False
        self.ui.setDB(objectID)
        self.QuesWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = App()
    sys.exit(app.exec_())
