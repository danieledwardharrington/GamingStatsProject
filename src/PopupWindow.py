import tkinter
from tkinter import *
from tkinter import ttk
from Global import *

class PopupWindow:

    def __init__(self, message):
        win = tkinter.Toplevel()
        win.wm_title("Alert!")
        win.geometry("200x100")

        label = tkinter.Label(win, text = message)
        label.pack(side = "top", fill = "x", pady = 10)

        okay_button = ttk.Button(win, text = "Okay", command = win.destroy)
        okay_button.pack()