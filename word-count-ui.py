# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 493)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 541, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yellow = QtWidgets.QCheckBox(self.centralwidget)
        self.yellow.setGeometry(QtCore.QRect(10, 100, 70, 17))
        self.yellow.setObjectName("yellow")
        self.red = QtWidgets.QCheckBox(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(10, 120, 70, 17))
        self.red.setObjectName("red")
        self.green = QtWidgets.QCheckBox(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(10, 140, 70, 17))
        self.green.setObjectName("green")
        self.blue = QtWidgets.QCheckBox(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(10, 160, 70, 17))
        self.blue.setObjectName("blue")
        self.cyan = QtWidgets.QCheckBox(self.centralwidget)
        self.cyan.setGeometry(QtCore.QRect(10, 220, 70, 17))
        self.cyan.setObjectName("cyan")
        self.pink = QtWidgets.QCheckBox(self.centralwidget)
        self.pink.setGeometry(QtCore.QRect(10, 200, 70, 17))
        self.pink.setObjectName("pink")
        self.gray = QtWidgets.QCheckBox(self.centralwidget)
        self.gray.setGeometry(QtCore.QRect(10, 180, 70, 17))
        self.gray.setObjectName("gray")
        self.dyellow = QtWidgets.QCheckBox(self.centralwidget)
        self.dyellow.setGeometry(QtCore.QRect(10, 320, 70, 17))
        self.dyellow.setObjectName("dyellow")
        self.dred = QtWidgets.QCheckBox(self.centralwidget)
        self.dred.setGeometry(QtCore.QRect(10, 300, 70, 17))
        self.dred.setObjectName("dred")
        self.dblue = QtWidgets.QCheckBox(self.centralwidget)
        self.dblue.setGeometry(QtCore.QRect(10, 280, 70, 17))
        self.dblue.setObjectName("dblue")
        self.white = QtWidgets.QCheckBox(self.centralwidget)
        self.white.setGeometry(QtCore.QRect(10, 240, 70, 17))
        self.white.setObjectName("white")
        self.black = QtWidgets.QCheckBox(self.centralwidget)
        self.black.setGeometry(QtCore.QRect(10, 260, 70, 17))
        self.black.setObjectName("black")
        self.dpink = QtWidgets.QCheckBox(self.centralwidget)
        self.dpink.setGeometry(QtCore.QRect(10, 400, 101, 17))
        self.dpink.setObjectName("dpink")
        self.dcyan = QtWidgets.QCheckBox(self.centralwidget)
        self.dcyan.setGeometry(QtCore.QRect(10, 380, 70, 17))
        self.dcyan.setObjectName("dcyan")
        self.dgreen = QtWidgets.QCheckBox(self.centralwidget)
        self.dgreen.setGeometry(QtCore.QRect(10, 360, 91, 17))
        self.dgreen.setObjectName("dgreen")
        self.dgray = QtWidgets.QCheckBox(self.centralwidget)
        self.dgray.setGeometry(QtCore.QRect(10, 340, 70, 17))
        self.dgray.setObjectName("dgray")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.calculate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_btn.setGeometry(QtCore.QRect(10, 430, 311, 23))
        self.calculate_btn.setObjectName("calculate_btn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(340, 111, 291, 341))
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.calculate_btn.clicked.connect(self.get_data) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Path of file:"))
        self.yellow.setText(_translate("MainWindow", "Yellow"))
        self.red.setText(_translate("MainWindow", "Red"))
        self.green.setText(_translate("MainWindow", "Green"))
        self.blue.setText(_translate("MainWindow", "Blue"))
        self.cyan.setText(_translate("MainWindow", "Cyan "))
        self.pink.setText(_translate("MainWindow", "Pink"))
        self.gray.setText(_translate("MainWindow", "Gray"))
        self.dyellow.setText(_translate("MainWindow", "Dark Yellow"))
        self.dred.setText(_translate("MainWindow", "Dark Red"))
        self.dblue.setText(_translate("MainWindow", "Dark Blue"))
        self.white.setText(_translate("MainWindow", "White "))
        self.black.setText(_translate("MainWindow", "Black"))
        self.dpink.setText(_translate("MainWindow", "Dark Pink"))
        self.dcyan.setText(_translate("MainWindow", "Dark Cyan"))
        self.dgreen.setText(_translate("MainWindow", "Dark Green"))
        self.dgray.setText(_translate("MainWindow", "Dark Gray"))
        self.label_2.setText(_translate("MainWindow", "Check the coloers want to calculate"))
        self.calculate_btn.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "Statistics"))
    def get_data(self):
        print("Worked!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
