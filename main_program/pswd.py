from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def pswd(passwd):
    passwd = passwd.encode()
    salt = b'\x13\xed~z\xe4~I\xab#_Q(\x94\x91\x89\x8aR'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passwd))
    with open('icons/f.key', 'wb') as key_file:
        key_file.write(key)
    f = Fernet(key)
    filename = 'icons/sys.key'
    file_data = passwd
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    with open('icons/f.key', 'w') as file:
        file.write("")
    print("2")


def enter(passwd):
    global propysk
    propysk = 0
    filename = 'icons/sys.key'
    if os.path.exists(filename) == False:
        propysk = 0
        return 0
    else:
        try:
            passw = passwd
            passw = passw.encode()
            salt = b'\x13\xed~z\xe4~I\xab#_Q(\x94\x91\x89\x8aR'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(passw))

            with open('icons/f.key', 'wb') as key_file:
                key_file.write(key)

            f = Fernet(key)
            with open(filename, 'rb') as file:
                encrypted_data = file.read()

            decrypted_data = f.decrypt(encrypted_data)
            if passw == decrypted_data:
                propysk = 1
            with open('icons/f.key', 'w') as file:
                file.write("")
            return 1

        except Exception:
            print("Pass Invalid")
            propysk = 0
            return 0
