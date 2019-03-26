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


import finalPyDrill_main
import finalPyDrill_func

def load_gui(self):
        self.btnSource = tk.Button(self.master,width=14,height=1,text="Select Source", command=lambda:  finalPyDrill_func.searchSource(self))
        self.btnSource.grid(row=1,column=0, padx=(25,25),pady=(25,10))



        self.btnFindTxt = tk.Button(self.master,width=14,height=1,text="Locate .txt Files", command=lambda:  finalPyDrill_func.findPath(self))
        self.btnFindTxt.grid(row=2,column=0, padx=(25,25),pady=(0,25))


        
        self.btnDest = tk.Button(self.master,width=14,height=1,text="Select Destination", command=lambda:  finalPyDrill_func.searchDest(self))
        self.btnDest.grid(row=5,column=0, padx=(25,25),pady=(25,25))



        self.txtSource = tk.Entry(self.master, text=self.varSource, width=70, font=("sans-serif","14"))
        self.txtSource.grid(row=1, column=1,padx=(0,0),pady=(25,10))

        

        self.txtDest = tk.Entry(self.master, width=70, font=("sans-serif","14"))
        self.txtDest.grid(row=5, column=1,padx=(0,0),pady=(25,25))  














if __name__ == "__main__":
    pass                        #doesn't run this whole page.  Only the phonebook_main file does that
