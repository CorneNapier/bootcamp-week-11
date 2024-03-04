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