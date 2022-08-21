import datetime
import pyodbc
import uuid

server = 'DESKTOP-DLPF745\MSSQLSERVER01'
database = 'ALL_CURRENCIES'
username = 'py'
password = '111'
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

def save_all_data(data):
    print(datetime.datetime.now())
    print('Amount of currencies: ' + str(len(data)))

    con = pyodbc.connect(conn_str)
    con.autocommit = True
    cur = con.cursor()

    now = datetime.datetime.now()

    for item in data:
        cur.execute("INSERT INTO Tickers VALUES (?, ?, ?, ?)", str(uuid.uuid4()), item["symbol"], item["price"], now)

    con.commit()
    con.close()