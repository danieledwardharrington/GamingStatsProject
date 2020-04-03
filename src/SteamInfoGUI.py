import tkinter
import webbrowser
import requests
import bs4
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
import concurrent.futures
import time
from GSPmenu import *

class SteamInfoGUI:

    user_api_key = ""
    user_id_number = ""

    def __init__(self):
        root = tkinter.Tk()

        root.title("Gaming Stats")
        root.iconbitmap("images/gspDesktop2.ico")
        root.geometry("1200x700")
        GSPmenu(root)

        key_label = Label(root, text = "Enter your Steam API key", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        key_label.grid(row = 0, column = 0)
        key_entry = Entry(root, width = 25, font = LARGE_FONT)
        key_entry.grid(row = 0, column = 1)
        id_label = Label(root, text = "Enter your SteamID64", font = LARGE_FONT, anchor = W, width = 25, pady = 10)
        id_label.grid(row = 1, column = 0)
        id_entry = Entry(root, width = 25, font = LARGE_FONT)
        id_entry.grid(row = 1, column = 1)
        wait_label = Label(root, text = "After clicking submit, please wait. It may take a few minutes.", font = LARGE_FONT, anchor = W, width = 50, pady = 10)
        wait_label.grid(row = 4, column = 1)
        disconnect_label = Label(root, text = "Do not close or disconnect from the network.", font = LARGE_FONT, anchor = W, width = 50, pady = 10)
        disconnect_label.grid(row = 5, column = 1)

        submit_button = Button(root, text = "SUBMIT", borderwidth = 5, width = 34, font = NORM_FONT, command = lambda: self._get_input(key_entry, id_entry, root))
        submit_button.grid(row = 2, column = 0)

        #This button forwards the user to the GitHub repo for more information
        instructions_button = Button(root, text = "Need API key/Don't know SteamID64?", borderwidth = 5, width = 34, font = NORM_FONT, command = self._send_to_repo)
        instructions_button.grid(row = 3, column = 0)

        #root.iconbitmap()
        print("Steam info gui loaded")
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
            
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.user_api_key + "&include_appinfo=true&include_played_free_games=true&steamid=" + self.user_id_number + "&format=json")
            print(type(ownedGamesReq))
            
            #checking for good response from Steam
            if(ownedGamesReq.status_code == 200):
                start = time.time()
                print("-----------------------------")
                print("Job start: " + str(start))
                print("-----------------------------")
                #if all good, starting everything and saving user info and library files
                print(vars(ownedGamesReq))
                print(type(ownedGamesReq))
                ownedGamesRes = ownedGamesReq.json()
                print(type(ownedGamesRes))

                game_list = []
                print(type(game_list))
                for game in ownedGamesRes["response"]["games"]:
                    if game["playtime_forever"] > 0:
                        game_minutes = game["playtime_forever"]
                        game_name = game["name"]
                        game_app_id = game["appid"]
                        game_genre = ""
                        new_game = Game(game_name, game_genre, game_app_id, game_minutes)
                        game_list.append(new_game)
                print("Game list done")
                print(type(game_list))

                with concurrent.futures.ProcessPoolExecutor() as executor:
                    result = executor.map(self._set_genre, game_list)
                result_list = list(result)
                for i  in result_list:
                    print(type(i))
                    print(str(i))

                #Sorting the list alphabetically, omitting "the " or "The " from the beginning of titles   
                game_list.sort(key = attrgetter("sort_name"), reverse = False)

                #basically just assigning the genres from the futures result to the actual games in the games_list
                for game in game_list:
                    for genre in result_list:
                        if game.name in genre:
                            game.genre = genre.replace(game.name, "")

                for game in game_list:
                    print(game.name)
                    print(game.steam_app_id)
                    print(game.genre)

                #saving user files once everything has been done successfully
                userInfoFile = UserFile(self.user_api_key, self.user_id_number)
                userInfoFile.create_user_file()
                    
                userInfoFile.create_library_file(game_list)

                root.destroy()

                print("-----------------------------")
                end = time.time()
                print("Job end: " + str(end))
                print("Job took: " + str(end - start))
                print("-----------------------------")

                LibraryGUI()

            else:
                steam_popup = PopupWindow(STEAM_POPUP)
                print(STEAM_EXCEPTION)
        else:
            print(NO_NETWORK)
            network_popup = PopupWindow(NO_NETWORK)

    def _set_genre(self, game):
        steam_cookies = {'birthtime': '283993201', 'mature_content': '1'}
        sauce = requests.get(STEAM_APP_URL + str(game.steam_app_id), cookies = steam_cookies)
        soup = bs4.BeautifulSoup(sauce.content, "lxml")

        genre = ""
        for a in soup.find_all("a", class_ = "app_tag"):
            if genre == "":
                genre = str(a.text.strip())
            else:
                genre = genre + ", " + str(a.text.strip())

        #I'm adding the name of the game to the beginning of the string here so that later, I can easily assign the genre to the actual game in the game_list
        return_str = game.name + genre
        return return_str
