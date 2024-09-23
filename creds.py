import os
import pandas as pd

file = 'temp.py'

def decrypt():
    # Load the key
    with open([os.path.join("..", f) for f in os.listdir("..") if f.endswith('key')][0], 'rb') as filekey:
        key = filekey.read()

    from cryptography.fernet import Fernet

    # Initialize Fernet
    fernet = Fernet(key)

    # Open the encrypted file
    with open('..\get_credentials copy.py', 'rb') as enc_file:
        encrypted = enc_file.read()

    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)
    return decrypted

def get_username():
    # Write the decrypted file to a temporary file
    with open(file, 'wb') as dec_file:
        dec_file.write(decrypt())

    # Import the temporary file and run the code
    import temp
    username = temp.get_username()
    os.remove(file)
    return username

def get_password():
    # Write the decrypted file to a temporary file
    with open(file, 'wb') as dec_file:
        dec_file.write(decrypt())

    # Import the temporary file and run the code
    import temp
    password = temp.get_password()
    os.remove(file)
    return password

def get_user_input(message):
    return input(message)

def clearCMD():
    os.system('cls') if os.name == 'nt' else os.system('clear')
