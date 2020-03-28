import tkinter
from tkinter import *
from tkinter import ttk
from Global import *
from SteamInfoGUI import *
import os

class PopupWindow:

    def __init__(self, message, delete_user = False):
        
        win = tkinter.Toplevel()
        win.wm_title("Alert!")
        win.geometry("200x100")
        label = tkinter.Label(win, text = message)
        label.pack(side = "top", fill = "x", pady = 10)

        if not delete_user:
            okay_button = ttk.Button(win, text = "Okay", command = win.destroy)
            okay_button.pack()
        else:
            yes_button = ttk.Button(win, text = "Yes", command = _confirmed(win))

            no_button = ttk.Button(win, Text = "No", command = win.destroy)
            no_button.pack()

    def _confirmed(self, win):
        os.remove(USER_FILE_NAME)
        os.remove(LIBRARY_FILE_NAME)
        steam_info_win = SteamInfoGUI()
        win.destroy

