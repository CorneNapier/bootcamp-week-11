import sqlite3 as sql #import sqlite3 and assigned it an alias

try:
    # use connect function to open folder then file
    with sql.connect("Film_Database/filmflix.db") as dbcon:  #dbCon hold the folder and file path
        #use to execute sql statement with the execute method
        dbCursor = dbcon.cursor()
except sql.OperationalError as e: #raise sql error
    #handling the error
    print(f'Connection Failed: {e}')
    