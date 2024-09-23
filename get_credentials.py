#do NOT encrypt this file

import io
import msoffcrypto
import pandas as pd

def get_data():
    with open(r"D:\Users\jason.kristanto\Desktop\Excel Password.xlsx", 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)
        office_file.load_key('Lalabora29')
        decrypted_workbook = io.BytesIO()
        office_file.decrypt(decrypted_workbook)
        df = pd.read_excel(decrypted_workbook)  
        del office_file, decrypted_workbook
    return df

def get_username():
    df = get_data()
    return df['Username'].values[0]

def get_password():
    df = get_data()
    return df['Password'].values[0]
