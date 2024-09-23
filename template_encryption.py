from cryptography.fernet import Fernet
import time
import os

def encrypt_file(filepath):
    key_filename = 'filekey.key'

    # Generate a key
    key = Fernet.generate_key()

    # Save the key to a file
    with open(key_filename, 'wb') as filekey:
        filekey.write(key)

    # Load the key
    with open(key_filename, 'rb') as filekey:
        key = filekey.read()

    # Initialize Fernet
    fernet = Fernet(key)

    # Open the file to encrypt
    with open(filepath, 'rb') as file:
        original = file.read()

    # Encrypt the file
    encrypted = fernet.encrypt(original)

    # Write the encrypted file
    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    print(filepath, 'has been encrypted')

def run_encrypted_file(filepath, key_filename):
    # Load the key
    with open(key_filename, 'rb') as filekey:
        key = filekey.read()

    # Initialize Fernet
    fernet = Fernet(key)

    # Open the encrypted file
    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    # Decrypt the file
    decrypted = fernet.decrypt(encrypted)

    # Write the decrypted file to a temporary file
    with open('temp.py', 'wb') as dec_file:
        dec_file.write(decrypted)

    # Import the temporary file and run the code
    import temp
    username = temp.get_username()
    password = temp.get_password()
    print(username)
    print(password)

    while not os.path.isfile('temp.py'):
        time.sleep(1)
    os.remove('temp.py')

# filepath = r'..\get_credentials copy.py'
# encrypt_file(filepath)

# keyfilename = r'..\filekey.key'
# run_encrypted_file(filepath, keyfilename)