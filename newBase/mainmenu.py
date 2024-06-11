# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1103, 784)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1103, 784))
        MainWindow.setMaximumSize(QtCore.QSize(1103, 784))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Astro/1b0b14f2-7525-4b4b-90fc-639c0496cbd9.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 751))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1101, 751))
        self.tabWidget.setMaximumSize(QtCore.QSize(1101, 751))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(0, 10, 256, 711))
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 121, 41))
        self.pushButton.setStyleSheet("background-color:rgb(133, 139, 255);color:rgb(247, 255, 251)\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1103, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuControl = QtWidgets.QMenu(self.menuBar)
        self.menuControl.setObjectName("menuControl")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLogs = QtWidgets.QAction(MainWindow)
        self.actionLogs.setObjectName("actionLogs")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAccounts = QtWidgets.QAction(MainWindow)
        self.actionAccounts.setEnabled(False)
        self.actionAccounts.setVisible(False)
        self.actionAccounts.setObjectName("actionAccounts")
        self.menuControl.addAction(self.actionLogs)
        self.menuControl.addAction(self.actionExit)
        self.menuControl.addAction(self.actionHelp)
        self.menuControl.addAction(self.actionAccounts)
        self.menuBar.addAction(self.menuControl.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное окно"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Основное меню"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Заявки"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Черновики"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Отправленные"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Подтвержденные"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Все"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "Новая заявка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Основное меню"))
        self.menuControl.setTitle(_translate("MainWindow", "Управление"))
        self.actionLogs.setText(_translate("MainWindow", "Логи"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.actionHelp.setText(_translate("MainWindow", "О программе"))
        self.actionAccounts.setText(_translate("MainWindow", "Аккаунты"))