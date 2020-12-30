# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listbox = QtWidgets.QGroupBox(self.centralwidget)
        self.listbox.setGeometry(QtCore.QRect(30, 30, 551, 541))
        font = QtGui.QFont()
        font.setFamily("Rondalo")
        font.setPointSize(20)
        self.listbox.setFont(font)
        self.listbox.setAlignment(QtCore.Qt.AlignCenter)
        self.listbox.setObjectName("listbox")
        self.listtable = QtWidgets.QTableWidget(self.listbox)
        self.listtable.setGeometry(QtCore.QRect(40, 60, 441, 431))
        self.listtable.setRowCount(10)
        self.listtable.setColumnCount(1)
        self.listtable.setObjectName("listtable")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 100, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 180, 151, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 260, 151, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.read()

        self.pushButton.clicked.connect(self.addfile)
        self.pushButton_2.clicked.connect(self.openfile)
        self.pushButton_3.clicked.connect(self.read)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.listbox.setTitle(_translate("MainWindow", "list"))
        self.pushButton.setText(_translate("MainWindow", "add"))
        self.pushButton_2.setText(_translate("MainWindow", "open files"))
        self.pushButton_3.setText(_translate("MainWindow", "reload"))

    def addfile(self):
        file_n_a  = QFileDialog.getOpenFileName()
        file = open('save.txt', 'a')
        file.write(file_n_a[0] + "\n")

    def openfile(self):
        file = open('save.txt', 'r')
        for i in file.readlines():
            os.startfile(i[:-1])

    def read(self):
        self.data = []
        file = open('save.txt', 'r')
        for i in file.readlines():
            self.data.append(i)

        row = 0
        for e in self.data:
            print(e)
            self.listtable.setItem(row, 0, QtWidgets.QTableWidgetItem(e))
            row = row + 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
