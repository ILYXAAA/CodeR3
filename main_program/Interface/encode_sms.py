# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encode_sms.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Encode_sms_Dialog(object):
    def setupUi(self, Encode_sms_Dialog):
        Encode_sms_Dialog.setObjectName("Encode_sms_Dialog")
        Encode_sms_Dialog.resize(851, 577)
        Encode_sms_Dialog.setMinimumSize(QtCore.QSize(851, 577))
        Encode_sms_Dialog.setMaximumSize(QtCore.QSize(851, 577))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/sms.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Encode_sms_Dialog.setWindowIcon(icon)
        Encode_sms_Dialog.setStyleSheet("background-image: url(:/background/icons/background.png);")
        self.plainTextEdit_for_mess_encode = QtWidgets.QPlainTextEdit(Encode_sms_Dialog)
        self.plainTextEdit_for_mess_encode.setGeometry(QtCore.QRect(20, 160, 331, 371))
        self.plainTextEdit_for_mess_encode.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_for_mess_encode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.plainTextEdit_for_mess_encode.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.plainTextEdit_for_mess_encode.setObjectName("plainTextEdit_for_mess_encode")
        self.label = QtWidgets.QLabel(Encode_sms_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 521, 61))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Encode_sms_Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 541, 51))
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Encode_sms_Dialog)
        self.label_3.setGeometry(QtCore.QRect(570, 0, 271, 31))
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton_ok_encode = QtWidgets.QPushButton(Encode_sms_Dialog)
        self.pushButton_ok_encode.setGeometry(QtCore.QRect(20, 540, 75, 23))
        self.pushButton_ok_encode.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_ok_encode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_ok_encode.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_ok_encode.setObjectName("pushButton_ok_encode")
        self.lineEdit_sys_messages_encode = QtWidgets.QTextEdit(Encode_sms_Dialog)
        self.lineEdit_sys_messages_encode.setGeometry(QtCore.QRect(570, 30, 271, 71))
        self.lineEdit_sys_messages_encode.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_sys_messages_encode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit_sys_messages_encode.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_sys_messages_encode.setObjectName("lineEdit_sys_messages_encode")
        self.plainTextEdit_for_pass_encode = QtWidgets.QLineEdit(Encode_sms_Dialog)
        self.plainTextEdit_for_pass_encode.setGeometry(QtCore.QRect(20, 60, 331, 31))
        self.plainTextEdit_for_pass_encode.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_for_pass_encode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.plainTextEdit_for_pass_encode.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.plainTextEdit_for_pass_encode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.plainTextEdit_for_pass_encode.setObjectName("plainTextEdit_for_pass_encode")
        self.label_2.raise_()
        self.plainTextEdit_for_mess_encode.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.pushButton_ok_encode.raise_()
        self.lineEdit_sys_messages_encode.raise_()
        self.plainTextEdit_for_pass_encode.raise_()

        self.retranslateUi(Encode_sms_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Encode_sms_Dialog)

    def retranslateUi(self, Encode_sms_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Encode_sms_Dialog.setWindowTitle(_translate("Encode_sms_Dialog", "?????????? ??????????????????"))
        self.label.setText(_translate("Encode_sms_Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">?????????????? ???????????? ?????? ????????????????????:</span></p></body></html>"))
        self.label_2.setText(_translate("Encode_sms_Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">?????????????? ?????????????????? ?????? ????????????????:</span></p></body></html>"))
        self.label_3.setText(_translate("Encode_sms_Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">System Messages:</span></p></body></html>"))
        self.pushButton_ok_encode.setText(_translate("Encode_sms_Dialog", "????"))
import iconscryptor_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Encode_sms_Dialog = QtWidgets.QDialog()
    ui = Ui_Encode_sms_Dialog()
    ui.setupUi(Encode_sms_Dialog)
    Encode_sms_Dialog.show()
    sys.exit(app.exec_())
