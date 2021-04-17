from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisGui(object):
    def setupUi(self, JarvisGui):
        JarvisGui.setObjectName("JarvisGui")
        JarvisGui.resize(1376, 796)
        self.centralwidget = QtWidgets.QWidget(JarvisGui)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-60, 0, 1441, 841))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.bg.setFont(font)
        self.bg.setStyleSheet("")
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("img/bg1.gif"))
        self.bg.setObjectName("bg")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(920, 650, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(1100, 650, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.stop.setObjectName("stop")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(0, 20, 401, 131))
        self.img.setText("")
        self.img.setPixmap(QtGui.QPixmap("img/bg.gif"))
        self.img.setObjectName("img")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(650, 30, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: none;\n"
"background-color: transparent;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(960, 30, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: none;\n"
"background-color: transparent;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        JarvisGui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(JarvisGui)
        self.statusbar.setObjectName("statusbar")
        JarvisGui.setStatusBar(self.statusbar)

        self.retranslateUi(JarvisGui)
        QtCore.QMetaObject.connectSlotsByName(JarvisGui)

    def retranslateUi(self, JarvisGui):
        _translate = QtCore.QCoreApplication.translate
        JarvisGui.setWindowTitle(_translate("JarvisGui", "MainWindow"))
        self.start.setText(_translate("JarvisGui", "Start"))
        self.stop.setText(_translate("JarvisGui", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JarvisGui = QtWidgets.QMainWindow()
    ui = Ui_JarvisGui()
    ui.setupUi(JarvisGui)
    JarvisGui.show()
    sys.exit(app.exec_())
