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
        self._load_data()
        
        root = tkinter.Tk()

        root.title("Gaming Stats - Library")
        root.geometry("600x600")

        game_box = Listbox(root, selectmode = SINGLE)
        for game in self.game_list:
            game_box.insert(game.name)
        
        game_box.pack(side = "top", fill = "x", pady = 10)

        edit_button = Button(root, text = "Edit rating/genre", font = NORM_FONT, width = 20, borderwidth = 5, command = self._edit_game(game_box))
        edit_button.pack()

        delete_info_button = Button(root, text = "Delete user", font = NORM_FONT, width = 20, borderwidth = 5, command = self._delete_user(root))
        delete_info_button.pack()
        
        root.mainloop

    #loading data from the file
    def _load_data(self):
        pickle_in = open(LIBRARY_FILE_NAME, "rb")
        self.game_list = pickle.load(pickle_in)        

    def _edit_game(self, game_box):
        game_name = game_box.get(ACTIVE)

        game_to_edit = Game()

        for game in self.game_list:
            if game_name == game.name:
                game_to_edit = game

        edit_game_window = EditGameWindow(game, self.game_list)

    def _delete_user(self, root):
        confirm_popup = PopupWindow("Are you sure?", True)

        if confirm_popup.clicked_yes:
            os.remove(USER_FILE_NAME)
            os.remove(LIBRARY_FILE_NAME)
            steam_info_win = SteamInfoGUI()
            root.destroy()