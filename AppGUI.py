import webbrowser
import tkinter
import requests
import json
from tkinter import *
from Global import *

'''
REPO_URL = "https://github.com/danieledwardharrington/GamingStatsProject"
USER_STEAM_ID=""
USER_API_KEY=""
'''

class AppGUI:

    def __init__(self):
        root = tkinter.Tk()

        root.title("Gaming Stats")
        root.geometry("1200x700")

        key_label = Label(root, text = "Enter your Steam API key", font = ("Helvetica", 14), anchor = W, width = 25, pady = 10)
        key_label.grid(row = 0, column = 0)
        key_entry = Entry(root, width = 25, font = ("Helvetica", 14))
        key_entry.grid(row = 0, column = 1)
        id_label = Label(root, text = "Enter your SteamID64", font = ("Helvetica", 14), anchor = W, width = 25, pady = 10)
        id_label.grid(row = 1, column = 0)
        id_entry = Entry(root, width = 25, font = ("Helvetica", 14))
        id_entry.grid(row = 1, column = 1)

        submit_button = Button(root, text = "SUBMIT", borderwidth = 5, width = 34, font = ("Helvetica", 12), command = lambda:  self.get_input(key_entry, id_entry))
        submit_button.grid(row = 2, column = 0)

        instructions_button = Button(root, text = "Need API key/Don't know SteamID64?", borderwidth = 5, width = 34, font = ("Helvetica", 12), command = self.send_to_repo)
        instructions_button.grid(row = 3, column = 0)

        root.mainloop()
    def send_to_repo(self):
        webbrowser.open_new_tab(REPO_URL)

    def get_input(self, key_entry, id_entry):
        USER_STEAM_ID = id_entry.get()
        print("Steam user ID: " + USER_STEAM_ID)
        USER_API_KEY = key_entry.get()
        print("Steam user API key: " + USER_API_KEY)

        ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + USER_API_KEY + "&include_appinfo=true" + "&steamid=" + USER_STEAM_ID + "&format=json")
        print(vars(ownedGamesReq))
        ownedGamesJsonObj = json.loads(ownedGamesReq.text)
        for game in ownedGamesJsonObj:
            for name, value in game.items():
                print(name + " " + value)

        