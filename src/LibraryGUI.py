from tkinter import *
from Global import *
from UserFile import *
from tkinter import ttk

class LibraryGUI:

    game_list = []
    
    def __init__(self):
        self._load_data()
        
        root = tkinter.Tk()

        root.title("Gaming Stats - Library")
        root.geometry("600x600")

        game_box = Listbox(root)
        for game in game_list:
            game_box.insert(game.name)
        
        game_box.pack(side = "top", fill = "x", pady = 10)

        edit_button = Button(root, text = "Edit game info", font = NORM_FONT, width = 20, borderwidth = 5, command = self._edit_game)
        edit_button.pack()


    #loading data from the file
    def _load_data(self):
        pass        

    def _edit_game(self):
        pass