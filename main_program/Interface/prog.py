# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWnidow(object):
    def setupUi(self, MainWnidow):
        MainWnidow.setObjectName("MainWnidow")
        MainWnidow.resize(1110, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWnidow.sizePolicy().hasHeightForWidth())
        MainWnidow.setSizePolicy(sizePolicy)
        MainWnidow.setMinimumSize(QtCore.QSize(1110, 720))
        MainWnidow.setMaximumSize(QtCore.QSize(1110, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWnidow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWnidow)
        self.centralwidget.setStyleSheet("background-image: url(:/background/icons/background.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 481, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(880, 0, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_sys_mes = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_sys_mes.setGeometry(QtCore.QRect(881, 33, 221, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_sys_mes.sizePolicy().hasHeightForWidth())
        self.lineEdit_sys_mes.setSizePolicy(sizePolicy)
        self.lineEdit_sys_mes.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_sys_mes.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit_sys_mes.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.lineEdit_sys_mes.setObjectName("lineEdit_sys_mes")
        self.pushButton_enter_mail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enter_mail.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.pushButton_enter_mail.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_enter_mail.setObjectName("pushButton_enter_mail")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(990, 120, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_date = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_date.setGeometry(QtCore.QRect(1060, 150, 41, 21))
        self.pushButton_date.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_date.setObjectName("pushButton_date")
        MainWnidow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWnidow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        self.menu_menu = QtWidgets.QMenu(self.menubar)
        self.menu_menu.setObjectName("menu_menu")
        self.menu_Gallery = QtWidgets.QMenu(self.menu_menu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_Gallery.setIcon(icon1)
        self.menu_Gallery.setObjectName("menu_Gallery")
        self.menuALL_SAFE = QtWidgets.QMenu(self.menu_menu)
        self.menuALL_SAFE.setIcon(icon1)
        self.menuALL_SAFE.setObjectName("menuALL_SAFE")
        self.menu_encode = QtWidgets.QMenu(self.menubar)
        self.menu_encode.setObjectName("menu_encode")
        self.menu_decode = QtWidgets.QMenu(self.menubar)
        self.menu_decode.setObjectName("menu_decode")
        self.menu_sending = QtWidgets.QMenu(self.menubar)
        self.menu_sending.setObjectName("menu_sending")
        MainWnidow.setMenuBar(self.menubar)
        self.action_exit = QtWidgets.QAction(MainWnidow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon2)
        self.action_exit.setObjectName("action_exit")
        self.action_en_sms = QtWidgets.QAction(MainWnidow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/sms.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_en_sms.setIcon(icon3)
        self.action_en_sms.setObjectName("action_en_sms")
        self.action_en_img = QtWidgets.QAction(MainWnidow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/pictures.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_en_img.setIcon(icon4)
        self.action_en_img.setObjectName("action_en_img")
        self.action_de_sms = QtWidgets.QAction(MainWnidow)
        self.action_de_sms.setIcon(icon3)
        self.action_de_sms.setObjectName("action_de_sms")
        self.action_de_img = QtWidgets.QAction(MainWnidow)
        self.action_de_img.setIcon(icon4)
        self.action_de_img.setObjectName("action_de_img")
        self.action_send = QtWidgets.QAction(MainWnidow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_send.setIcon(icon5)
        self.action_send.setObjectName("action_send")
        self.action_send_img = QtWidgets.QAction(MainWnidow)
        self.action_send_img.setIcon(icon5)
        self.action_send_img.setObjectName("action_send_img")
        self.action_send_both = QtWidgets.QAction(MainWnidow)
        self.action_send_both.setIcon(icon5)
        self.action_send_both.setObjectName("action_send_both")
        self.action_sobr = QtWidgets.QAction(MainWnidow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_sobr.setIcon(icon6)
        self.action_sobr.setObjectName("action_sobr")
        self.action_upload = QtWidgets.QAction(MainWnidow)
        self.action_upload.setIcon(icon6)
        self.action_upload.setObjectName("action_upload")
        self.action_4 = QtWidgets.QAction(MainWnidow)
        self.action_4.setObjectName("action_4")
        self.action_open = QtWidgets.QAction(MainWnidow)
        self.action_open.setIcon(icon6)
        self.action_open.setObjectName("action_open")
        self.action_clean = QtWidgets.QAction(MainWnidow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_clean.setIcon(icon7)
        self.action_clean.setObjectName("action_clean")
        self.action_delete_txt = QtWidgets.QAction(MainWnidow)
        self.action_delete_txt.setIcon(icon7)
        self.action_delete_txt.setObjectName("action_delete_txt")
        self.action_ALL_SAFE = QtWidgets.QAction(MainWnidow)
        self.action_ALL_SAFE.setIcon(icon6)
        self.action_ALL_SAFE.setObjectName("action_ALL_SAFE")
        self.action_settings = QtWidgets.QAction(MainWnidow)
        self.action_settings.setIcon(icon1)
        self.action_settings.setObjectName("action_settings")
        self.action_en_video = QtWidgets.QAction(MainWnidow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/clapperboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_en_video.setIcon(icon8)
        self.action_en_video.setObjectName("action_en_video")
        self.action_de_video = QtWidgets.QAction(MainWnidow)
        self.action_de_video.setIcon(icon8)
        self.action_de_video.setObjectName("action_de_video")
        self.action_clear_logs = QtWidgets.QAction(MainWnidow)
        self.action_clear_logs.setIcon(icon7)
        self.action_clear_logs.setObjectName("action_clear_logs")
        self.menu_Gallery.addAction(self.action_open)
        self.menu_Gallery.addAction(self.action_clean)
        self.menuALL_SAFE.addAction(self.action_ALL_SAFE)
        self.menuALL_SAFE.addAction(self.action_delete_txt)
        self.menu_menu.addAction(self.menu_Gallery.menuAction())
        self.menu_menu.addAction(self.menuALL_SAFE.menuAction())
        self.menu_menu.addAction(self.action_settings)
        self.menu_menu.addAction(self.action_clear_logs)
        self.menu_menu.addSeparator()
        self.menu_menu.addAction(self.action_exit)
        self.menu_menu.addSeparator()
        self.menu_encode.addAction(self.action_en_sms)
        self.menu_encode.addAction(self.action_en_img)
        self.menu_encode.addAction(self.action_en_video)
        self.menu_decode.addAction(self.action_de_sms)
        self.menu_decode.addAction(self.action_de_img)
        self.menu_decode.addAction(self.action_de_video)
        self.menu_sending.addAction(self.action_send)
        self.menubar.addAction(self.menu_menu.menuAction())
        self.menubar.addAction(self.menu_encode.menuAction())
        self.menubar.addAction(self.menu_decode.menuAction())
        self.menubar.addAction(self.menu_sending.menuAction())

        self.retranslateUi(MainWnidow)
        QtCore.QMetaObject.connectSlotsByName(MainWnidow)

    def retranslateUi(self, MainWnidow):
        _translate = QtCore.QCoreApplication.translate
        MainWnidow.setWindowTitle(_translate("MainWnidow", "Cryptor 3.0"))
        self.label_2.setText(_translate("MainWnidow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">???????????????????????????? ???????? ?? ?????????????????? ???????? ??????????:</span></p></body></html>"))
        self.label.setText(_translate("MainWnidow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">System Messages:</span></p></body></html>"))
        self.pushButton_enter_mail.setText(_translate("MainWnidow", "??????????"))
        self.pushButton_date.setText(_translate("MainWnidow", "Ok"))
        self.menu_menu.setTitle(_translate("MainWnidow", "????????"))
        self.menu_Gallery.setTitle(_translate("MainWnidow", "??????????????"))
        self.menuALL_SAFE.setTitle(_translate("MainWnidow", "ALL_SAFE"))
        self.menu_encode.setTitle(_translate("MainWnidow", "??????????"))
        self.menu_decode.setTitle(_translate("MainWnidow", "??????????????"))
        self.menu_sending.setTitle(_translate("MainWnidow", "????????????????"))
        self.action_exit.setText(_translate("MainWnidow", "?????????? "))
        self.action_en_sms.setText(_translate("MainWnidow", "??????????????????"))
        self.action_en_img.setText(_translate("MainWnidow", "????????????????"))
        self.action_de_sms.setText(_translate("MainWnidow", "??????????????????"))
        self.action_de_img.setText(_translate("MainWnidow", "????????????????"))
        self.action_send.setText(_translate("MainWnidow", "?????????????????? ???????? (??)"))
        self.action_send_img.setText(_translate("MainWnidow", "????????????????"))
        self.action_send_both.setText(_translate("MainWnidow", "?????? ??????????"))
        self.action_sobr.setText(_translate("MainWnidow", "?????????????????? ????????"))
        self.action_upload.setText(_translate("MainWnidow", "Upload Folder"))
        self.action_4.setText(_translate("MainWnidow", "?????????? ?? ????????????????????"))
        self.action_open.setText(_translate("MainWnidow", "?????????????? ??????????????"))
        self.action_clean.setText(_translate("MainWnidow", "???????????????? ??????????????"))
        self.action_delete_txt.setText(_translate("MainWnidow", "?????????????? ?????????????????? ??????????"))
        self.action_ALL_SAFE.setText(_translate("MainWnidow", "?????????????? ??????????"))
        self.action_settings.setText(_translate("MainWnidow", "??????????????????"))
        self.action_en_video.setText(_translate("MainWnidow", "??????????"))
        self.action_de_video.setText(_translate("MainWnidow", "??????????"))
        self.action_clear_logs.setText(_translate("MainWnidow", "???????????????? ????????"))
import iconscryptor_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWnidow = QtWidgets.QMainWindow()
    ui = Ui_MainWnidow()
    ui.setupUi(MainWnidow)
    MainWnidow.show()
    sys.exit(app.exec_())
