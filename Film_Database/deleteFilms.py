from connect import *

def delete_film():
    try:
        filmID = int(input("Enter the FilmID of the record to be deleted: "))
        dbCursor.execute(f"SELECT * FROM tblFIlms WHERE filmID = {filmID}")
        
        row = dbCursor.fetchone()
            
        if row == None:
            print(f'Delete not possible: No record with the FilmID {filmID} exists.')
        else:
            dbCursor.execute("DELETE FROM tblFIlms WHERE filmID = ?", (filmID,))
            dbcon.commit()
            print(f'The record with the filmID {filmID} has been deleted from the tblFIlms table.')
            
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
    delete_film()