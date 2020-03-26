import tkinter
from Global import *
from tkinter import *
from tkinter import ttk
from Game import *

class EditGameWindow:

    def __init__(self, name = "Game name"):
        win = tkinter.Tk()
        win.title(name)
        win.geometry("600x300")

        genre_label = Label(win, text = "Game genre", font = LARGE_FONT, anchor = W, width = 20, pady = 10)
        genre_label.grid(row = 0, column = 0)
        genre_entry = Entry(win, width = 25, font = LARGE_FONT)
        genre_entry.grid(row = 0, column = 1)

        rating_label = Label(win, text = "Game rating (1-10)", font = LARGE_FONT, anchor = W, width = 20, pady = 10)
        rating_label.grid(row = 1, column = 0)
        rating_entry = Entry(win, width = 25, font = LARGE_FONT)
        rating_entry.grid(row = 1, column = 1)

        save_button = Button(win, text = "Save", borderwidth = 5, width = 10, font = NORM_FONT, padx = 15, pady = 10)
        save_button.grid(row = 2, column = 0)

        cancel_button = Button(win, text = "Cancel", borderwidth = 5, width = 10, font = NORM_FONT, padx = 15, pady = 10)
        cancel_button.grid(row = 2, column = 1)

        win.mainloop()

EditGameWindow("The Witcher")