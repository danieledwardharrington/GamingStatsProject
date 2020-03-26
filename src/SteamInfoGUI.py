import webbrowser
import tkinter
import requests
import json
import os
import urllib.request
from tkinter import *
from tkinter import ttk
from Global import *
from UserFile import *
from PopupWindow import *

class SteamInfoGUI:

    user_api_key = ""
    user_id_number = ""

    def __init__(self):
        root = tkinter.Tk()

        root.title("Gaming Stats")
        root.geometry("1200x700")

        key_label = Label(root, text = "Enter your Steam API key", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        key_label.grid(row = 0, column = 0)
        key_entry = Entry(root, width = 25, font = LARGE_FONT)
        key_entry.grid(row = 0, column = 1)
        id_label = Label(root, text = "Enter your SteamID64", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        id_label.grid(row = 1, column = 0)
        id_entry = Entry(root, width = 25, font = LARGE_FONT)
        id_entry.grid(row = 1, column = 1)

        submit_button = Button(root, text = "SUBMIT", borderwidth = 5, width = 34, font = NORM_FONT, command = lambda:  self._get_input(key_entry, id_entry))
        submit_button.grid(row = 2, column = 0)

        instructions_button = Button(root, text = "Need API key/Don't know SteamID64?", borderwidth = 5, width = 34, font = NORM_FONT, command = self._send_to_repo)
        instructions_button.grid(row = 3, column = 0)

        #root.iconbitmap()
        root.mainloop()

    # def _make_popup(self, message = "Error"):
    #     win = tkinter.Toplevel()
    #     win.wm_title("Alert!")
    #     win.geometry("200x100")

    #     label = tkinter.Label(win, text = message)
    #     label.pack(side = "top", fill = "x", pady = 10)

    #     okay_button = ttk.Button(win, text = "Okay", command = win.destroy)
    #     okay_button.pack()

    def _send_to_repo(self):
        try:
            webbrowser.open_new_tab(REPO_URL)
        except:
            browser_popup = PopupWindow(BROWSER_POPUP)
            print(BROWSER_EXCEPTION)

    def _check_connection(self):
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False

    def _get_input(self, key_entry, id_entry):
        
        self.user_id_number = id_entry.get().strip()
        print("Steam user ID: " + self.user_id_number)
        self.user_api_key = key_entry.get().strip()
        print("Steam user API key: " + self.user_api_key)

        if self._check_connection():
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + api_key + "&include_appinfo=true" + "&steamid=" + steam_id + "&format=json")
            print(type(ownedGamesReq))
            
            #checking for good response from Steam
            if(ownedGamesReq.status_code == 200):
                
                #if all good, saving user info to txt file
                userInfoFile = UserFile(self.user_api_key, self.user_id_number)
                userInfoFile.create_user_file()
                
                print(vars(ownedGamesReq))
                print(type(ownedGamesReq))
                ownedGamesRes = ownedGamesReq.json()
                print(type(ownedGamesRes))
                
                #getting list of game names
                for item in ownedGamesRes["response"]["games"]:
                    print(item["name"])
            else:
                steam_popup = PopupWindow(STEAM_POPUP)
                print(STEAM_EXCEPTION)
        else:
            print(NO_NETWORK)
            network_popup = PopupWindow(NO_NETWORK)
    
