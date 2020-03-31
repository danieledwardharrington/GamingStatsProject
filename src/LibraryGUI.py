from tkinter import *
from Global import *
from UserFile import *
from tkinter import ttk
import pickle
from EditGameWindow import *
import os
from SteamInfoGUI import *

class LibraryGUI:

    game_list = []
    
    def __init__(self):
        root = tkinter.Tk()

        self._load_data()

        root.title("Gaming Stats - Library")
        root.geometry("600x600")

        frame = Frame(root, borderwidth = 1, height = 300, width = 300)
        frame.pack(fill = BOTH, expand = True)
        game_scrollbar = Scrollbar(frame)
        game_scrollbar.pack(side = RIGHT, fill = Y)

        game_box = Listbox(frame, selectmode = SINGLE, borderwidth = 0)
        for game in self.game_list:
             game_box.insert(END, game.name)
        game_box.pack(fill = BOTH, expand = True)
        

        game_box.config(yscrollcommand = game_scrollbar.set)
        game_scrollbar.config(command = game_box.yview)

        edit_button = Button(root, text = "Edit rating/genre", font = NORM_FONT, width = 20, borderwidth = 5, command = lambda: self._edit_game(game_box))
        edit_button.pack()

        delete_info_button = Button(root, text = "Delete user", font = NORM_FONT, width = 20, borderwidth = 5, command = lambda: self._delete_user(root))
        delete_info_button.pack()

        update_library_button = Button(root, text = "Update library", font = NORM_FONT, width = 20, borderwidth = 5)
        update_library_button.pack()
        
        root.mainloop()

    #loading data from the file
    def _load_data(self):
        try:
            pickle_in = open(LIBRARY_FILE_NAME, "rb")
            self.game_list = pickle.load(pickle_in) 
        except Exception as e:
            print("File not found")
            print(e)
            popup = PopupWindow("Library file not found")

    def _edit_game(self, game_box):
        game_name = game_box.get(ACTIVE)

        game_to_edit = Game()

        for game in self.game_list:
            if game_name == game.name:
                game_to_edit = game

        edit_game_window = EditGameWindow(game_to_edit, self.game_list)

    def _delete_user(self, root):
        confirm_popup = PopupWindow("Are you sure?", True, root)