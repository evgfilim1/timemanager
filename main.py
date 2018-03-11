# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(732, 242)
        MainWindow.setMinimumSize(QtCore.QSize(700, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.table_area = QtWidgets.QScrollArea(self.centralwidget)
        self.table_area.setWidgetResizable(True)
        self.table_area.setObjectName("table_area")
        self.table_contents = TableContents()
        self.table_contents.setGeometry(QtCore.QRect(0, 0, 712, 155))
        self.table_contents.setObjectName("table_contents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.table_contents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.table_contents)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.table_area.setWidget(self.table_contents)
        self.gridLayout.addWidget(self.table_area, 2, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 1)
        self.head = Head(self.centralwidget)
        self.head.setObjectName("head")
        self.gridLayout.addWidget(self.head, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 732, 20))
        self.menuBar.setObjectName("menuBar")
        self.menu_neural = QtWidgets.QMenu(self.menuBar)
        self.menu_neural.setObjectName("menu_neural")
        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_file.setObjectName("menu_file")
        self.menu_queue = QtWidgets.QMenu(self.menuBar)
        self.menu_queue.setObjectName("menu_queue")
        self.menu_help = QtWidgets.QMenu(self.menuBar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menuBar)
        self.action_teach = QtWidgets.QAction(MainWindow)
        self.action_teach.setObjectName("action_teach")
        self.action_clear = QtWidgets.QAction(MainWindow)
        self.action_clear.setObjectName("action_clear")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_qclear = QtWidgets.QAction(MainWindow)
        self.action_qclear.setObjectName("action_qclear")
        self.action_Qt = QtWidgets.QAction(MainWindow)
        self.action_Qt.setObjectName("action_Qt")
        self.actionada = QtWidgets.QAction(MainWindow)
        self.actionada.setObjectName("actionada")
        self.menu_neural.addAction(self.action_teach)
        self.menu_neural.addAction(self.action_clear)
        self.menu_file.addAction(self.action_exit)
        self.menu_queue.addAction(self.action_qclear)
        self.menu_help.addAction(self.action_Qt)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_neural.menuAction())
        self.menuBar.addAction(self.menu_queue.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeManager"))
        self.menu_neural.setTitle(_translate("MainWindow", "&Нейронная сеть"))
        self.menu_file.setTitle(_translate("MainWindow", "&Файл"))
        self.menu_queue.setTitle(_translate("MainWindow", "&Очередь"))
        self.menu_help.setTitle(_translate("MainWindow", "&Справка"))
        self.action_teach.setText(_translate("MainWindow", "&Обучить"))
        self.action_clear.setText(_translate("MainWindow", "О&чистить"))
        self.action_3.setText(_translate("MainWindow", "Сохранить"))
        self.action_4.setText(_translate("MainWindow", "Выход"))
        self.action_exit.setText(_translate("MainWindow", "&Выход"))
        self.action_qclear.setText(_translate("MainWindow", "&Очистить"))
        self.action_Qt.setText(_translate("MainWindow", "&О Qt"))
        self.actionada.setText(_translate("MainWindow", "ada"))

from head import Head
from tablecontents import TableContents
