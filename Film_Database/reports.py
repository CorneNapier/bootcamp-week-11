from connect import *

def searchByID():
    try: 
        filmID = int(input("Search by filmID: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,))
        row = dbCursor.fetchone()
        
        if row == None:
            print(f'No record with the FilmID {filmID} exists in the table.')
        else:
            print(row)
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")  
    
def searchByGenre():
    try:
        fGenre = input('Search by film genre (Case Sensitive): ')
        dbCursor.execute("SELECT * FROM tblFilms WHERE genre = ?", (fGenre,))
        rows = dbCursor.fetchall()
        
        if not rows:
            print(f'No record with the genre {fGenre} exists in the table.')
        else:
            for row in rows:
                print(row)
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")  

def searchByYear():
    try: 
        fyear = int(input("Search by year of release: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (fyear,))
        rows = dbCursor.fetchall()
        
        if not rows:
            print(f'No record with the year of release {fyear} exists in the table.')
        else:
            for row in rows:
                print(row)
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}") 

def searchByRating():
    try:
        fRating = input('Search by film rating; U, PG, 12A, 12, 15, 18, R18 (Case Sensitive): ')
        dbCursor.execute("SELECT * FROM tblFilms WHERE rating = ?", (fRating,))
        rows = dbCursor.fetchall()
        
        if not rows:
            print(f'No record with the rating {fRating} exists in the table.')
        else:
            for row in rows:
                print(row)
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
    searchByID()
    searchByGenre()
    searchByYear()
    searchByRating()