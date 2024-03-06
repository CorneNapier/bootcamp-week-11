import sqlite3 as sql #import sqlite3 and assigned it an alias

try:
    #to use the sqlite(sql) module by creating a variable to hold the path to the folder/file
    # use connect function to open folder then file
    with sql.connect('ExpenseTracker/Database/expenses.db') as dbCon: #dbCon hold the folder and file path
        #use to execute sql statement with the execute method
        dbCursor = dbCon.cursor()
except sql.OperationalError as e: #raise sql error
    #handling the error
    print(f'Connection Failed: {e}')