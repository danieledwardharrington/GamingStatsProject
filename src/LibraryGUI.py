from tkinter import *
from Global import *
from UserFile import *
from tkinter import ttk
import pickle
from EditGameWindow import *
import os
from SteamInfoGUI import *
import time
from LibrarySummary import *
import concurrent.futures


class LibraryGUI:

    game_list = []
    
    def __init__(self):
        root = tkinter.Tk()

        self._load_data()

        root.title("Gaming Stats - Library")
        root.geometry("600x600")
        root.iconbitmap("images/gspIconTransparent.ico")
        GSPmenu(root)

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

        update_library_button = Button(root, text = "Update library", font = NORM_FONT, width = 20, borderwidth = 5, command = lambda: self._update_library(root))
        update_library_button.pack()
        
        summary_button = Button(root, text = "Library summary", font = NORM_FONT, width = 20, borderwidth = 5, command = lambda: self._show_library_summary(self.game_list))
        summary_button.pack()

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
        confirm_popup = PopupWindow("Are you sure?", "delete_user", root)

    #modified version of the _get_input method from the SteamInfoGUI class so that the user's genre and rating changes remain intact
    def _update_library(self, root):

        pickle_in = open(USER_FILE_NAME, "rb")
        user = pickle.load(pickle_in)
        
        user_id_number = user.steam_user_id.strip()
        print("Steam user ID: " + user_id_number)
        user_api_key = user.steam_user_api.strip()
        print("Steam user API key: " + user_api_key)

        if self._check_connection():
            
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + user_api_key + "&include_appinfo=true" + "&steamid=" + user_id_number + "&format=json")
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

                name_list = []
                new_game_list = []
                print(type(game_list))
                for game in ownedGamesRes["response"]["games"]:
                    if game["playtime_forever"] > 0:
                        game_minutes = game["playtime_forever"]
                        game_name = game["name"]
                        game_app_id = game["appid"]
                        game_genre = ""
                        new_game = Game(game_name, game_genre, game_app_id, game_minutes)
                        for item in self.game_list:
                            name_list.append(item.name)
                        if game_name not in name_list: 
                            new_game_list.append(new_game)
                print("New game list done")

                with concurrent.futures.ProcessPoolExecutor() as executor:
                    result = executor.map(self._set_genre, new_game_list)
                result_list = list(result)
                for i  in result_list:
                    print(str(i))

                #basically just assigning the genres from the futures result to the actual games in the games_list
                for game in new_game_list:
                    for genre in result_list:
                        if game.name in genre:
                            game.genre = genre.replace(game.name, "")

                #Sorting the list alphabetically, omitting "the " or "The " from the beginning of titles
                updated_game_list = self.game_list + new_game_list   
                updated_game_list.sort(key = attrgetter("sort_name"), reverse = False)

                for game in game_list:
                    print(game.name)
                    print(game.steam_app_id)
                    print(game.genre)
                    
                user.create_library_file(updated_game_list)

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

    def _check_connection(self):
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            return True
        except Exception as e:
            print(e)
            return False

    def _show_library_summary(self, game_list):
        LibrarySummary(game_list)
