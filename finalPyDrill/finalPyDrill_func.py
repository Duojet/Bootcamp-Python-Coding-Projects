##Python Ver:     3.6.6
##
##Author:         Jordan Richter
##
##Purpose:        script will need to provide the user with a graphical user interface
##                that includes two buttons allowing the user to browse their own system
##                and select a source directory and a destination directory. Your script
##                should also show those selected directory paths in their own corresponding
##                text fields.
##
##                Next, your script will need to provide a button for the user to execute
##                a function that should iterate through the source directory, checking
##                for the existence of any files that end with a “.txt” file extension and
##                if so, cut the qualifying files and paste them within the selected
##                destination directory.
##
##                Finally, your script will need to record the file names that were
##                moved and their corresponding modified time-stamps into a database
##                and print out those text files and their modified time-stamps
##                to the console.
##                
##
##Tested OS:      This code was written and tested on Windows 10.


import os
from tkinter import *
import tkinter as tk
import sqlite3
import shutil
import tkinter.filedialog as tkFileDialog




# Be sure to import our other modules

import finalPyDrill_main
import finalPyDrill_gui

##global sourcePath

def center_window(self, w, h):  # pass in the tkinter frame (master) reference and the w and h
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# catch if the user clicks on the window's upper-right "X" to ensure they want to close
##def ask_quit(self):
##    if messagebox.askokcancel("Exit program", "Okay to exit application??"):        
##        # this closes app
##        self.master.destroy()
##        os._exit(0)


#==========================================================


##btnSource = searchSource(self)

def searchSource(self):
    btnSource = tkFileDialog.askdirectory()
    self.txtSource.insert(END,btnSource)

        
def searchDest(self):
    btnDest = tkFileDialog.askdirectory()
    self.txtDest.insert(END,btnDest)

 
def cutMove(self):
    sourcePath = self.varSource.get()
    destPath = self.varDest.get()
    sourceItems = os.listdir(sourcePath)
    for files in sourceItems:
        if files.endswith(".txt"):
            abPath = os.path.join(sourcePath, files)
            shutil.move(abPath, destPath)
            
    movedItems = os.listdir(destPath)
    itemList = []
    for names in movedItems:
        abPath2 = os.path.join(destPath, names)
        mTime = os.path.getmtime(abPath2)
        if names.endswith(".txt"):
            itemList.append(names)
            create_db(self)
    
    conn = sqlite3.connect('db_movedFiles.db')
    for names in itemList:
        with conn:
            cur = conn.cursor()
            cur.execute("""INSERT INTO tbl_filenames (col_filename,col_modTime) VALUES (?,?)""", (names, mTime))
            conn.commit()
    conn.close()
    db_contents(self)                

def create_db(self):
    conn = sqlite3.connect('db_movedFiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE if not exists tbl_filenames(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT, col_modTime TEXT);""")
        conn.commit()   
    conn.close()

    
##    populate_db(self)
##
##
##def populate_db(self,itemList):
##    itemList = cutMove(self)
##    conn = sqlite3.connect('db_movedFiles.db')
##    for names in itemList:
##        with conn:
##            cur = conn.cursor()
##            cur.execute("""INSERT INTO tbl_filenames (col_filename,col_modTime) VALUES (?,?)""", (names, mTime))
##            conn.commit()
##    conn.close()
##    db_contents



def db_contents(self):
    conn = sqlite3.connect('db_movedFiles.db')
    with conn:
        cur = conn.cursor()
        for items in cur.execute("SELECT * FROM tbl_filenames"):
            print(items)




if __name__ == "__main__":
    pass

    

                             
            
    


    

    
								  
																	
        
                                  
