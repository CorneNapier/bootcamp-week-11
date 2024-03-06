from connect import *

def update_film():
    try:
        filmID = int(input("Enter the FilmID of the record to be updated: "))
        dbCursor.execute(f"SELECT * FROM tblFIlms WHERE filmID = {filmID}")
        
        row = dbCursor.fetchone()
        
        if row == None:
            print(f'No record with the FilmID {filmID} exists.')
        else:
            fName = input("Enter the field (title, yearReleased, rating, duration, genre): ").title()
            fValue = input(f"Enter the value for {fName}: ")
            
            dbCursor.execute(f"UPDATE tblFilms SET {fName} = ? WHERE filmID = ?", (fValue, filmID))
            dbcon.commit()
            print(f'Record with FilmID {filmID} has been Updated.')
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
    update_film()