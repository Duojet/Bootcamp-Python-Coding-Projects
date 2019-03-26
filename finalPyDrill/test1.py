from tkinter import *
import tkinter as tk
import tkinter.filedialog as tkFileDialog

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self,master, *args, **kwargs)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(1000,400))
        
        self.master.title("Final Python Drill")
        


    
        self.btnSource = tk.Button(self.master,width=14,height=1,text="Select Source")#, command = self.searchDir)
        self.btnSource.grid(row=1,column=0, padx=(25,25),pady=(25,25))

        self.btnDestination = tk.Button(self.master,width=14,height=1,text="Select Destination")#, command = self.searchDir)
        self.btnDestination.grid(row=3,column=0, padx=(25,25),pady=(25,25))

        self.txtSource = tk.Entry(self.master, width=70, font=("sans-serif","14"))
        self.txtSource.grid(row=1, column=1,padx=(0,0),pady=(25,25))

        self.txtDestination = tk.Entry(self.master, width=70, font=("sans-serif","14"))
        self.txtDestination.grid(row=3, column=1,padx=(0,0),pady=(25,25))

        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()     
