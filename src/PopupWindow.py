import tkinter
from tkinter import *
from tkinter import ttk
from Global import *
from SteamInfoGUI import *
import os

class PopupWindow:

    def __init__(self, message, delete_user = False, libWin = None):
        
        #General error/exception popup
        win = tkinter.Toplevel()
        win.wm_title("Alert!")
        win.geometry("200x100")
        label = tkinter.Label(win, text = message)
        label.pack(side = "top", fill = "x", pady = 10)

        #Popup to confirm deletion of user info/Steam library files
        if delete_user:
            yes_button = Button(win, text = "Yes", width = 8, command = lambda:  self._confirmed(win, libWin))
            yes_button.pack()

            no_button = Button(win, text = "No", width = 8, command = win.destroy)
            no_button.pack()
        elif not delete_user:
            okay_button = Button(win, text = "Okay", command = win.destroy)
            okay_button.pack()


    def _confirmed(self, win, libWin):
        os.remove(USER_FILE_NAME)
        os.remove(LIBRARY_FILE_NAME)
        from SteamInfoGUI import SteamInfoGUI
        win.destroy()
        libWin.destroy()
        SteamInfoGUI()

