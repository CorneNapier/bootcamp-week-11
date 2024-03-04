from connect import *

def read_films():
    try:
        dbCursor.execute("SELECT * FROM tblFilms") # selects all data from tblFilms
        allFilms = dbCursor.fetchall() # retrieves all selected rows/records
        
        if allFilms:
            #format output
            print("| filmID |              Title                  | yearReleased | rating  | duration |        genre         |")
            print("*" * 107)
            
            for aFilm in allFilms:
                print(f'|{aFilm[0]:7} | {aFilm[1]:35} |{aFilm[2]:13} | {aFilm[3]:7} | {aFilm[4]:8} | {aFilm[5]:20} |')
                print("-" * 107)
                
        else:
            print("No films found in the table.")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
            
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    
    except sql.Error as er:
        print(f"Failed because of Error: {er}")
if __name__ == "__main__":
    read_films()
    