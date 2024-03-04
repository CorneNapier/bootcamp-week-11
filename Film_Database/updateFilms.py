from connect import *

def update_film():
    try:
        filmID = int(input("Enter the FilmID of the record to be updated: "))
        dbCursor.execute(f"SELECT * FROM tblFIlms WHERE filmID = {filmID}")
        
        row = dbCursor.fetchone()
        
        if row == None:
            print(f'No record with the FilmID {filmID} exists.')
        else:
            fTitle = input("Enter the film title: ")
            fReleaseYear = int(input("Enter the film's release year: "))
            fRating = input("Enter age rating for the film: ")
            fDuration = int(input("Enter the duration of the film: "))
            fGenre = input("Enter the film's genre: ")
            
            dbCursor.execute("UPDATE tblFilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ? WHERE filmID = ?", (fTitle, fReleaseYear, fRating, fDuration, fGenre, filmID))
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