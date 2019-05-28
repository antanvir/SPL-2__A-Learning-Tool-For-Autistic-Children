import random

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import mysql.connector
from PyQt5 import QtGui, QtCore, QtWidgets

class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.axis = self.figure.add_subplot(111)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)

class ThreadSample(QtCore.QThread):
    newSample = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(ThreadSample, self).__init__(parent)

    def run(self):
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = "root",
            #passwd = "ant904",
            database = "spl"
    #auth_plugin='mysql_native_password'
        )
        myCursor = mydb.cursor(buffered=True)
        controlGameTime=list()
        testGameTIme=list()
        for i in range(1,8):
            sql = "SELECT game.elapsedTime,controlGroup.gameTime from game,controlGroup where game_id=%s"
            val=(i,)
            print(i)
            myCursor.execute(sql,val)
            row=myCursor.fetchone()
            controlGameTime.append(row[1])
            testGameTIme.append(row[0])
        qusTimeList=list()
        qusTimeList.append("0:00:03")
        qusTimeList.append("0:00:02")
        qusTimeList.append("0:00:05")
        qusTimeList.append("0:00:06")
        qusTimeList.append("0:00:08")
        qusTimeList.append("0:00:02")
        qusTimeList.append("0:00:03")
        qusTimeList.append("0:00:03")
        qusTimeList.append("0:00:04")
        qusTimeList.append("0:00:05")
        qusTimeList.append("0:00:08")

        gameTimeList=list()
        gameTimeList.append("0:00:13")
        gameTimeList.append("0:00:19")
        gameTimeList.append("0:00:24")
        gameTimeList.append("0:00:08")
        gameTimeList.append("0:00:09")
        gameTimeList.append("0:00:13")
        gameTimeList.append("0:00:08")
        gameTimeList.append("0:00:09")
        gameTimeList.append("0:00:13")
        gameTimeList.append("0:00:14")
        gameTimeList.append("0:00:12")

        randomSample = random.sample(range(0, 10), 10)
        print(randomSample)
        #self.newSample.emit(qusTimeList)
        #self.newSample.emit(gameTimeList)
        self.newSample.emit(controlGameTime) #############ei duita line thakbe###########
        self.newSample.emit(testGameTIme)
        mydb.commit()
        myCursor.close()
        mydb.close()

class MyWindowGame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindowGame, self).__init__(parent)

        self.pushButtonPlot = QtWidgets.QPushButton(self)
        self.pushButtonPlot.setText("Plot")
        self.pushButtonPlot.clicked.connect(self.on_pushButtonPlot_clicked)

        self.matplotlibWidget = MatplotlibWidget(self)

        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPlot)
        self.layoutVertical.addWidget(self.matplotlibWidget)

        self.threadSample = ThreadSample(self)
        self.threadSample.newSample.connect(self.on_threadSample_newSample)
        self.threadSample.finished.connect(self.on_threadSample_finished)

    @QtCore.pyqtSlot()
    def on_pushButtonPlot_clicked(self):
        self.samples = 0
        self.matplotlibWidget.axis.clear()
        self.threadSample.start()

    @QtCore.pyqtSlot(list)
    def on_threadSample_newSample(self, sample):
        self.matplotlibWidget.axis.plot(sample)
        self.matplotlibWidget.canvas.draw()

    @QtCore.pyqtSlot()
    def on_threadSample_finished(self):
        self.samples += 1
        if self.samples <= 2:
            self.threadSample.start()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindowGame')

    main = MyWindowGame()
    main.resize(666, 333)
    main.show()

    sys.exit(app.exec_())
