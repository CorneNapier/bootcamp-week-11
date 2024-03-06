from connect import *

def insert_films():
    try:
        #filmID(auto increment), title, yearReleased, rating, duration, genre
        fTitle = input("Enter the film title: ")
        fReleaseYear = int(input("Enter the film's release year: "))
        fRating = input("Enter age rating for the film: ")
        fDuration = int(input("Enter the duration of the film: "))
        fGenre = input("Enter the film's genre: ")
        
        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)", (fTitle, fReleaseYear, fRating, fDuration, fGenre))
        dbcon.commit()
        
        print(f'{fTitle} has been inserted into tblFilms')
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
            
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    
    except sql.Error as er:
        print(f"Failed because of Error: {er}")
if __name__ == "__main__": 
    insert_films()