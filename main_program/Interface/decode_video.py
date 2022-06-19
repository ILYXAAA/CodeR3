# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decode_video.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_decode_video(object):
    def setupUi(self, Dialog_decode_video):
        Dialog_decode_video.setObjectName("Dialog_decode_video")
        Dialog_decode_video.resize(825, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_decode_video.setWindowIcon(icon)
        Dialog_decode_video.setStyleSheet("background-image: url(:/background/icons/background.png);")
        self.plainTextEdit_for_pass_decode = QtWidgets.QLineEdit(Dialog_decode_video)
        self.plainTextEdit_for_pass_decode.setGeometry(QtCore.QRect(10, 250, 331, 31))
        self.plainTextEdit_for_pass_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit_for_pass_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.plainTextEdit_for_pass_decode.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.plainTextEdit_for_pass_decode.setEchoMode(QtWidgets.QLineEdit.Password)
        self.plainTextEdit_for_pass_decode.setObjectName("plainTextEdit_for_pass_decode")
        self.lineEdit_path = QtWidgets.QLineEdit(Dialog_decode_video)
        self.lineEdit_path.setGeometry(QtCore.QRect(10, 60, 361, 31))
        self.lineEdit_path.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_path.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit_path.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_open_decode = QtWidgets.QPushButton(Dialog_decode_video)
        self.pushButton_open_decode.setGeometry(QtCore.QRect(380, 62, 81, 31))
        self.pushButton_open_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_open_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_open_decode.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_open_decode.setObjectName("pushButton_open_decode")
        self.pushButton_accept_pass_decode = QtWidgets.QPushButton(Dialog_decode_video)
        self.pushButton_accept_pass_decode.setGeometry(QtCore.QRect(350, 250, 111, 31))
        self.pushButton_accept_pass_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_accept_pass_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.pushButton_accept_pass_decode.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_accept_pass_decode.setObjectName("pushButton_accept_pass_decode")
        self.label = QtWidgets.QLabel(Dialog_decode_video)
        self.label.setGeometry(QtCore.QRect(10, 190, 591, 61))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit_sys_messages_decode = QtWidgets.QTextEdit(Dialog_decode_video)
        self.lineEdit_sys_messages_decode.setGeometry(QtCore.QRect(520, 40, 281, 71))
        self.lineEdit_sys_messages_decode.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_sys_messages_decode.setMaximumSize(QtCore.QSize(1000, 1000))
        self.lineEdit_sys_messages_decode.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_sys_messages_decode.setObjectName("lineEdit_sys_messages_decode")
        self.label_3 = QtWidgets.QLabel(Dialog_decode_video)
        self.label_3.setGeometry(QtCore.QRect(520, 5, 271, 41))
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_decode_video)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 451, 41))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(1000, 1000))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit_path.raise_()
        self.pushButton_open_decode.raise_()
        self.plainTextEdit_for_pass_decode.raise_()
        self.pushButton_accept_pass_decode.raise_()
        self.lineEdit_sys_messages_decode.raise_()

        self.retranslateUi(Dialog_decode_video)
        QtCore.QMetaObject.connectSlotsByName(Dialog_decode_video)

    def retranslateUi(self, Dialog_decode_video):
        _translate = QtCore.QCoreApplication.translate
        Dialog_decode_video.setWindowTitle(_translate("Dialog_decode_video", "Декодер Видео"))
        self.pushButton_open_decode.setText(_translate("Dialog_decode_video", "Открыть"))
        self.pushButton_accept_pass_decode.setText(_translate("Dialog_decode_video", "Подтвердить"))
        self.label.setText(_translate("Dialog_decode_video", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Введите пароль для дешифрования:</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog_decode_video", "<html><head/><body><p><span style=\" font-size:10pt;\">System Messages:</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog_decode_video", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Открыть txt файл видео:</span></p></body></html>"))
import iconscryptor_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_decode_video = QtWidgets.QDialog()
    ui = Ui_Dialog_decode_video()
    ui.setupUi(Dialog_decode_video)
    Dialog_decode_video.show()
    sys.exit(app.exec_())