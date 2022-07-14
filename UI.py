import datetime
import os, time, counter
import tkinter
from functools import partial
from tkinter import filedialog

mydate = datetime.datetime.now()
counter = 0

# Function to get the branches of the current month

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.configure(background="white")
        self.root.title("Silhouette Build Notifier")
        self.root.resizable(0, 0)
        folder_path = tkinter.StringVar()
        if not os.path.exists("filepath.txt"):
            folder_path.set("//srtserver-01/build_folder")

        ltitle = tkinter.Label(self.root, text="Silhouette R&T Build Notifier", background="white",
                               font=("Segoe UI", 14))
        ldate = tkinter.Label(self.root, text="{0} - {1}".format(mydate.strftime("%B"), mydate.year),
                              background="white", font=("Segoe UI", 12))
        lcounter = tkinter.Label(self.root, textvariable=self.timer(counter), background="white", font=("Segoe UI", 10))
        bselectserver = tkinter.Label(self.root, text="Time Alive", background="white", activebackground="#339AB7", activeforeground="white", highlightthickness=0, bd=0, font=("Segoe UI", 12))
        ltitle.grid(pady=5, padx=10, columnspan=3)
        ldate.grid(columnspan=3, pady=(0, 15))
        bselectserver.grid(row=3, column=0, padx=10)
        lcounter.grid(row=3, column=1, columnspan=2, padx=(0, 10))

        # Will check to see if the branches are in the watchlist.txt file and set the checkbox to "active" when launching the UI
        self.root.mainloop()

    # Adds / removes the branch from the watchlist.txt file
    def printSelf(self, branchesVar, branches):
        file = open("watchlist.txt", "w+")
        for count, i in enumerate(branchesVar):
            if branchesVar[count].get() == 1:
                file.write(branches[count] + "\n")
        file.close
        return ()

    #Timer
    def timer(self,counter):
        time.sleep(1)
        counter=counter+1
        return(counter)

    # Minimises the UI Window
    def quit(self):
        self.root.iconify()
        return ()

    # Allows the user to select the file path to the build folder
    def browse_button(self, folder_path):
        filename = filedialog.askdirectory()
        folder_path.set(filename)
        file = open("folderpath.txt", "w+")
        file.write(filename + "\n")
        file.close()
        return ()

    def makeLabel(self):
        lTitle = tkinter.Label(self.root, text="THIS IS FROM A FUNCTION", background="white", font=("Segoe UI", 14))
        lTitle.grid(pady=5, padx=10, columnspan=3)
        return ()