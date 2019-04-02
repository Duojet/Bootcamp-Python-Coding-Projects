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


from tkinter import *
import tkinter as tk
from tkinter import messagebox


##import other modules so we have access to them
import finalPyDrill_gui
import finalPyDrill_func
from finalPyDrill_func import *



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1000,400))
        finalPyDrill_func.center_window(self,1000,400)
        self.master.title("Final Python Drill")
        self.master.protocol("WM_DELETE_WINDOW", lambda: finalPyDrill_func.ask_quit(self))

        self.varSource = StringVar()
        self.varDest = StringVar()
        
        
        finalPyDrill_gui.load_gui(self)
   

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    create_db() #added this, just need to call this on spin up, don't need the calls elsewhere.
    root.mainloop()             
