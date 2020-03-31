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
from Game import *
from operator import attrgetter
from LibraryGUI import *
from SteamBot import *
import threading

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

        submit_button = Button(root, text = "SUBMIT", borderwidth = 5, width = 34, font = NORM_FONT, command = lambda: self._get_input(key_entry, id_entry, root))
        submit_button.grid(row = 2, column = 0)

        #This button forwards the user to the GitHub repo for more information
        instructions_button = Button(root, text = "Need API key/Don't know SteamID64?", borderwidth = 5, width = 34, font = NORM_FONT, command = self._send_to_repo)
        instructions_button.grid(row = 3, column = 0)

        #root.iconbitmap()
        root.mainloop()

    def _send_to_repo(self):
        try:
            webbrowser.open_new_tab(REPO_URL)
        except Exception as e:
            browser_popup = PopupWindow(BROWSER_POPUP)
            print(BROWSER_EXCEPTION)
            print(e)

    def _check_connection(self):
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            return True
        except Exception as e:
            print(e)
            return False

    def _get_input(self, key_entry, id_entry, root):
        
        self.user_id_number = id_entry.get().strip()
        print("Steam user ID: " + self.user_id_number)
        self.user_api_key = key_entry.get().strip()
        print("Steam user API key: " + self.user_api_key)

        if self._check_connection():
            
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + api_key + "&include_appinfo=true" + "&steamid=" + steam_id + "&format=json")
            print(type(ownedGamesReq))
            
            #checking for good response from Steam
            if(ownedGamesReq.status_code == 200):

                #if all good, starting everything and saving user info and library files
                print(vars(ownedGamesReq))
                print(type(ownedGamesReq))
                ownedGamesRes = ownedGamesReq.json()
                print(type(ownedGamesRes))

                game_list = []

                # #getting list of game names
                for item in ownedGamesRes["response"]["games"]:
                    game_minutes = item["playtime_forever"]

                    #only adding to the list if the user has actually played the game
                    if game_minutes > 0:
                        game_name = item["name"]
                        game_app_id = item["appid"]
                        game_genre = ""

                        game = Game(game_name, game_genre, game_app_id, game_minutes)

                        self._set_genre(game) #scraping this from Steam

                        #only adding to the list if the user has actually played the game
                        if game_minutes > 0:
                            game_list.append(game)

                            print(game.name)
                            print(game.steam_app_id)
                            print(game.genre)

                game_list.sort(key = attrgetter("sort_name"), reverse = False)

                #saving user files once everything has been done successfully
                userInfoFile = UserFile(self.user_api_key, self.user_id_number)
                userInfoFile.create_user_file()
                    
                userInfoFile.create_library_file(game_list)

                root.destroy()

                LibraryGUI()
            else:
                steam_popup = PopupWindow(STEAM_POPUP)
                print(STEAM_EXCEPTION)
        else:
            print(NO_NETWORK)
            network_popup = PopupWindow(NO_NETWORK)

    def _set_genre(self, game):
        steam_scraper = SteamBot(game)

    def _get_steam_game_info(self, game_list, ownedGamesRes):
        for item in ownedGamesRes["response"]["games"]:
            game_name = item["name"]
            game_minutes = item["playtime_forever"]
            game_app_id = item["appid"]
            game_genre = ""

            game = Game(game_name, game_genre, game_app_id, game_minutes)

            self._set_genre(game) #scraping this from Steam

            #only adding to the list if the user has actually played the game
            if game_minutes > 0:
                game_list.append(game)

                print(game.name)
                print(game.steam_app_id)
                print(game.genre)
