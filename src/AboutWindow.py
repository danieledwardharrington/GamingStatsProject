import tkinter
from tkinter import *
from Global import *
import webbrowser
from PopupWindow import *

class AboutWindow:

    def __init__(self):
        root = tkinter.Tk()
        root.geometry("650x400")
        root.title("About")
        root.iconbitmap("images/gspDesktop2.ico")

        parent_frame = Frame(root)

        about_label = Label(parent_frame, text = "This app utilizes the Steam Web API.\nCheck the GitHub repo for instructions on obtaining an API key or your SteamID number.", font = NORM_FONT, pady = 10)
        about_label.pack(fill = "x")

        feedback_link = Label(parent_frame, text = "Got feedback? Click here", font = NORM_FONT, fg = "blue", cursor = "hand2")
        feedback_link.pack(fill = "x")
        feedback_link.bind("<Button-1>", lambda e: self._callback(GOOGLE_FORM_URL))

        parent_frame.pack(expand = True)

        root.mainloop()

    def _callback(self, url):
        try:
            webbrowser.open_new_tab(url)
        except Exception as e:
            print(e)
            PopupWindow(BROWSER_EXCEPTION)