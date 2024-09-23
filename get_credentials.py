# clone this file and use the cloned file for encryption
#
# the logic behind this code is to read an encrypted excel file that contains credentials
# the excel file is a 2x2 dataframe, with its two columns named 'Username' and 'Password'

import io
import msoffcrypto
import pandas as pd

def get_data():
    # this excel path contains your credentials
    excelpath = r"...\credentials.xlsx"
    
    with open(excelpath, 'rb') as file:
        office_file = msoffcrypto.OfficeFile(file)

        # the excel password
        excelpassword = '...'
        
        office_file.load_key(excelpassword)
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
