#Music Player
#Task1 : Open text file, mission file and test file.
#Task2: Create 3 classes :Duree,m Chanson, Album (with tests)
from mission8 import Duree, Chanson, Album
#from test import *
#We need to open the text file in a read mode, and the python files in a x (exectubale) format.
def open_file():
    try:
        with open("music-db.txt","r") as music: # Pending q. : shoudl we open mission8 as an exectubales
            database=music.read().split("\n")
        return database
    except FileNotFoundError:
        return ("The music database was not found")
    except Exception as e:
        return("An error occured:",e)
database=open_file()
print(database)
