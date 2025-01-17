# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1398, 653)
        MainWindow.setStyleSheet("QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"    border-radius: 20px;\n"
"}\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"QPushButton {\n"
"  background-color:  rgb(200,200,200);\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  font-weight: 600;\n"
"  background-color: #0b5ed7;\n"
"  border: 3px solid #9ac3fe;\n"
"  color: #fff;\n"
"}\n"
"QPushButton:pressed{\n"
"     background-color:rgb(0, 150, 255);\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(200,200,200);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"    background-color:  rgb(200,200,200);\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:  rgb(0, 85, 255);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:  rgb(0, 150, 255);\n"
"\n"
"}\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"    background-color:  rgb(200,200,200);\n"
"    border-radius: 10px;\n"
"}\n"
"/*QScrollBar::handle:vertical:hover{\n"
"    background-color:  rgb(0, 85, 255);\n"
"}\n"
"*/\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:  rgb(0, 85, 255)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1371, 561))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setStyleSheet("QHeaderView::section {\n"
"    background-color: rgb(200,200,200);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"    background-color:  rgb(200,200,200);\n"
"    border-radius: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover{\n"
"    background-color:  rgb(0, 85, 255);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"    background-color:  rgb(0, 150, 255);\n"
"\n"
"}\n"
"QScrollBar:vertical{\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"    background-color:  rgb(200,200,200);\n"
"    border-radius: 10px;\n"
"}\n"
"/*QScrollBar::handle:vertical:hover{\n"
"    background-color:  rgb(0, 85, 255);\n"
"}\n"
"*/\n"
"QScrollBar::handle:vertical:pressed{\n"
"    background-color:  rgb(0, 85, 255)\n"
"}")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.deny_button = QtWidgets.QPushButton(self.centralwidget)
        self.deny_button.setGeometry(QtCore.QRect(10, 570, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.deny_button.setFont(font)
        self.deny_button.setObjectName("deny_button")
        self.approve_button = QtWidgets.QPushButton(self.centralwidget)
        self.approve_button.setGeometry(QtCore.QRect(170, 570, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.approve_button.setFont(font)
        self.approve_button.setObjectName("approve_button")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(1210, 570, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.refresh_button.setFont(font)
        self.refresh_button.setObjectName("refresh_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-110, -10, 1511, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("6fadc29d97ab55aa5185d4116d5d10d3.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(558, 576, 283, 69))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("2560px-Roscosmos_Corp_Brand_2015.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.tableWidget.raise_()
        self.deny_button.raise_()
        self.approve_button.raise_()
        self.refresh_button.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактирование заявок на астрономические наблюдения"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Время"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Эл. почта"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Тип набл."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Р. старт"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "П. старт"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Прод-ть"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Смещение"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Величина"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Тип объекта"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Комментарий"))
        self.deny_button.setText(_translate("MainWindow", "Отклонить"))
        self.approve_button.setText(_translate("MainWindow", "Утвердить"))
        self.refresh_button.setText(_translate("MainWindow", "Обновить"))
