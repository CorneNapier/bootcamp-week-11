from connect import *

dbCursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        ID INTEGER PRIMARY KEY,
        expenseName TEXT,
        amount REAL,
        expenseCategory TEXT
    )
    """)
dbCon.commit()