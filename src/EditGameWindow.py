import tkinter
from Global import *
from tkinter import *
from tkinter import ttk
from Game import *
from UserFile import *

class EditGameWindow:

    new_genre = ""
    new_rating_str = ""

    def __init__(self, game, game_list):
        win = tkinter.Tk()
        win.title(game.name)
        win.geometry("600x300")

        genre_label = Label(win, text = "Game genre", font = LARGE_FONT, anchor = W, width = 20, pady = 10)
        genre_label.grid(row = 0, column = 0)
        genre_entry = Entry(win, width = 25, font = LARGE_FONT)
        genre_entry.insert(END, game.genre) #inserting the current genre
        genre_entry.grid(row = 0, column = 1)

        rating_label = Label(win, text = "Game rating (1-10)", font = LARGE_FONT, anchor = W, width = 20, pady = 10)
        rating_label.grid(row = 1, column = 0)
        rating_entry = Entry(win, width = 25, font = LARGE_FONT)
        rating_entry.insert(END, str(game.rating)) #inserting the current rating (0.0 if not rated yet)
        rating_entry.grid(row = 1, column = 1)

        save_button = Button(win, text = "Save", borderwidth = 5, width = 10, font = NORM_FONT, padx = 15, pady = 10, command = self._edit_info(game, genre_entry, rating_entry, game_list))
        save_button.grid(row = 2, column = 1)

        cancel_button = Button(win, text = "Cancel", borderwidth = 5, width = 10, font = NORM_FONT, padx = 15, pady = 10, command = win.destroy)
        cancel_button.grid(row = 3, column = 1)

        win.mainloop()


    def _edit_info(self, game, genre_entry, rating_entry, game_list):
        self.new_genre = genre_entry.get().strip()
        self.new_rating_str = rating_entry.get().strip()

        new_rating = round(float(new_rating_str), 1) #rounding the rating to the nearest 10th place

        game.genre = self.new_genre
        game.rating = new_rating

        new_library_file = UserFile()
        new_library_file.create_library_file(game_list)