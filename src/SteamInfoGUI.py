import webbrowser
import tkinter
import requests
import json
import os
from tkinter import *
from Global import *
from UserFile import *

class SteamInfoGUI:

    user_api_key = ""
    user_id_number = ""

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

        submit_button = Button(root, text = "SUBMIT", borderwidth = 5, width = 34, font = ("Helvetica", 12), command = lambda:  self._get_input(key_entry, id_entry))
        submit_button.grid(row = 2, column = 0)

        instructions_button = Button(root, text = "Need API key/Don't know SteamID64?", borderwidth = 5, width = 34, font = ("Helvetica", 12), command = self._send_to_repo)
        instructions_button.grid(row = 3, column = 0)

        #root.iconbitmap()
        root.mainloop()

    def _send_to_repo(self):
        try:
            webbrowser.open_new_tab(REPO_URL)
        except:
            print("Exception opening browser")
            #TODO("Pop-up dialog for user")

    def _get_input(self, key_entry, id_entry):
        self.user_id_number = id_entry.get()
        print("Steam user ID: " + self.user_id_number)
        self.user_api_key = key_entry.get()
        print("Steam user API key: " + self.user_api_key)

        userInfoFile = UserFile(self.user_api_key, self.user_id_number)
        userInfoFile.create_user_file()

        try:
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.user_api_key + "&include_appinfo=true" + "&steamid=" + self.user_id_number + "&format=json")
            print(vars(ownedGamesReq))
            print(type(ownedGamesReq))
            ownedGamesRes = ownedGamesReq.json()
            print(type(ownedGamesRes))
            for item in ownedGamesRes["response"]["games"]:
                print(item["name"])
        except:
            print("Exception getting userr info from Steam")
            #TODO("Create pop-up for user")

        