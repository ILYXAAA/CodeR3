# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QDialog
import time
import pyperclip
import keyboard
import sys
sys.path.append('Interface/')
from prog import *
import random
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QProgressBar, QPushButton
from PyQt5.QtCore import Qt
from encode_img import *
from encode_sms import *
from decode_sms import *
from decode_img import *
from save_img import *
from send_sms import *
from Enter import *
from settings import *
from encode_video import *
from decode_video import *
import datetime
import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from platform import python_version
import shutil
import os.path
from pswd import *
now = datetime.datetime.now()
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # font = QFont()
        # font.setPixelSize(50)
        self.ui = Ui_MainWnidow()
        # font.setStyleHint(QFont.TypeWriter)

        self.ui.setupUi(self)
        self.Start_up()
        self.check()
        self.ui.action_exit.triggered.connect(self.exit_prog)

        self.ui.action_open.triggered.connect(self.gallery_folder)
        self.ui.action_clean.triggered.connect(self.clean_gallery)
        self.ui.lineEdit_sys_mes.setReadOnly(True)
        self.ui.action_en_img.triggered.connect(self.encode_img)
        self.ui.action_en_sms.triggered.connect(self.encode_sms)
        self.ui.action_de_sms.triggered.connect(self.decode_sms)
        self.ui.action_de_img.triggered.connect(self.decode_image)
        self.ui.action_send.triggered.connect(self.sending)
        self.ui.action_ALL_SAFE.triggered.connect(self.ALL_SAFE)
        self.ui.action_delete_txt.triggered.connect(self.delete_t)
        self.ui.action_settings.triggered.connect(self.settings)
        self.ui.action_en_video.triggered.connect(self.en_vid)
        self.ui.action_de_video.triggered.connect(self.de_vid)
        self.ui.action_clear_logs.triggered.connect(self.clear_logs)
        self.ui.pushButton_enter_mail.clicked.connect(self.enter_mail)
        self.ui.pushButton_date.clicked.connect(self.set_date)

        global propysk
        propysk = 0

        # Encode image Dialog
        global Encode_img_Dialog
        Encode_img_Dialog = QtWidgets.QDialog()
        self.enimg = Ui_Encode_img_Dialog()
        self.enimg.setupUi(Encode_img_Dialog)
        self.enimg.lineEdit_sys_messages_decode.setReadOnly(True)
        self.enimg.lineEdit_path.setReadOnly(True)
        self.enimg.pushButton_accept_pass_decode.clicked.connect(self.encode_image)
        self.enimg.pushButton_open_decode.clicked.connect(self.browse_file_image)

        # Encode sms Dialog
        global Encode_sms_Dialog
        Encode_sms_Dialog = QtWidgets.QDialog()
        self.ensms = Ui_Encode_sms_Dialog()
        self.ensms.setupUi(Encode_sms_Dialog)
        self.ensms.lineEdit_sys_messages_encode.setReadOnly(True)
        self.ensms.pushButton_ok_encode.clicked.connect(self.encrypt_sms)

        # Decode sms Dialog
        global Encode_Dialog
        Encode_Dialog = QtWidgets.QDialog()
        self.desms = Ui_Encode_Dialog()
        self.desms.setupUi(Encode_Dialog)
        self.desms.lineEdit_sys_messages_decode.setReadOnly(True)
        self.desms.plainTextEdit_for_mess_decode.setReadOnly(True)
        self.desms.lineEdit_path.setReadOnly(True)
        self.desms.pushButton_accept_pass_decode.clicked.connect(self.decrypt)
        self.desms.pushButton_open_decode.clicked.connect(self.browse_file_txt)

        # Decode image Dialog
        global Decode_img_Dialog
        Decode_img_Dialog = QtWidgets.QDialog()
        self.deimg = Ui_Decode_img_Dialog()
        self.deimg.setupUi(Decode_img_Dialog)
        self.deimg.lineEdit_sys_messages_decode.setReadOnly(True)
        self.deimg.pushButton_open_decode.clicked.connect(self.browse_file_img)
        self.deimg.pushButton_accept_pass_decode.clicked.connect(self.decrypt_img)

        # Save image Dialog
        global Dialog_save
        Dialog_save = QtWidgets.QDialog()
        self.save = Ui_Dialog_save()
        self.save.setupUi(Dialog_save)
        self.save.pushButton_save_no.clicked.connect(self.save_no)
        self.save.pushButton_save_yes.clicked.connect(self.save_yes)

        # Send Dialog
        global Dialog_send
        Dialog_send = QtWidgets.QDialog()
        self.sen = Ui_Dialog_send()
        self.sen.setupUi(Dialog_send)
        self.sen.lineEdit_system_message_send.setReadOnly(True)
        self.sen.pushButton_send.clicked.connect(self.box_checker)
        self.sen.pushButton_auto_fill.clicked.connect(self.auto_fill)

        # Settings Dialog
        global Dialog_settings
        Dialog_settings = QtWidgets.QDialog()
        self.st = Ui_Dialog_settings()
        self.st.setupUi(Dialog_settings)
        self.st.pushButton.clicked.connect(self.change_pass)
        self.st.pushButton_2.clicked.connect(self.delete_pass)
        self.st.pushButton_show_iter.clicked.connect(self.show_iter)
        self.st.lineEdit_sys_mes.setReadOnly(True)
        self.st.lineEdit_3.setReadOnly(True)
        self.st.pushButton_generate.clicked.connect(self.generate_iter)
        self.st.pushButton_write.clicked.connect(self.write_iter)
        self.st.pushButton_write_mail.clicked.connect(self.rem_mail)
        self.st.pushButton_write_to.clicked.connect(self.rem_to)
        self.st.pushButton_delete_autofill.clicked.connect(self.delete_auto_fill)
        self.st.pushButton_show_email.clicked.connect(self.show_mail)
        self.st.pushButton_speed_2.clicked.connect(self.change_speed2)
        self.st.pushButton_speed_3.clicked.connect(self.change_speed3)
        self.st.pushButton_speed_4.clicked.connect(self.change_speed4)
        self.st.pushButton_speed_5.clicked.connect(self.change_speed5)
        self.st.pushButton_speed_6.clicked.connect(self.change_speed6)

        if os.path.exists('speed.txt'):
            with open('speed.txt', 'r') as file:
                speed = file.readlines()
                speed = speed[0]
                self.st.lineEdit_3.setText(speed)
        else:
            with open('speed.txt', 'w') as file:
                file.write(str(5))
                self.st.lineEdit_3.setText(str(5))
                self.msg_warn("У вас не была установлена мощность ПК. Мы установили её на самую низкую по умолчанию" + '\n' + "Если хотите изменить параметры мощности, зайдите в настройки.")


        # Encode Video Dialog
        global Dialog_encode_video
        Dialog_encode_video = QtWidgets.QDialog()
        self.envid = Ui_Dialog_encode_video()
        self.envid.setupUi(Dialog_encode_video)
        self.envid.lineEdit_sys_messages_decode.setReadOnly(True)
        self.envid.lineEdit_path.setReadOnly(True)
        self.envid.pushButton_open_decode.clicked.connect(self.browse_file_video)
        self.envid.pushButton_accept_pass_decode.clicked.connect(self.encode_video)

        # Decode Video Dialog
        global Dialog_decode_video
        Dialog_decode_video = QtWidgets.QDialog()
        self.devid = Ui_Dialog_decode_video()
        self.devid.setupUi(Dialog_decode_video)
        self.devid.lineEdit_sys_messages_decode.setReadOnly(True)
        self.devid.lineEdit_path.setReadOnly(True)
        self.devid.pushButton_open_decode.clicked.connect(self.browse_txt_v)
        self.devid.pushButton_accept_pass_decode.clicked.connect(self.dec_vid)

    def set_date(self):
        nowa = self.ui.dateEdit.date().toString('dd-MM')
        global now_day 
        now_day = nowa[0:2]
        global now_month
        now_month = nowa[3:5]
        self.msg_info("Дата установлена!")
        

    def clear_crypto(self):
        with open(papath + 'crypto.key', 'wb') as key_file:
            key_file.write(b"")

    def change_speed2(self):
        speed = 2
        speed = str(speed)
        with open('speed.txt', 'w') as file:
            file.write(speed)
        self.msg_info("Скорость установлена")
        self.st.lineEdit_3.setText(speed)
    def change_speed3(self):
        speed = 3
        speed = str(speed)
        with open('speed.txt', 'w') as file:
            file.write(str(speed))
        self.msg_info("Скорость установлена")
        self.st.lineEdit_3.setText(speed)
    def change_speed4(self):
        speed = 4
        speed = str(speed)
        with open('speed.txt', 'w') as file:
            file.write(str(speed))
        self.msg_info("Скорость установлена")
        self.st.lineEdit_3.setText(speed)
    def change_speed5(self):
        speed = 5
        speed = str(speed)
        with open('speed.txt', 'w') as file:
            file.write(str(speed))
        self.msg_info("Скорость установлена")
        self.st.lineEdit_3.setText(speed)
    def change_speed6(self):
        speed = 6
        speed = str(speed)
        with open('speed.txt', 'w') as file:
            file.write(str(speed))
        self.msg_info("Скорость установлена")
        self.st.lineEdit_3.setText(speed)

    def enter_mail(self):
        try:
            if os.path.exists('email_login.txt') == True:
                with open('email_login.txt', 'r') as file:
                    data = file.readlines()
                    enmail = data[0]
                    enpas = data[1]
                password_mail = b"password_for_emailcry_pt_Or"
                salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt,
                                 iterations=100000,
                                 )
                key = base64.urlsafe_b64encode(kdf.derive(password_mail))
                f = Fernet(key)
                text = (f.decrypt(enmail.encode())).decode()
                text2 = (f.decrypt(enpas.encode())).decode()

                try:
                    with open('speed.txt', 'r') as file:
                        speed = file.readlines()
                    speed = speed[0]
                    speed = int(speed)
                except Exception:
                    self.msg_crit("Что-то пошло не так. Проверьте установленную мощность ПК в настройках.")

                pyperclip.copy('https://www.google.com/')
                keyboard.send("windows+r")
                time.sleep(speed)
                keyboard.send("control+v")
                keyboard.send("enter")
                time.sleep(speed)
                keyboard.send("control+shift+n")
                time.sleep(speed)
                pyperclip.copy(
                    'https://accounts.google.com/ServiceLogin?service=mail&ss=1&scc=1&ltmpl=ecobx&nui=5&btmpl=mobile&emr=1')
                keyboard.send("control+v")
                keyboard.send("enter")
                time.sleep(speed)
                pyperclip.copy(str(text))
                keyboard.send("control+v")
                keyboard.send("enter")
                time.sleep(speed)
                pyperclip.copy(str(text2))
                keyboard.send("control+v")
                keyboard.send("enter")

            elif os.path.exists('email_to_login.txt') == False and os.path.exists('email_login.txt') == False:
                self.msg_warn("Данных для входа в почту не существует")
                self.st.lineEdit_sys_mes.clear()
                Dialog_send.activateWindow()

        except Exception:
            self.msg_crit("Что-то пошло не так. Попробуйте удалить данные для автозаполнения и записать их заново.")

    def show_mail(self):
        try:
            a=0
            if os.path.exists('email_login.txt') == True:
                with open('email_login.txt', 'r') as file:
                    data = file.readlines()
                    enmail = data[0]
                    enpas = data[1]
                password_mail = b"password_for_emailcry_pt_Or"
                salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt,
                                 iterations=100000,
                                 )
                key = base64.urlsafe_b64encode(kdf.derive(password_mail))
                f = Fernet(key)
                text = f.decrypt(enmail.encode())
                text2 = f.decrypt(enpas.encode())
                a += 1
            if os.path.exists('email_to_login.txt') == True:
                with open('email_to_login.txt', 'r') as file:
                    data = file.readlines()
                    ento = data[0]
                password_mail = b"password_for_emailcry_pt_Or"
                salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt,
                                 iterations=100000,
                                 )
                key = base64.urlsafe_b64encode(kdf.derive(password_mail))
                f = Fernet(key)
                text3 = f.decrypt(ento.encode())
                a += 2

            if a ==1:
                self.st.lineEdit_sys_mes.setText("Ваша почта: " + str(text.decode()) + '\n' + "Пароль от вашей почты: " + str(text2.decode()))
            elif a == 2:
                self.st.lineEdit_sys_mes.setText("Почта получателя: " + str(text3.decode()))
            elif a == 3:
                self.st.lineEdit_sys_mes.setText("Ваша почта: " + str(text.decode()) + '\n' + "Пароль от вашей почты: " + str(text2.decode()) + '\n' + "Почта получателя: " + str(text3.decode()))

            elif os.path.exists('email_to_login.txt') == False and os.path.exists('email_login.txt') == False:
                self.msg_warn("Данные для автозаполнения не записаны в программу")
                self.st.lineEdit_sys_mes.clear()
                Dialog_send.activateWindow()
                a = 0


        except Exception:
            self.msg_crit("Что-то пошло не так. Попробуйте удалить данные для автозаполнения и записать их заново.")

    def delete_auto_fill(self):
        if os.path.exists('email_login.txt') == True:
            os.remove('email_login.txt')
        if os.path.exists('email_to_login.txt') == True:
            os.remove('email_to_login.txt')
        self.msg_info("Данные автозаполнения удалены")
        self.st.lineEdit_sys_mes.clear()

    def rem_mail(self):
        if len(self.st.lineEdit_from.text()) == 0 and len(self.st.lineEdit_from_pass.text()) == 0:
            self.msg_crit("Вы ничего не ввели")
        elif len(self.st.lineEdit_from.text()) == 0:
            self.msg_crit("Вы не ввели адрес своей почты")
        elif len(self.st.lineEdit_from_pass.text()) == 0:
            self.msg_crit("Вы не ввели пароль от своей почты")
        elif len(self.st.lineEdit_from.text()) != 0 and len(self.st.lineEdit_from_pass.text()) != 0:
            try:
                TIME_LIMIT = 100
                count = 0
                self.st.progress = QProgressBar(self)
                self.st.progress.setWindowTitle('Подождите..')
                self.st.progress.setGeometry(0, 0, 300, 25)
                self.st.progress.setMaximum(100)
                self.st.progress.show()
                mail_sender = self.st.lineEdit_from.text()

                mail_receiver = 'for.testing.service.cryptor@gmail.com'
                username = self.st.lineEdit_from.text()
                password = self.st.lineEdit_from_pass.text()

                count +=25
                self.st.progress.setValue(count)

                server = smtplib.SMTP(self.smtp_checker(mail_sender))

                subject = u'Тестовый email от '
                body = u'Отправка тестового письма'
                msg = MIMEText(body, 'plain', 'utf-8')
                msg['Subject'] = Header(subject, 'utf-8')

                count += 25
                self.st.progress.setValue(count)

                server.starttls()
                server.ehlo()
                server.login(username, password)

                count += 25
                self.st.progress.setValue(count)

                server.sendmail(mail_sender, mail_receiver, msg.as_string())
                server.quit()

                count += 25
                self.st.progress.setValue(count)
                self.st.progress.close()
                # Шифрование логина и пароля от почты
                password_mail = b"password_for_emailcry_pt_Or"
                salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt,
                                 iterations=100000,
                                 )
                key = base64.urlsafe_b64encode(kdf.derive(password_mail))
                f = Fernet(key)
                en_mail = f.encrypt(mail_sender.encode())
                en_pas = f.encrypt(password.encode())
                with open("email_login.txt", 'w') as file:
                    file.write(str(en_mail.decode()))
                    file.write('\n')
                    file.write(str(en_pas.decode()))
                self.st.lineEdit_from_pass.clear()
                self.st.lineEdit_from.clear()
                self.msg_info("Ваша почта успешно записана в автозаполнение")

            except Exception:
                self.msg_crit("Что-то пошло не так. Проверьте правильность введённых данных")
                # Dialog_settings.activateWindow()

    def rem_to(self):
        if len(self.st.lineEdit_to.text()) == 0:
            self.msg_crit("Вы ничего не ввели")
        else:
            password_mail = b"password_for_emailcry_pt_Or"
            salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                             length=32,
                             salt=salt,
                             iterations=100000,
                             )
            key = base64.urlsafe_b64encode(kdf.derive(password_mail))
            f = Fernet(key)
            en_to = f.encrypt(self.st.lineEdit_to.text().encode())
            with open("email_to_login.txt", 'w') as file:
                file.write(str(en_to.decode()))
            self.msg_info("Почта получателя записана. На всякий случай перепроверьте правильность введённых данных.")
            self.st.lineEdit_to.clear()

    def auto_fill(self):
        try:
            if os.path.exists('email_login.txt') == True:
                with open('email_login.txt', 'r') as file:
                    data = file.readlines()
                    enmail = data[0]
                    enpas = data[1]
                password_mail = b"password_for_emailcry_pt_Or"
                salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt,
                                 iterations=100000,
                                 )
                key = base64.urlsafe_b64encode(kdf.derive(password_mail))
                f = Fernet(key)
                text = f.decrypt(enmail.encode())
                self.sen.plainTextEdit_send_from.setPlainText(str(text.decode()))
                text = f.decrypt(enpas.encode())
                self.sen.plainTextEdit_send_pass.setText(str(text.decode()))
            if os.path.exists('email_to_login.txt') == True:
                with open('email_to_login.txt', 'r') as file:
                    data = file.readlines()
                    ento = data[0]
                password_mail = b"password_for_emailcry_pt_Or"
                salt = b'\x8f\xd9\xd4c\x8b\xad\xefu\xbb\x86\xe9\xfb\xcf\xe9\xa3*'
                kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                                 length=32,
                                 salt=salt,
                                 iterations=100000,
                                 )
                key = base64.urlsafe_b64encode(kdf.derive(password_mail))
                f = Fernet(key)
                text = f.decrypt(ento.encode())
                self.sen.plainTextEdit_send_to.setPlainText(str(text.decode()))
            elif os.path.exists('email_to_login.txt') == False and os.path.exists('email_login.txt') == False:
                self.msg_warn("Данные для автозаполнения не записаны в программу")
                Dialog_send.activateWindow()
        except Exception:
            self.msg_crit("Что-то пошло не так. Проверьте данные автозаполнения в настройках.")


    def msg_warn(self, text):
        QMessageBox.warning(self, "Предупреждение ",
                            text, QMessageBox.Ok)
    def msg_crit(self, text):
        QMessageBox.critical(self, "Ошибка ",
                            text, QMessageBox.Ok)
    def msg_info(self, text):
        QMessageBox.information(self, "Информация ",
                            text, QMessageBox.Ok)

    def clear_logs(self):
        with open('Logs.txt', 'r') as f:
            text = str(f.readlines()[0])
        with open('Logs.txt', 'w') as fa:
            fa.write('')
            fa.write(text)
        self.ui.lineEdit_sys_mes.setText("Log file was cleared")

    def show_iter(self):
        with open(papath + 'For_text.txt', 'r') as f:
            self.st.lineEdit_iter.setText(str(f.readlines()[0]))

    def add_logs(self, text):
        with open('Logs.txt', 'a') as f:
            f.write(str(now.day) + ":" + str(now.month) + ":" + str(now.hour) + ":"+str(now.minute) +":"+ '\n')
            f.write(text)
            f.write('\n')
            f.close()

    def copy_p(self):
        text = self.st.lineEdit_iter.text()
        if len(text) > 0:
            pyperclip.copy(text)
            self.st.lineEdit_sys_mes.setText("Your code was copied")
            self.add_logs("Your code was copied")
            self.st.lineEdit_iter.setText('')
        else:
            self.st.lineEdit_sys_mes.setText("The field is empty")
            self.add_logs("The field is empty")
            self.st.lineEdit_iter.setPlaceholderText("There are not any text in the field")

    def generate_iter(self):
        iterr = random.randint(100000,999999)
        self.st.lineEdit_iter.setText(str(iterr))

    def write_iter(self):
        try:
            if len(self.st.lineEdit_iter.text()) == 6:
                a = int(self.st.lineEdit_iter.text())
                with open(papath + 'For_text.txt', "w") as f:
                    f.write(str(self.st.lineEdit_iter.text()))
                self.copy_p()
                self.st.lineEdit_iter.setText('')
                self.st.lineEdit_iter.setPlaceholderText('')
                self.st.lineEdit_sys_mes.setText("Your code was written to the program" + '\n' "and" + '\n' + "Your code was copied")
                self.msg_info("Ваш код был записан в программу и скопирован в буфер обмена")
                self.clear_logs()
                self.Start_up()
            else:
                self.st.lineEdit_iter.clear()
                self.st.lineEdit_iter.setPlaceholderText("Wrong Input")
                self.st.lineEdit_sys_mes.setText("The length of your code is not 6")
                self.msg_crit("Неправильный ввод. Длина вашего кода меньше или больше 6")
        except Exception:
            self.st.lineEdit_sys_mes.setText(
                "Probably your code isn't integer" + '\n'  + "Input INTEGER, NOT String" + '\n' + "Or the length of your code is not 6")
            self.st.lineEdit_iter.clear()
            self.st.lineEdit_iter.setPlaceholderText("Wrong Input...")
            self.add_logs(
                "Your code isn't integer" + '\n'  + "Input INTEGER, NOT String")
            self.msg_crit("Неправильнй ввод, ваш код должен состоять из цифр")

    def smtp_checker(self, mail):
        if mail.endswith("@gmail.com"):
            return 'smtp.gmail.com'
        elif mail.endswith("@mail.ru"):
            return 'smtp.mail.ru'

    def de_vid(self):
        self.devid.lineEdit_sys_messages_decode.clear()
        self.devid.lineEdit_path.clear()
        self.devid.plainTextEdit_for_pass_decode.clear()
        Dialog_decode_video.exec_()

    def dec_vid(self):
        filename = self.devid.lineEdit_path.text()
        try:
            if os.path.exists(filename) == True:
                if len(self.devid.plainTextEdit_for_pass_decode.text()) == 0:
                    self.msg_crit("Вы не ввели пароль для дешифрования")
                    Dialog_decode_video.activateWindow()
                else:
                    passw = self.devid.plainTextEdit_for_pass_decode.text()
                    self.write_key(passw)
                    f = Fernet(self.load_key())
                    self.clear_crypto()
                    with open(filename, 'rb') as file:
                        encrypted_data = file.read()
                    decrypted_data = f.decrypt(encrypted_data)
                    with open(papath + 'Coded_Files/For_Input.txt', 'wb') as file:
                        file.write(decrypted_data)

                    self.decode_vid()
            else:
                self.devid.lineEdit_sys_messages_decode.setText(
                    "There are not any 'file_i' or you do not choose anything")
                self.add_logs("There are not any 'file_i' or you do not choose anything")
                self.msg_crit("Вы не выбрали файл для дешифровки, либо такого файла не существует")
                Dialog_decode_video.activateWindow()
        except Exception:
            self.devid.lineEdit_sys_messages_decode.setText("Invalid Token")
            self.add_logs("Invalid Token")
            self.msg_crit("Указанный вами ключ - не валидный")
            Dialog_decode_video.activateWindow()

    def decode_vid(self):
        try:
            img_form = '.mp4'
            with open(papath + 'Coded_Files/For_Input.txt', 'rb') as file:
                img_data = file.read()

            with open(papath + "Download_Pic/pic" + str(img_form), "wb") as fh:
                fh.write(base64.decodebytes(img_data))

            self.devid.lineEdit_sys_messages_decode.setText("!!! Done !!!")
            self.add_logs("!!! Done !!!")
            self.devid.lineEdit_sys_messages_decode.setText("!!! Your video is in the Folder 'Собранное фото' !!!")
            self.add_logs("!!! Your video is in the Folder 'Собранное фото' !!!")
            self.devid.plainTextEdit_for_pass_decode.clear()
            self.devid.lineEdit_path.clear()
            self.save_dialog()
            self.sobr_folder()
            Dialog_decode_video.close()

        except Exception:
            self.devid.lineEdit_sys_messages_decode.setText("!!! Something went wrong, try another one !!!")
            self.add_logs("!!! Something went wrong, try another one !!!")
            self.msg_crit("Что-то пошло не так. Убедитесь в правильности введённых данных")

    def en_vid(self):
        self.envid.lineEdit_sys_messages_decode.clear()
        self.envid.lineEdit_path.clear()
        self.envid.plainTextEdit_for_pass_decode.clear()
        Dialog_encode_video.exec_()

    def encode_video(self):
        if len(self.envid.plainTextEdit_for_pass_decode.text()) == 0 and len(self.envid.lineEdit_path.text()) == 0:
            self.msg_crit("Вы ничего не ввели!")
            Dialog_encode_video.activateWindow()
        elif len(self.envid.plainTextEdit_for_pass_decode.text()) == 0:
            self.msg_crit("Вы не ввели пароль для шифрования!")
            Dialog_encode_video.activateWindow()
        elif len(self.envid.lineEdit_path.text()) == 0:
            self.msg_crit("Вы не выбрали файл для шифрования!")
            Dialog_encode_video.activateWindow()
        elif len(self.envid.plainTextEdit_for_pass_decode.text()) != 0 and len(self.envid.lineEdit_path.text()) != 0:
            try:
                passw = self.envid.plainTextEdit_for_pass_decode.text()
                self.write_key(passw)
                self.renamer()
                # print("IMG_FORM = ", img_form)
                with open(papath + 'Upload_Pic/pic' + str(img_form), "rb") as vid_file:
                    b64_string = base64.b64encode(vid_file.read())
                with open(papath + 'Coded_Files/For_Sending.txt', 'wb') as file:
                    file.write(b64_string)
                filenamer = papath + 'Coded_Files/For_Sending.txt'
                self.encrypt_vid(filenamer, self.load_key())
                self.clear_crypto()
                Dialog_encode_video.close()
                self.add_logs("!!! Done !!!")
                self.add_logs("!!! file_v.txt in your ALL_SAFE Folder !!!")
                self.envid.plainTextEdit_for_pass_decode.clear()
                self.envid.lineEdit_path.clear()
                self.msg_info("Ваш видеофайл зашифрован!"+'\n'+"Файл с зашифрованным видео, под названием 'file_v.txt'"+'\n'+"находится в папке ALL_SAFE")
            except Exception:
                self.envid.lineEdit_sys_messages_decode.setPlainText("!!! Something went wrong, try another one !!!" '\n' "!!! Probably there are no pictures chosen !!!")
                self.add_logs("!!! Something went wrong, try another one !!!")
                self.add_logs("!!! Probably there are no pictures chosen !!!")
                self.msg_crit("Что-то пошло не так!"+'\n'+"Возможно указанного вами файла не существует!")

    def encrypt_vid(self, filenamer, key):
        f = Fernet(key)
        with open(filenamer, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(papath_a + 'file_v.txt', 'wb') as file:
            file.write(encrypted_data)

    def settings(self):
        self.st.lineEdit.clear()
        self.st.lineEdit_2.clear()
        self.st.lineEdit_iter.clear()
        self.st.lineEdit_sys_mes.clear()
        self.st.lineEdit_from_pass.clear()
        self.st.lineEdit_from.clear()
        self.st.lineEdit_to.clear()
        Dialog_settings.exec_()

    def change_pass(self):
        if self.st.lineEdit.text() == self.st.lineEdit_2.text() and len(self.st.lineEdit.text()) != 0:
            pswd(self.st.lineEdit.text())
            self.ui.lineEdit_sys_mes.setText("Password was change")
            self.add_logs("Password was change")
            with open('logs.txt', 'w') as file:
                file.write("Logs file:")
            Dialog_settings.close()
            self.msg_info("Пароль был изменён")
        else:
            self.st.lineEdit.clear()
            self.st.lineEdit_2.clear()
            self.st.lineEdit.setPlaceholderText("Попробуйте снова")
            self.st.lineEdit_2.setPlaceholderText("Попробуйте снова")
            self.msg_warn("Пароли не совпадают, попробуйте снова")

    def delete_pass(self):
        with open('icons/f.key', 'w') as file:
            file.write("")
        with open('icons/sys.key', 'w') as file:
            file.write("")
        with open('logs.txt', 'w') as file:
            file.write("L0gs file:")
        self.ui.lineEdit_sys_mes.setText("Password was deleted")
        self.add_logs("Password was deleted")
        Dialog_settings.close()
        self.msg_info("Пароль был удалён")

    def Start_up(self):
        global papath
        papath = os.path.abspath(os.curdir)
        papath = papath.replace('\\',"/")
        papath = papath.replace('main_program','Data/')
        global papath_a
        papath_a = papath.replace('Data/', '')
        with open(papath + 'Coded_Files/For_Input.txt', 'w') as r:
            r.write("")
        with open(papath + 'Coded_Files/For_Sending.txt', 'w') as r:
            r.write("")
        if os.path.exists(papath + "Download_Pic"):
            shutil.rmtree(papath + "Download_Pic")
        os.mkdir(papath + "Download_Pic")
        if os.path.exists(papath + "Upload_Pic"):
            shutil.rmtree(papath + "Upload_Pic")
        os.mkdir(papath + "Upload_Pic")
        global now_day
        now_day = 0
        global now_month
        now_month = 0
        with open(papath + 'For_text.txt', "r") as f:
            global itr
            itr = f.readlines()[0]
            try:
                itr = int(itr)
            except Exception:
                self.ui.lineEdit_sys_mes.setText("Your sync code is Invalid." + '\n' + "Go to settings to fix it, if you want")
                self.add_logs("Your sync code is Invalid." + '\n' + "Go to settings to fix it, if you want")
                itr = 100000
        if os.path.exists('Logs.txt') == True:
            with open('Logs.txt', 'r') as f:
                try:
                    a = f.readlines()
                    if a[1][4] == ':':
                        a = a[1][3]
                    elif a[1][5] == ':':
                        a = a[1][3:5]
                    if str(now.month) == str(int(a)+1):
                        # self.clear_logs()
                        QMessageBox.warning(self, "Рекомендация ",
                                                "Прошел месяц, для безопасности смените пин-код синхронизации", QMessageBox.Ok)
                except Exception:
                    a=1
        else:
            with open('Logs.txt', 'w') as f:
                f.write('')

    def write_key(self, password):
        password = password.encode()
        password = password + str(now_month).encode()
        salt = b'\x11\xed~z\xe4~I\xab#_Q(\x98\x91\x8aR' + str(now_day).encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=itr,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        with open(papath + 'crypto.key', 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        return open(papath + 'crypto.key', 'rb').read()


    def check(self):
        with open(papath + 'num_list.txt', 'r') as r:
            with open(papath + 'num_list.txt', 'w') as file:
                file.write("")
                for i in range(100):
                    if os.path.exists(papath + 'Gallery/pic_' + str(i) + '.jpg') == True:
                        file.write('pic_' + str(i) + '.jpg' + '\n')
                    elif os.path.exists(papath + 'Gallery/pic_' + str(i) + '.png') == True:
                        file.write('pic_' + str(i) + '.png' + '\n')
                    elif os.path.exists(papath + 'Gallery/pic_' + str(i) + '.mp4') == True:
                        file.write('pic_' + str(i) + '.mp4' + '\n')
                    elif os.path.exists(papath + 'Gallery/pic_' + str(i) + '.avi') == True:
                        file.write('pic_' + str(i) + '.avi' + '\n')

        with open(papath + 'Coded_Files/For_Input.txt', 'w') as r:
            r.write("")
        with open(papath + 'Coded_Files/For_Sending.txt', 'w') as r:
            r.write("")

    def renamer(self):
        if len(self.enimg.lineEdit_path.text()) == 0:
            filename = self.envid.lineEdit_path.text()
        elif len(self.envid.lineEdit_path.text()) == 0:
            filename = self.enimg.lineEdit_path.text()
        if filename.endswith('.png'):
            shutil.copy(filename, papath + "Upload_Pic/pic.png")
        if filename.endswith('.jpg'):
            shutil.copy(filename, papath + "Upload_Pic/pic.jpg")
        if filename.endswith('.mp4'):
            shutil.copy(filename, papath + "Upload_Pic/pic.mp4")
        if filename.endswith('.avi'):
            shutil.copy(filename, papath + "Upload_Pic/pic.avi")
        global img_form
        file_list = os.listdir(papath + 'Upload_Pic')
        for ind, file_name in enumerate(file_list, 1):
            if file_name.endswith('.png'):
                composite_name = 'pic.png'
                img_form = '.png'
                os.rename(os.path.join(papath + 'Upload_Pic', file_name), os.path.join(papath + 'Upload_Pic', composite_name))
            elif file_name.endswith('.jpg'):
                composite_name = 'pic.jpg'
                img_form = '.jpg'
                os.rename(os.path.join(papath + 'Upload_Pic', file_name), os.path.join(papath + 'Upload_Pic', composite_name))
            elif file_name.endswith('.mp4'):
                composite_name = 'pic.mp4'
                img_form = '.mp4'
                os.rename(os.path.join(papath + 'Upload_Pic', file_name), os.path.join(papath + 'Upload_Pic', composite_name))
            elif file_name.endswith('.avi'):
                composite_name = 'pic.avi'
                img_form = '.avi'
                os.rename(os.path.join(papath + 'Upload_Pic', file_name), os.path.join(papath + 'Upload_Pic', composite_name))

    def replace(self):
        img_form = ''
        if os.path.exists(papath + "Download_pic/pic.jpg") == True:
            img_form = '.jpg'
        if os.path.exists(papath + "Download_pic/pic.png") == True:
            img_form = '.png'
        if os.path.exists(papath + "Download_pic/pic.mp4") == True:
            img_form = '.mp4'
        if os.path.exists(papath + "Download_pic/pic.avi") == True:
            img_form = '.avi'
        shutil.move(papath + "Download_Pic\pic" + str(img_form), papath + "Gallery\pic" + str(img_form))
        with open(papath + 'num_list.txt', 'r') as r:
            with open(papath + 'num_list.txt', 'a') as file:
                for i in range(100):
                    if os.path.exists(papath + 'Gallery/pic_' + str(i) + str(img_form)) == False:
                        os.rename(papath + "Gallery/pic" + str(img_form), papath + "Gallery/pic_" + str(i) + str(img_form))
                        break
                Dialog_save.close()
                self.check()

    def encode_img(self):
        self.enimg.lineEdit_sys_messages_decode.clear()
        self.enimg.lineEdit_path.clear()
        self.enimg.plainTextEdit_for_pass_decode.clear()
        Encode_img_Dialog.exec_()

    def encode_image(self):
        if len(self.enimg.plainTextEdit_for_pass_decode.text()) == 0 and len(self.enimg.lineEdit_path.text()) == 0:
            self.msg_crit("Вы ничего не ввели!")
            Encode_img_Dialog.activateWindow()
        elif len(self.enimg.plainTextEdit_for_pass_decode.text()) == 0:
            self.msg_crit("Вы не ввели пароль для шифрования!")
            Encode_img_Dialog.activateWindow()
        elif len(self.enimg.lineEdit_path.text()) == 0:
            self.msg_crit("Вы не выбрали файл для шифрования!")
            Encode_img_Dialog.activateWindow()
        elif len(self.enimg.plainTextEdit_for_pass_decode.text()) != 0 and len(self.enimg.lineEdit_path.text()) != 0:
            try:
                passw = self.enimg.plainTextEdit_for_pass_decode.text()
                self.write_key(passw)
                self.renamer()
                with open(papath + 'Upload_Pic/pic' + str(img_form), "rb") as img_file:
                    b64_string = base64.b64encode(img_file.read())
                with open(papath + 'Coded_Files/For_Sending.txt', 'wb') as file:
                    file.write(b64_string)
                filenamer = papath + 'Coded_Files/For_Sending.txt'
                self.encrypt_img(filenamer, self.load_key())
                self.clear_crypto()
                Encode_img_Dialog.close()
                self.add_logs("!!! Done !!!")
                self.add_logs("!!! file_i.txt in your ALL_SAFE Folder !!!")
                self.enimg.plainTextEdit_for_pass_decode.clear()
                self.enimg.lineEdit_path.clear()
                self.msg_info("Ваша картинка зашифрована!"+'\n'+"Файл с зашифрованной картинкой, под названием 'file_i.txt'"+'\n'+"находится в папке ALL_SAFE")
            except Exception:
                self.msg_crit("Что-то пошло не так!"+'\n'+"Возможно указанного вами файла не существует!")
                self.enimg.lineEdit_sys_messages_decode.setPlainText("!!! Something went wrong, try another one !!!" '\n' "!!! Probably there are no pictures chosen !!!")
                self.add_logs("!!! Something went wrong, try another one !!!")
                self.add_logs("!!! Probably there are no pictures chosen !!!")
                Encode_img_Dialog.activateWindow()

    def encrypt_img(self, filenamer, key):
        f = Fernet(key)
        with open(filenamer, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(papath_a + 'file_i.txt', 'wb') as file:
            file.write(encrypted_data)

    def encode_sms(self):
        self.ensms.lineEdit_sys_messages_encode.clear()
        self.ensms.plainTextEdit_for_pass_encode.clear()
        self.ensms.plainTextEdit_for_mess_encode.clear()
        Encode_sms_Dialog.show()

    def encrypt_sms(self):
        if len(self.ensms.plainTextEdit_for_pass_encode.text()) == 0 and len(self.ensms.plainTextEdit_for_mess_encode.toPlainText()) == 0:
            self.msg_crit("Вы ничего не ввели!")
            Encode_sms_Dialog.activateWindow()
        elif len(self.ensms.plainTextEdit_for_mess_encode.toPlainText()) == 0:
            self.msg_crit("Вы не ввели сообщение!")
            Encode_sms_Dialog.activateWindow()
        elif len(self.ensms.plainTextEdit_for_pass_encode.text()) == 0:
            self.msg_crit("Вы не ввели пароль для шифровки!")
            Encode_sms_Dialog.activateWindow()
        elif len(self.ensms.plainTextEdit_for_mess_encode.toPlainText()) != 0 and len(self.ensms.plainTextEdit_for_pass_encode.text()) != 0:
            passw = self.ensms.plainTextEdit_for_pass_encode.text()
            self.write_key(passw)
            f = Fernet(self.load_key())
            self.clear_crypto()
            file_data = self.ensms.plainTextEdit_for_mess_encode.toPlainText()
            file_data = file_data.encode()
            encrypted_data = f.encrypt(file_data)
            with open(papath_a + 'file_t.txt', 'wb') as file:
                file.write(encrypted_data)
            self.ensms.lineEdit_sys_messages_encode.setText("!!! Done !!!")
            self.add_logs("!!! Done !!!")
            self.ensms.plainTextEdit_for_pass_encode.clear()
            self.ensms.plainTextEdit_for_mess_encode.clear()
            self.msg_info("Ваше сообщение зашифровано!"+'\n'+"Файл с зашифрованным смс, под названием 'file_t.txt'" +'\n'+"находится в папке ALL_SAFE")
            Encode_sms_Dialog.close()

    def decode_image(self):
        self.deimg.lineEdit_sys_messages_decode.clear()
        self.deimg.plainTextEdit_for_pass_decode.clear()
        self.deimg.lineEdit_path.clear()
        Decode_img_Dialog.show()

    def decrypt_img(self):
        filename = self.deimg.lineEdit_path.text()
        try:
            if os.path.exists(filename) == True:
                passw = self.deimg.plainTextEdit_for_pass_decode.text()
                self.write_key(passw)
                f = Fernet(self.load_key())
                self.clear_crypto()
                with open(filename, 'rb') as file:
                    encrypted_data = file.read()
                decrypted_data = f.decrypt(encrypted_data)
                with open(papath + 'Coded_Files/For_Input.txt', 'wb') as file:
                    file.write(decrypted_data)

                self.decode_img()
                Decode_img_Dialog.close()
            else:
                self.deimg.lineEdit_sys_messages_decode.setText("There are not any 'file_i' or you do not choose anything")
                self.add_logs("There are not any 'file_i' or you do not choose anything")
        except Exception:
            self.msg_crit("Ваш ключ - не валидный")
            #self.deimg.lineEdit_sys_messages_decode.setText("Invalid Token")
            #self.add_logs("Invalid Token")
            Decode_img_Dialog.activateWindow()

    def decode_img(self):
        try:
            img_form = '.jpg'
            with open(papath + 'Coded_Files/For_Input.txt', 'rb') as file:
                img_data = file.read()

            with open(papath + "Download_Pic/pic" + str(img_form), "wb") as fh:
                fh.write(base64.decodebytes(img_data))

            self.deimg.lineEdit_sys_messages_decode.setText("!!! Done !!!")
            self.deimg.lineEdit_sys_messages_decode.setText("!!! Your picture is in the Folder 'Собранное фото' !!!")
            self.add_logs("!!! Done !!!")
            self.add_logs("!!! Your picture is in the Folder 'Собранное фото' !!!")
            self.deimg.lineEdit_path.clear()
            self.deimg.plainTextEdit_for_pass_decode.clear()
            self.sobr_folder()
            self.save_dialog()

        except Exception:
            self.deimg.lineEdit_sys_messages_decode.setText("!!! Something went wrong, try another one !!!")
            self.add_logs("!!! Something went wrong, try another one !!!")

    def decode_sms(self):
        self.desms.lineEdit_sys_messages_decode.clear()
        self.desms.plainTextEdit_for_mess_decode.clear()
        self.desms.lineEdit_path.clear()
        self.desms.plainTextEdit_for_pass_decode.clear()
        Encode_Dialog.show()

    def decrypt(self, key):
        self.desms.plainTextEdit_for_mess_decode.clear()
        filename = self.desms.lineEdit_path.text()
        if os.path.exists(filename) == False:
            self.desms.lineEdit_sys_messages_decode.setText("!!! You do not choose a file!!!" + '\n' + "or" + '\n' + "Chosen file does not exists")
            self.add_logs("!!! You do not choose a file!!!")
            self.add_logs("Chosen file does not exists")
            self.msg_crit("Вы не указали файл для дешифрования, либо такого файла не существует")
            Encode_Dialog.activateWindow()
        else:
            try:
                if len(self.desms.plainTextEdit_for_pass_decode.text()) == 0:
                    self.msg_crit("Вы не ввели пароль для дешифрования")
                    Encode_Dialog.activateWindow()
                else:
                    passw = self.desms.plainTextEdit_for_pass_decode.text()
                    self.write_key(passw)
                    f = Fernet(self.load_key())
                    self.clear_crypto()
                    with open(filename, 'rb') as file:
                        encrypted_data = file.read()
                    decrypted_data = f.decrypt(encrypted_data)
                    self.desms.plainTextEdit_for_mess_decode.setPlainText(decrypted_data.decode())
                    self.desms.lineEdit_sys_messages_decode.setText("!!! Done !!!")
                    self.add_logs("!!! Done !!!")
                    self.desms.plainTextEdit_for_pass_decode.clear()
                    self.desms.lineEdit_path.clear()
                    self.msg_info("Ваше сообщение расшифровано")
                    Encode_Dialog.activateWindow()

            except Exception:
                self.desms.lineEdit_sys_messages_decode.setText("!!! Invalid Token !!!")
                self.add_logs("!!! Invalid Token !!!")
                self.msg_crit("Указанный вами ключ - не валидный")
                Encode_Dialog.activateWindow()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы точно хотите выйти? ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            with open(papath + 'Coded_Files/For_Input.txt', 'w') as r:
                r.write("")
            with open(papath + 'Coded_Files/For_Sending.txt', 'w') as r:
                r.write("")
            shutil.rmtree(papath + "Download_Pic")
            os.mkdir(papath + "Download_Pic")
            shutil.rmtree(papath + "Upload_Pic")
            os.mkdir(papath + "Upload_Pic")
            self.clear_crypto()
            event.accept()
        else:
            event.ignore()

    def exit_prog(self):
        sys.exit(app.exec_())

    def save_dialog(self):
        Dialog_save.show()

    def save_yes(self):
        self.replace()
        self.msg_info("Файл сохранён в Галерее")

    def upload_folder(self):
        path = papath + "Upload_Pic"
        path = os.path.realpath(path)
        os.startfile(path)

    def sobr_folder(self):
        path = papath + "Download_Pic"
        path = os.path.realpath(path)
        os.startfile(path)

    def gallery_folder(self):
        path = papath + "Gallery"
        path = os.path.realpath(path)
        os.startfile(path)

    def ALL_SAFE(self):
        path = papath_a
        path = os.path.realpath(path)
        os.startfile(path)

    def save_no(self):
        Dialog_save.close()
        if os.path.exists(papath + "Download_pic/pic.jpg") == True:
            os.remove(papath + "Download_pic/pic.jpg")
            self.deimg.lineEdit_sys_messages_decode.setText("Your picture was deleted")
            self.add_logs("Your picture was deleted")
        elif os.path.exists(papath + "Download_pic/pic.png") == True:
            os.remove(papath + "Download_pic/pic.png")
            self.deimg.lineEdit_sys_messages_decode.setText("Your picture file was deleted")
            self.add_logs("Your picture was deleted")
        elif os.path.exists(papath + "Download_pic/pic.mp4") == True:
            os.remove(papath + "Download_pic/pic.mp4")
            self.devid.lineEdit_sys_messages_decode.setText("Your video was deleted")
            self.add_logs("Your picture was deleted")
        elif os.path.exists(papath + "Download_pic/pic.avi") == True:
            os.remove(papath + "Download_pic/pic.avi")
            self.devid.lineEdit_sys_messages_decode.setText("Your video was deleted")
            self.add_logs("Your picture was deleted")
        self.msg_info("Файл был удалён с вашего ПК")

    def clean_gallery(self):
        with open(papath + 'num_list.txt', 'w') as r:
            r.write("")
        shutil.rmtree(papath + "Gallery")
        os.mkdir(papath + "Gallery")
        self.ui.lineEdit_sys_mes.setText("!!! Your Gallery was cleared !!!")
        self.add_logs("!!! Your Gallery was cleared !!!")
        self.msg_info("Галерея была очищена")

    def sending(self):
        self.sen.plainTextEdit_send_from.clear()
        self.sen.plainTextEdit_send_pass.clear()
        self.sen.plainTextEdit_send_to.clear()
        self.sen.lineEdit_system_message_send.clear()
        self.sen.checkBox_sms.setCheckState(0)
        self.sen.checkBox_img.setCheckState(0)
        self.sen.checkBox_video.setCheckState(0)
        self.sen.checkBox_both.setCheckState(0)
        Dialog_send.show()

    def sendd(self, file, n, fro, to, pas, server):

        try:
            TIME_LIMIT = 100
            count = 0
            self.st.progress = QProgressBar(self)
            self.st.progress.setWindowTitle('Подождите..')
            self.st.progress.setGeometry(0, 0, 300, 25)
            self.st.progress.setMaximum(100)
            self.st.progress.show()
            now = datetime.datetime.now()

            # server = 'smtp.gmail.com'
            server = server
            user = fro
            password = pas

            recipients = [to]
            sender = fro
            subject = "NEW MESSAGE"
            text = '<b><h1>NEW MESSAGE</h1></b><b><h2>Сообщение доставлено:</h2></b><br/>' + '\n' + "<b><<< </b><u>" + str(
                now.day) + ' числа, ' + str(now.month) + ' месяца.' + '\n' + 'В ' + str(now.hour) + ':' + str(
                now.minute) + "</u><b> >>></b>"
            html = '<html><head></head><body><p>' + text + '</p></body></html>'

            filepath = file

            count += 25
            self.st.progress.setValue(count)

            basename = os.path.basename(filepath)
            filesize = os.path.getsize(filepath)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = fro
            msg['To'] = to
            msg['Reply-To'] = sender
            msg['Return-Path'] = sender
            msg['X-Mailer'] = 'Python/' + (python_version())


            part_text = MIMEText(text, 'plain')
            part_html = MIMEText(html, 'html')
            part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
            part_file.set_payload(open(filepath, "rb").read())
            part_file.add_header('Content-Description', basename)
            part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
            encoders.encode_base64(part_file)

            msg.attach(part_text)
            msg.attach(part_html)
            msg.attach(part_file)

            count += 25
            self.st.progress.setValue(count)

            if n != 0:
                filepath2 = n[1]

                basename = os.path.basename(filepath2)
                filesize = os.path.getsize(filepath2)

                part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
                part_file.set_payload(open(filepath2, "rb").read())
                part_file.add_header('Content-Description', basename)
                part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
                encoders.encode_base64(part_file)
                msg.attach(part_file)
                try:
                    filepath3 = n[2]
                    basename = os.path.basename(filepath3)
                    filesize = os.path.getsize(filepath3)

                    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
                    part_file.set_payload(open(filepath3, "rb").read())
                    part_file.add_header('Content-Description', basename)
                    part_file.add_header('Content-Disposition',
                                         'attachment; filename="{}"; size={}'.format(basename, filesize))
                    encoders.encode_base64(part_file)
                    msg.attach(part_file)
                except Exception:
                    pass

            mail = smtplib.SMTP_SSL(server)
            mail.login(user, password)

            count += 25
            self.st.progress.setValue(count)

            mail.sendmail(sender, recipients, msg.as_string())

            count += 25
            self.st.progress.setValue(count)

            mail.quit()

            self.st.progress.hide()

            self.add_logs("Message was delivered")
            Dialog_send.close()
            self.msg_info("Ваше сообщение было отправлено адресату на почту")

        except Exception:
            self.st.progress.hide()
            self.sen.lineEdit_system_message_send.setPlainText("Some problem was discovered." +'\n'+"Check password, emails and try again")
            self.msg_crit("Что-то пошло не так." +'\n'+"Проверьте правильность введённых данных.")
            Dialog_send.activateWindow()

    def mail_s(self):
        fro = self.sen.plainTextEdit_send_from.toPlainText()
        to = self.sen.plainTextEdit_send_to.toPlainText()
        pas = self.sen.plainTextEdit_send_pass.text()
        if len(fro) == 0 and len(to) == 0 and len(pas) == 0:
            self.msg_crit("Вы ничего не ввели")
            Dialog_send.activateWindow()
        elif len(fro) == 0:
            self.msg_crit("Вы не указали свою почту")
            Dialog_send.activateWindow()
        elif len(to) == 0:
            self.msg_crit("Вы не указали почту получателя")
            Dialog_send.activateWindow()
        elif len(pas) == 0:
            self.msg_crit("Вы не указали пароль от своей почты")
            Dialog_send.activateWindow()
        elif len(fro) != 0 and len(to) != 0 and len(pas) != 0:
            server = self.smtp_checker(fro)

            if str(self.sen.checkBox_both.checkState()) == "2":
                if os.path.exists(papath_a + 'file_t.txt') == False and os.path.exists(
                        papath_a + 'file_i.txt') == False and os.path.exists(papath_a + 'file_v.txt') == False:
                    self.sen.lineEdit_system_message_send.setPlainText("!!! Всех указанных файлов не найдено !!!")
                    self.msg_crit("Указанных файлов для отправки не найдено. Проверьте наличие таких файлов, как:"+'\n'+"'file_t.txt', 'file_i.txt', 'file_v.txt' в папке ALL_SAFE" + '\n'+ "в зависимости от выбранных ранеее файлов")
                    Dialog_send.activateWindow()

                else:
                    n = [papath_a + "file_t.txt",
                         papath_a + "file_i.txt", papath_a + "file_v.txt"]
                    self.sendd(papath_a + 'file_t.txt', n, fro, to, pas, server)

            elif str(self.sen.checkBox_sms.checkState()) == "2" and str(self.sen.checkBox_video.checkState()) == "2":
                if os.path.exists(papath_a + 'file_t.txt') == False and os.path.exists(
                        papath_a + 'file_v.txt') == False:
                    self.msg_crit("Указанных файлов не существует."+'\n'+"Проверьте наличие файлов 'file_t.txt' и 'file_v.txt' в папке ALL_SAFE")
                    Dialog_send.activateWindow()

            elif str(self.sen.checkBox_sms.checkState()) == "2" and str(self.sen.checkBox_img.checkState()) == "2":
                if os.path.exists(papath_a + 'file_i.txt') == False and os.path.exists(
                        papath_a + 'file_t.txt') == False:
                    self.msg_crit(
                    "Указанных файлов не существует." + '\n' + "Проверьте наличие файлов 'file_t.txt' и 'file_i.txt' в папке ALL_SAFE")
                    Dialog_send.activateWindow()

            elif str(self.sen.checkBox_img.checkState()) == "2" and str(self.sen.checkBox_video.checkState()) == "2":
                if os.path.exists(papath_a + 'file_i.txt') == False and os.path.exists(papath_a + 'file_v.txt') == False:
                    self.msg_crit(
                    "Указанных файлов не существует." + '\n' + "Проверьте наличие файлов 'file_i.txt' и 'file_v.txt' в папке ALL_SAFE")
                    Dialog_send.activateWindow()

            elif str(self.sen.checkBox_sms.checkState()) == "2":
                if os.path.exists(papath_a + 'file_t.txt') == True:
                    self.sendd(papath_a + 'file_t.txt', 0, fro, to, pas, server)
                else:
                    self.sen.lineEdit_system_message_send.setPlainText("file_t does not exist !!!")
                    self.msg_crit("Указанного файла не существует."+'\n'+"Проверьте наличие файла 'file_t.txt' в папке ALL_SAFE")
                    Dialog_send.activateWindow()

            elif str(self.sen.checkBox_img.checkState()) == "2":
                if os.path.exists(papath_a + 'file_i.txt') == True:
                    self.sendd(papath_a + 'file_i.txt', 0, fro, to, pas, server)
                else:
                    self.sen.lineEdit_system_message_send.setPlainText("!!! file_i does not exist !!!")
                    self.msg_crit("Указанного файла не существует."+'\n'+"Проверьте наличие файла 'file_i.txt' в папке ALL_SAFE")
                    Dialog_send.activateWindow()

            elif str(self.sen.checkBox_video.checkState()) == "2":
                if os.path.exists(papath_a + 'file_v.txt') == True:
                    self.sendd(papath_a + 'file_v.txt', 0, fro, to, pas, server)
                else:
                    self.sen.lineEdit_system_message_send.setPlainText("!!! file_v does not exist !!!")
                    self.msg_crit("Указанного файла не существует."+'\n'+"Проверьте наличие файла 'file_v.txt' в папке ALL_SAFE")
                    Dialog_send.activateWindow()

            elif str(self.sen.checkBox_sms.checkState()) == "0" and str(self.sen.checkBox_img.checkState()) == "0" and str(self.sen.checkBox_video.checkState()) == "0":
                self.sen.lineEdit_system_message_send.setPlainText("!!! Поставьте галочку в опциях отправки !!!")
                self.msg_warn("Поставьте галочку в опциях отправки")
                Dialog_send.activateWindow()

    def box_checker(self):
        if str(self.sen.checkBox_sms.checkState()) == "2" and str(self.sen.checkBox_img.checkState()) == "2" and str(self.sen.checkBox_video.checkState()) == "2":
            self.sen.checkBox_both.setCheckState(2)
        if str(self.sen.checkBox_both.checkState()) == "2":
            self.sen.checkBox_sms.setCheckState(2)
            self.sen.checkBox_img.setCheckState(2)
            self.sen.checkBox_video.setCheckState(2)
        self.mail_s()

    def delete_t(self):
        if os.path.exists(papath_a + "file_t.txt") == True:
            os.remove(papath_a + "file_t.txt")
        if os.path.exists(papath_a + "file_i.txt") == True:
            os.remove(papath_a + "file_i.txt")
        if os.path.exists(papath_a + "file_v.txt") == True:
            os.remove(papath_a + "file_v.txt")
        self.ui.lineEdit_sys_mes.setText("!!! file_i, file_t and file_v were successfully deleted !!!")
        self.add_logs("!!! file_i, file_t and file_v were successfully deleted !!!")
        self.msg_info("Файлы были удалены с вашего ПК")


    def browse_file_txt(self):
        filen = QFileDialog.getOpenFileName(self,'Open file', os.path.expanduser(r'~\Downloads'), 'Text files (*.txt)')
        filenamee = filen[0]
        self.desms.lineEdit_path.setText(filenamee)
        Encode_Dialog.activateWindow()

    def browse_file_img(self):
        filen = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser(r'~\Downloads'),'Text files (*.txt)')
        filenamee = filen[0]
        self.deimg.lineEdit_path.setText(filenamee)
        Decode_img_Dialog.activateWindow()

    def browse_file_image(self):
        filen = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser(r'~\Downloads'), "Images (*.png *.jpg)")
        filenamee = filen[0]
        self.enimg.lineEdit_path.setText(filenamee)
        Encode_img_Dialog.activateWindow()

    def browse_file_video(self):
        filen = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser(r'~\Downloads'), "Video File (*.mp4 *.avi)")
        filenamee = filen[0]
        self.envid.lineEdit_path.setText(filenamee)
        Encode_img_Dialog.activateWindow()

    def browse_txt_v(self):
        filen = QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser(r'~\Downloads'),
                                            'Text files (*.txt)')
        filenamee = filen[0]
        self.devid.lineEdit_path.setText(filenamee)
        Dialog_decode_video.activateWindow()

if __name__=="__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
