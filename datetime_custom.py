from datetime import datetime
 
def get_current_date_SAP():
    return datetime.now().strftime('%d.%m.%Y')

def get_current_date_yyyymmdd():
    return datetime.now().strftime('%Y%m%d')

def get_month_string(month):
    return f'0{month}' if int(month) < 10 else str(month)

def get_full_month_name(month):
    return datetime.strptime(str(month), '%m').strftime('%B')

def get_month_of_x_months_ago(x):
    past_x_month = datetime.now().month - int(x)
    while past_x_month <= 0:
        past_x_month += 12
    return past_x_month
 
def get_year_of_x_months_ago(x):
    past_x_month = datetime.now().month - int(x)
    year_of_x_months_ago = datetime.now().year
    while past_x_month <= 0:
        past_x_month += 12
        year_of_x_months_ago -= 1
    return year_of_x_months_ago
 
def get_last_date_of_month_x(x):
    if int(x) == 2:
        return 29 if datetime.now().year % 4 == 0 else 28
    return 30 if int(x) in [4, 6, 9, 11] else 31

def get_fiscal_month_of_month_x(x):
    return int(x) + 9 if int(x) - 3 <= 0 else int(x) - 3
   
def get_fiscal_year_of_month_x(x):
    return datetime.now().year if int(x) >= 4 else datetime.now().year - 1

def get_first_date_of_prev_month():
    return f'01.{getMonthString(get_month_of_x_months_ago(1))}.{get_year_of_x_months_ago(1)}'
 
def get_last_date_of_prev_month():
    return f'{get_last_date_of_month_x(get_month_of_x_months_ago(1))}.{getMonthString(get_month_of_x_months_ago(1))}.{get_year_of_x_months_ago(1)}'
