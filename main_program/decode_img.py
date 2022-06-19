# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decode_img.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Decode_img_Dialog(object):
    def setupUi(self, Decode_img_Dialog):
        Decode_img_Dialog.setObjectName("Decode_img_Dialog")
        Decode_img_Dialog.resize(825, 370)
        Decode_img_Dialog.setMinimumSize(QtCore.QSize(825, 370))
        Decode_img_Dialog.setMaximumSize(QtCore.QSize(825, 370))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/pictures.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Decode_img_Dialog.setWindowIcon(icon)
        Decode_img_Dialog.setStyleSheet("background-image: url(:/background/icons/background.png);")
        self.label = QtWidgets.QLabel(Decode_img_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 180, 591, 61))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Decode_img_Dialog)
        self.label_3.setGeometry(QtCore.QRect(530, -5, 271, 41))
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_accept_pass_decode = QtWidgets.QPushButton(Decode_img_Dialog)
        self.pushButton_accept_pass_decode.setGeometry(QtCore.QRect(360, 240, 111, 31))
        self.pushButton_accept_pass_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_accept_pass_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_accept_pass_decode.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_accept_pass_decode.setObjectName("pushButton_accept_pass_decode")
        self.pushButton_open_decode = QtWidgets.QPushButton(Decode_img_Dialog)
        self.pushButton_open_decode.setGeometry(QtCore.QRect(390, 52, 81, 31))
        self.pushButton_open_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_open_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_open_decode.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_open_decode.setObjectName("pushButton_open_decode")
        self.label_4 = QtWidgets.QLabel(Decode_img_Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 451, 41))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_sys_messages_decode = QtWidgets.QTextEdit(Decode_img_Dialog)
        self.lineEdit_sys_messages_decode.setGeometry(QtCore.QRect(530, 30, 281, 71))
        self.lineEdit_sys_messages_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_sys_messages_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit_sys_messages_decode.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_sys_messages_decode.setObjectName("lineEdit_sys_messages_decode")
        self.plainTextEdit_for_pass_decode = QtWidgets.QLineEdit(Decode_img_Dialog)
        self.plainTextEdit_for_pass_decode.setGeometry(QtCore.QRect(20, 240, 331, 31))
        self.plainTextEdit_for_pass_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_for_pass_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.plainTextEdit_for_pass_decode.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.plainTextEdit_for_pass_decode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.plainTextEdit_for_pass_decode.setObjectName("plainTextEdit_for_pass_decode")
        self.lineEdit_path = QtWidgets.QLineEdit(Decode_img_Dialog)
        self.lineEdit_path.setGeometry(QtCore.QRect(20, 50, 361, 31))
        self.lineEdit_path.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_path.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit_path.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_path.setObjectName("lineEdit_path")

        self.retranslateUi(Decode_img_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Decode_img_Dialog)

    def retranslateUi(self, Decode_img_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Decode_img_Dialog.setWindowTitle(_translate("Decode_img_Dialog", "Декодер Изображения"))
        self.label.setText(_translate("Decode_img_Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Введите пароль для дешифрования:</span></p></body></html>"))
        self.label_3.setText(_translate("Decode_img_Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">System Messages:</span></p></body></html>"))
        self.pushButton_accept_pass_decode.setText(_translate("Decode_img_Dialog", "Подтвердить"))
        self.pushButton_open_decode.setText(_translate("Decode_img_Dialog", "Открыть"))
        self.label_4.setText(_translate("Decode_img_Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Открыть txt файл изображения:</span></p></body></html>"))
import iconscryptor_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Decode_img_Dialog = QtWidgets.QDialog()
    ui = Ui_Decode_img_Dialog()
    ui.setupUi(Decode_img_Dialog)
    Decode_img_Dialog.show()
    sys.exit(app.exec_())
