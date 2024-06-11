from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic.properties import QtGui

# импорт из файлов с бд
from SqliteHelper import *
from SqliteHelper_req import *

# создаю переменные которые присвоены к графическим интерфейсам
app = QtWidgets.QApplication([])
sgn_on = uic.loadUi('signon.ui')
sgn_in = uic.loadUi('singin.ui')
chng = uic.loadUi('change.ui')
dlg = uic.loadUi("test.ui")
main_menu = uic.loadUi('mainmenu.ui')
help_form = uic.loadUi('help.ui')
logs = uic.loadUi('logsWindow.ui')
obs = uic.loadUi('observation_edit_form.ui')
helper = SqliteHelper('testik.db')
helper_request = SqliteHelper_req('test.db')

admin_login = "admin"
admin_password = "admin"

def msgbtn(i):
    print("Button pressed is:", i.text())


# ниже будут описаны функции для работы с бд которая относится к пользователям
# загружаю данные из базы данных
def loadData():
    users = helper.select("SELECT * FROM userss")
    # создаю определенное количество строк, зависимое от созданных пользователей
    for row_number, user in enumerate(users):
        dlg.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            dlg.tableWidget.setItem(row_number, column_number, cell)


# очистка данных(для обновления таблицы визуально)
def clearData():
    dlg.tableWidget.clearSelection()
    while (dlg.tableWidget.rowCount() > 0):
        dlg.tableWidget.removeRow(0)
        dlg.tableWidget.clearSelection()


# добавляю пользователя
def addUser():
    # переменная соответствует полю ввода
    inv = sgn_on.lineEdit.text()
    username = sgn_on.lineEdit_2.text()
    Honorific = sgn_on.lineEdit_3.text()
    First_Name = sgn_on.lineEdit_4.text()
    Middle_name = sgn_on.lineEdit_5.text()
    Last_Name = sgn_on.lineEdit_6.text()
    Organisation = sgn_on.lineEdit_7.text()
    Adress = sgn_on.lineEdit_8.text()
    Country = sgn_on.lineEdit_11.text()
    Phone_Num = sgn_on.lineEdit_9.text()
    Fax_Num = sgn_on.lineEdit_10.text()
    Email = sgn_on.lineEdit_12.text()
    Login = sgn_on.lineEdit_13.text()
    Password = sgn_on.lineEdit_14.text()

    # проверка наличия пользователя с таким же логином
    login = helper.select(f"SELECT Login FROM userss WHERE login='{Login}'")
    if len(Adress.strip(' ')) <= 5 or \
            len(Login.strip(' ')) < 3 or \
            len(Password.strip(' ')) < 4 or \
            len(First_Name.strip(' ')) < 2 or \
            len(Last_Name.strip(' ')) < 2 or \
            len(Country.strip(' ')) < 2 or \
            len(Email.strip(' ')) < 8 or \
            len(Password.strip(' ')) < 4:
        show_message('Ошибка!', 'Заполните обязательные поля!')
    else:
        # ошибка на введение длины данных
        if len(username.strip(' ')) <= 5:
            show_message('Ошибка!', 'Длина ника должна содержать 6 или более символов')
        else:
            if (len(login) != 0):
                show_message('Ошибка!', 'Такой пользователь уже существует!')

            else:
                # ошибка на введение электронной почты
                if "@" not in Email.strip(' '):
                    show_message('Ошибка!', 'Email должен содержать "@"')
                else:
                    user = (
                        inv, username, Honorific, First_Name, Middle_name, Last_Name, Organisation, Adress, Country,
                        Phone_Num,
                        Fax_Num,
                        Email, Login, Password)
                    # вставить данные из полей в БД
                    helper.insert(
                        "INSERT INTO userss (inv,username,Honorific,First_Name,Middle_name,Last_Name,Organisation,Adress,Country,Phone_Num,Fax_Num,Email,Login,Password) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        user)
                    refresh()
                    # когда уже регистрация прошла, только после этого форма с БД откроется
                    sgn_on.close()


# выделяем строку
def selectionChanged():
    chng.show()
    selected_row = getSelectedRow()
    user_id = getSelectedUser()

    inv = dlg.tableWidget.item(selected_row, 1).text()
    username = dlg.tableWidget.item(selected_row, 2).text()
    Honorific = dlg.tableWidget.item(selected_row, 3).text()
    First_Name = dlg.tableWidget.item(selected_row, 4).text()
    Middle_name = dlg.tableWidget.item(selected_row, 5).text()
    Last_Name = dlg.tableWidget.item(selected_row, 6).text()
    Organisation = dlg.tableWidget.item(selected_row, 7).text()
    Adress = dlg.tableWidget.item(selected_row, 8).text()
    Country = dlg.tableWidget.item(selected_row, 11).text()
    Phone_Num = dlg.tableWidget.item(selected_row, 9).text()
    Fax_Num = dlg.tableWidget.item(selected_row, 10).text()
    Email = dlg.tableWidget.item(selected_row, 12).text()
    Login = dlg.tableWidget.item(selected_row, 13).text()
    Password = dlg.tableWidget.item(selected_row, 14).text()
    # возвращаем значения
    chng.lineEdit.setText(inv)
    chng.lineEdit_2.setText(username)
    chng.lineEdit_3.setText(Honorific)
    chng.lineEdit_4.setText(First_Name)
    chng.lineEdit_5.setText(Middle_name)
    chng.lineEdit_6.setText(Last_Name)
    chng.lineEdit_7.setText(Organisation)
    chng.lineEdit_8.setText(Adress)
    chng.lineEdit_9.setText(Country)
    chng.lineEdit_10.setText(Phone_Num)
    chng.lineEdit_11.setText(Fax_Num)
    chng.lineEdit_12.setText(Email)
    chng.lineEdit_13.setText(Login)
    chng.lineEdit_14.setText(Password)


# выбранная строка
def getSelectedRow():
    return dlg.tableWidget.currentRow()


# строка соответствует определенному пользователю
def getSelectedUser():
    return dlg.tableWidget.item(getSelectedRow(), 0).text()


# удалить пользователя
def deleteUser():
    id_delete = getSelectedUser()
    helper.delete("DELETE FROM userss WHERE id=" + id_delete)
    refresh()
    chng.close()


# обновить данные о пользователе(так же как и добавить, в принципе поменяла только запрос для БД)
def updateUser():
    id_update = getSelectedUser()

    inv = chng.lineEdit.text()
    username = chng.lineEdit_2.text()
    Honorific = chng.lineEdit_3.text()
    First_Name = chng.lineEdit_4.text()
    Middle_name = chng.lineEdit_5.text()
    Last_Name = chng.lineEdit_6.text()
    Organisation = chng.lineEdit_7.text()
    Country = chng.lineEdit_8.text()
    Adress = chng.lineEdit_11.text()
    Phone_Num = chng.lineEdit_9.text()
    Fax_Num = chng.lineEdit_10.text()
    Email = chng.lineEdit_12.text()
    Login = chng.lineEdit_13.text()
    Password = chng.lineEdit_14.text()

    if username.strip(' ') != "" and First_Name.strip(' ') != "" and Adress.strip(' ') != "":
        user = (
            inv, username, Honorific, First_Name, Middle_name, Last_Name, Organisation, Adress, Country, Phone_Num,
            Fax_Num,
            Email, Login, Password)
        helper.edit(
            "UPDATE userss SET inv=?,username=?,Honorific=?,First_Name=?,Middle_name=?,Last_Name=?,Organisation=?,Adress=?,Country=?,Phone_Num=?,Fax_Num=?,Email=?,Login=?,Password=? WHERE id=" + id_update,
            user)
        refresh()
    else:
        show_message('Error')
        main_menu.close()
    chng.close()


# обновить БД, чтобы визуально это было почти незаметно(очистить-загрузить)
def refresh():
    clearData()
    loadData()


# ДАЛЕЕ ФУНКЦИИ ДЛЯ РАБОТЫ С БД ЗАЯВОК
def refresh_req():
    clearData_req()
    loadData_req()


def loadData_req():
    request = helper_request.select("SELECT * FROM request")
    for row_number, user in enumerate(request):
        obs.tableWidget.insertRow(row_number)
        for column_number, data in enumerate(user):
            cell = QtWidgets.QTableWidgetItem(str(data))
            obs.tableWidget.setItem(row_number, column_number, cell)


def clearData_req():
    obs.tableWidget.clearSelection()
    while (obs.tableWidget.rowCount() > 0):
        obs.tableWidget.removeRow(0)
        obs.tableWidget.clearSelection()


# запрос подтверждения создания заявки
def addRequestCheck():
    def click(b):
        if b.text() == "OK":
            addRequest()

    error = QMessageBox()
    error.setWindowTitle("Внимание!")
    error.setText("Вы уверены, что хотите создать эту заявку?")
    error.setIcon(QMessageBox.Question)
    error.addButton("Да", QMessageBox.YesRole)
    error.addButton("Нет", QMessageBox.NoRole)
    error.buttonClicked.connect(click)

    error.exec_()


# создание заявки
def addRequest():
    addRequestCheck()
    Type = obs.comboBox.currentText()
    SubType = obs.comboBox_2.currentText()
    Early_Start = obs.dateTimeEdit.dateTime().toString('dd-MM-yyyy HH:mm')
    Late_Start = obs.dateTimeEdit_2.dateTime().toString('dd-MM-yyyy HH:mm')
    Duration = obs.lineEdit_7.text()
    Target_Name = obs.lineEdit_2.text()
    Right_Ascression = obs.lineEdit_3.text()
    V_Magnitude = obs.lineEdit_4.text()
    Target_Type = obs.comboBox_3.currentText()
    Decination = obs.lineEdit_5.text()
    Other_Fluxes = obs.lineEdit_6.text()

    user = (
        Type, SubType, Early_Start, Late_Start, Duration, Target_Name, Right_Ascression, V_Magnitude,
        Target_Type,
        Decination, Other_Fluxes)
    helper_request.insert(
        "INSERT INTO request(Type,SubType,Early_Start,Late_Start,Duration,Target_Name,Right_Ascression,V_Magnitude,Target_Type,Decination,Other_Fluxes) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        user)
    refresh_req()
    mainmenu_refresh()


def selectionChangedRequest():
    selected_row = getSelectedRowReq()
    user_id = getSelectedRequest()

    Type = obs.tableWidget.item(selected_row, 1).text()
    SubType = obs.tableWidget.item(selected_row, 2).text()
    Early_Start = obs.tableWidget.item(selected_row, 3).text()
    Late_Start = obs.tableWidget.item(selected_row, 4).text()
    Duration = obs.tableWidget.item(selected_row, 5).text()
    Target_Name = obs.tableWidget.item(selected_row, 6).text()
    Right_Ascression = obs.tableWidget.item(selected_row, 7).text()
    V_Magnitude = obs.tableWidget.item(selected_row, 8).text()
    Target_Type = obs.tableWidget.item(selected_row, 9).text()
    Decination = obs.tableWidget.item(selected_row, 10).text()
    Other_Fluxes = obs.tableWidget.item(selected_row, 11).text()

    obs.comboBox.setCurrentText(Type)
    obs.comboBox_2.setCurrentText(SubType)
    obs.dateTimeEdit.setDateTime(QDateTime.fromString(Early_Start, "dd-MM-yyyy HH:mm"))
    obs.dateTimeEdit_2.setDateTime(QDateTime.fromString(Late_Start, "dd-MM-yyyy HH:mm"))
    obs.lineEdit_7.setText(Duration)
    obs.lineEdit_2.setText(Target_Name)
    obs.lineEdit_3.setText(Right_Ascression)
    obs.lineEdit_4.setText(V_Magnitude)
    obs.comboBox_3.setCurrentText(Target_Type)
    obs.lineEdit_5.setText(Decination)
    obs.lineEdit_6.setText(Other_Fluxes)


def getSelectedRowReq():
    return obs.tableWidget.currentRow()


def getSelectedRequest():
    return obs.tableWidget.item(getSelectedRowReq(), 0).text()


# проверка подтверждения удаления заявки
def deleteRequestCheck():
    def click(b):
        if b.text() == "OK":
            deleteReq()
    error = QMessageBox()
    error.setWindowTitle("Внимание!")
    error.setText("Вы уверены, что хотите удалить эту заявку?")
    error.setIcon(QMessageBox.Question)
    error.addButton("Да", QMessageBox.YesRole)
    error.addButton("Нет", QMessageBox.NoRole)
    error.buttonClicked.connect(click)
    error.exec_()


def deleteReq():
    deleteRequestCheck()
    try:
        id_delete = getSelectedRequest()
        helper_request.delete("DELETE FROM request WHERE id=" + id_delete)
        refresh_req()
        mainmenu_refresh()

    except:
        Exception


# проверка подтверждения обновления заявки
def updateRequestCheck():
    def click(b):
        if b.text() == "OK":
            updateReq()

    error = QMessageBox()
    error.setWindowTitle("Внимание!")
    error.setText("Вы уверены, что хотите обновить эту заявку?")
    error.setIcon(QMessageBox.Question)
    error.addButton("Да", QMessageBox.YesRole)
    error.addButton("Нет", QMessageBox.NoRole)
    error.buttonClicked.connect(click)
    error.exec_()


def updateReq():
    updateRequestCheck()
    try:
        id_update = getSelectedRequest()

        Type = obs.comboBox.currentText()
        SubType = obs.comboBox_2.currentText()
        Early_Start = obs.dateTimeEdit.dateTime().toString('dd-MM-yyyy HH:mm')
        Late_Start = obs.dateTimeEdit_2.dateTime().toString('dd-MM-yyyy HH:mm')
        Duration = obs.lineEdit_7.text()
        Target_Name = obs.lineEdit_2.text()
        Right_Ascression = obs.lineEdit_3.text()
        V_Magnitude = obs.lineEdit_4.text()
        Target_Type = obs.comboBox_3.currentText()
        Decination = obs.lineEdit_5.text()
        Other_Fluxes = obs.lineEdit_6.text()

        user = (
            Type, SubType, str(Early_Start), str(Late_Start), Duration, Target_Name, Right_Ascression, V_Magnitude,
            Target_Type,
            Decination, Other_Fluxes)
        helper_request.edit(
            "UPDATE request SET Type=?,SubType=?,Early_Start=?,Late_Start=?,Duration=?,Target_Name=?,Right_Ascression=?,V_Magnitude=?,Target_Type=?,Decination=?,Other_Fluxes=?WHERE id=" + id_update,
            user)
        refresh_req()
        mainmenu_refresh()
    except:
        Exception
    # obs.show()


# функции для открытия, закрытия определенных форм (для нажатий)

def show_message(title='', message=''):
    QMessageBox.information(None, title, message)


def close_form():
    sgn_on.close()
    dlg.close()


def show_sgn_on():
    sgn_on.show()


def show_main_menu():
    # проверка логина и пароля
    login = sgn_in.lineEdit.text()
    password = sgn_in.lineEdit_2.text()
    users = helper.select(f"SELECT id FROM userss WHERE login='{login}' AND password='{password}'")
    if len(users) != 0 or (login == admin_login and password == admin_password):
        main_menu.show()
        mainmenu_settings()
        if login == admin_login and password == admin_password:
            main_menu.actionAccounts.setEnabled(True)
            main_menu.actionAccounts.setVisible(True)
        sgn_in.close()
    else:
        sgn_in.label_3.setText("Неверный логин или пароль!")


# проверка на наличие заявок и запись их в дерево (QTreeWidget в mainmenu)
def mainmenu_settings():
    data = helper_request.select("SELECT Target_Name, Early_Start FROM request")
    for Target_Name, Early_Start in data:
        prop_name = Target_Name + " " + Early_Start
        employee_item = QTreeWidgetItem(main_menu.treeWidget.topLevelItem(0).child(0))
        employee_item.setText(0, prop_name)
        main_menu.treeWidget.topLevelItem(0).child(0).addChild(employee_item)


def mainmenu_refresh():
    for i in reversed(range((main_menu.treeWidget.topLevelItem(0).child(0).childCount()))):
        main_menu.treeWidget.topLevelItem(0).child(0).removeChild(
            main_menu.treeWidget.topLevelItem(0).child(0).child(i))
    mainmenu_settings()


def obs_form():
    obs.show()
    obs.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
    obs.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())


def obs_save():
    obs.close()


def obs_reset():
    obs.close()


def show_help():
    help_form.show()


def show_logs():
    logs.show()

def show_accounts():
    dlg.show()

def form_exit():
    main_menu.close()


# открываем главную форму
sgn_in.show()
# и непосредственно сами нажатия
# обработка формы входа
sgn_in.loginButton.clicked.connect(show_main_menu)
sgn_in.pushButton.clicked.connect(show_sgn_on)

# обработка формы регистрации
sgn_on.pushButton.clicked.connect(addUser)
sgn_on.pushButton_2.clicked.connect(close_form)
dlg.tableWidget.itemSelectionChanged.connect(selectionChanged)

# обработка основной формы
main_menu.pushButton.clicked.connect(obs_form)
main_menu.actionHelp.triggered.connect(show_help)
main_menu.actionLogs.triggered.connect(show_logs)
main_menu.actionExit.triggered.connect(form_exit)
main_menu.actionAccounts.triggered.connect(show_accounts)

# обработка формы редактирования заявки
obs.pushButton.clicked.connect(addRequest)
obs.tableWidget.itemSelectionChanged.connect(selectionChangedRequest)
obs.pushButton_4.clicked.connect(deleteReq)
obs.pushButton_5.clicked.connect(updateReq)

chng.pushButton_2.clicked.connect(deleteUser)
chng.pushButton.clicked.connect(updateUser)

# загрузка БД
loadData()
loadData_req()

app.exec()
