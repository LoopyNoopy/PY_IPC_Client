import datetime
import os
import time
import tkinter
from multiprocessing.connection import Listener
import multiprocessing
from tkinter import filedialog

import main

mydate = datetime.datetime.now()

# Function to get the branches of the current month

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.configure(background="white")
        self.root.title("IPC Proof of Concept")
        self.root.resizable(0, 0)
        folder_path = tkinter.StringVar()
        root_timer = tkinter.IntVar()

        ltitle = tkinter.Label(self.root, text="IPC Proof of Concept", background="white",
                               font=("Segoe UI", 14))
        ldate = tkinter.Label(self.root, text="{0} - {1}".format(mydate.strftime("%B"), mydate.year),background="white", font=("Segoe UI", 12))
        bchangebackgroundcolor = tkinter.Button(self.root, text="Change Background", command=self.changebackground)
        ltitle.grid(pady=5, padx=10, columnspan=3)
        ldate.grid(columnspan=3, pady=(0, 15))
        bchangebackgroundcolor.grid(row=3, column=1, padx=10)

        self.root.mainloop()

    def changebackground(self):
        background = main.IPCSend("background")
        address = ('localhost', 7000)  # family is deduced to be 'AF_INET'
        listener = Listener(address, authkey=b'blah')
        print("Waiting for response")
        waiting = True
        while waiting == True:
            conn = listener.accept()
            print('connection accepted from', listener.last_accepted)
            msg = conn.recv()
            break
        listener.close()
        self.root.configure(background = msg)
        return()

    # Minimises the UI Window
    def quit(self):
        self.root.iconify()
        return()