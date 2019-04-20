'''
### THINGS TO DO ###

If NEXT button pressed & 'this' obj images run out:
    If 'this' obj already learned (i.e. question answered)
        it will load the next obj image
    Otherwise,
        it will load Question Window

Code for SKIP functionality

'''


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
# from qus2 import Ui_MainWindow
# from PyQt5.QtCore import pyqtSlot


class LearningModule(QWidget):

    curFileId = 1
    ObjectID = 1
    total = 3
    img1 = None
    img2 = None
    img3 = None
    img = list()
    alreadyLearned = list()

    def __init__(self):
        super().__init__()

        self.title = 'WELCOME TO AUDIO-VISUAL LEARNING'
        self.left = 50
        self.top = 50
        self.width = 1250  # 680
        self.height = 620  # 480

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: lightgray;")
    #=========================================Video Part===============================================#
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()
        # videoWidget.setStyleSheet("background-color: black;")

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                                      QSizePolicy.Maximum)

        self.mediaPlayer.setMedia(
            QMediaContent(QUrl.fromLocalFile
                          ("akifa.mp4")))
        self.playButton.setEnabled(True)

        # Create a widget for window contents
        wid = QWidget(self)
        wid.setGeometry(650, 30, 500, 400)
        wid.setStyleSheet("background-color: lightgray;")
        # wid.setCentralWidget(wid)
        '''
        player = QMainWindow()
        wid = QWidget(self)
        player.setCentralWidget(wid)
        '''
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)
        # layout.setStyleSheet("background-color: black;")

        # Set widget to contain window contents
        # mainlayout.setLayout(layout)
        wid.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        # self.mediaPlayer.show()
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        wid.show()
        # =====================================================================================#
        '''
        # Image  widget
        mydb = mysql.connector.connect(
            host='localhost',
            user="root",
            # passwd="",
            database="spl"
            # auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT image_name_1, image_name_2, image_name_3 FROM object where object_id = %s"
        val = (App.ObjectID,)
        myCursor.execute(sql, val)
        myresult = myCursor.fetchone()
        # App.img1, App.img2, App.img3 = myresult[0], myresult[1], myresult[2]
        App.img[0], App.img[1], App.img[2] = myresult[0], myresult[1], myresult[2]


        myCursor.close()
        mydb.close()

        self.label = QLabel(self)

        # self.pixmap = QPixmap('C:/Users/dell/Downloads/Python-master/Python-master/ImageShow/mango.jpg')
        self.pixmap = QPixmap(App.img[0])
        self.label.setPixmap(self.pixmap)
        self.label.setGeometry(50, 30, 550, 400)
        # self.resize(pixmap.width(),pixmap.height())
        # self.resize(640,450)
        '''
        # audio button widget
        self.pushButton = QPushButton('Play Audio', self)
        self.pushButton.setToolTip('play audio')
        self.pushButton.setGeometry(100, 550, 375, 28)
        self.pushButton.clicked.connect(self.play_audio)

        # Previous button widget
        self.buttonP = QPushButton('PREVIOUS', self)
        self.buttonP.setToolTip('Go to previous picture')
        self.buttonP.move(100, 500)
        self.buttonP.clicked.connect(self.on_click_prev)

        # Skip button widget
        self.buttonS = QPushButton('SKIP OBJECT', self)
        self.buttonS.setToolTip('Skip this object')
        self.buttonS.move(300, 500)
        self.buttonS.clicked.connect(self.on_click_skip)

        # Next button widget
        self.buttonN = QPushButton('NEXT', self)
        self.buttonN.setToolTip('Go to next picture')
        self.buttonN.move(500, 500)
        self.buttonN.clicked.connect(self.on_click_next)

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

        self.label.clear()
        print("from showImage function: ", filepath)

        pixmap = QtGui.QPixmap(filepath)
        pixmap = pixmap.scaled(self.label.width(),
                               self.label.height(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        # print("doesn't show")

    def play_audio(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user="root",
            # passwd="",
            database="spl"
            # auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT audioName FROM item where object_id=8"
        myCursor.execute(sql)
        row = myCursor.fetchone()
        for file in row:
            print(file)
            ifileName = str(file)
            # print("lol"+ifileName)
            if ifileName:
                QSound.play(ifileName)
                # self.setImage(ifileName)
        myCursor.close()
        mydb.close()

    def on_click_prev(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user="root",
            # passwd="",
            database="spl"
            # auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor()
        # global curFileId
        if (App.curFileId - 1) < 1:
            if App.ObjectID - 1 < 1:
                self.buttonP.hide()
            else:
                sql = "SELECT image_name_1, image_name_2, image_name_3 FROM object where object_id = %s"
                val = (App.ObjectID - 1,)
                myCursor.execute(sql, val)
                myresult = myCursor.fetchone()
                myCursor.close()
                mydb.close()
                # App.img1, App.img2, App.img3 = myresult[0], myresult[1], myresult[2]
                App.img[0], App.img[1], App.img[2] = myresult[0], myresult[1], myresult[2]

                App.ObjectID -= 1
                App.curFileId = 1
                self.showImage(App.img[App.curFileId - 1])
            # self.buttonP.hide()
        else:
            self.buttonN.show()
            App.curFileId -= 1
            self.showImage(App.img[App.curFileId - 1])

    def on_click_next(self):
        # print("in next click")
        # print(" total: ", total, " curFileId: ", App.curFileId)
        if (App.curFileId + 1) > App.total:
            mydb = mysql.connector.connect(
                host='localhost',
                user="root",
                # passwd="",
                database="spl"
                # auth_plugin='mysql_native_password'
            )
            myCursor = mydb.cursor()
            sql = "SELECT image_name_1, image_name_2, image_name_3 FROM object where object_id = %s"
            val = (App.ObjectID + 1,)
            myCursor.execute(sql, val)
            myresult = myCursor.fetchone()
            myCursor.close()
            mydb.close()
            App.img[0], App.img[1], App.img[2] = myresult[0], myresult[1], myresult[2]

            App.curFileId = 1
            App.ObjectID += 1

            if App.ObjectID in App.alreadyLearned:
                self.showImage(App.img[App.curFileId - 1])
                # self.buttonN.hide()
            else:
                self.showQuestionWindow()
                print("Question window called")
                App.alreadyLearned.append(App.ObjectID)
                self.showImage(App.img[App.curFileId - 1])
        else:
            self.buttonP.show()
            App.curFileId += 1
            self.showImage(App.img[App.curFileId - 1])

    def on_click_skip(self):
        "WILL BE WRITTEN"
        # print("in skip click")
        mydb = mysql.connector.connect(
            host='localhost',
            user="root",
            # passwd="",
            database="spl"
            # auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT Path FROM ImagePath where Image_ID = %s"
        val = (App.curFileId + 1,)
        myCursor.execute(sql, val)
        myresult = myCursor.fetchone()
        for data in myresult:
            print(data)
            # file = record
            self.showImage(data)
            # global curFileId
            App.curFileId += 1
        myCursor.close()
        mydb.close()

    def showQuestionWindow(self):
        self.QuesWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.QuesWindow)
        self.QuesWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = LearningModule()
    sys.exit(app.exec_())
