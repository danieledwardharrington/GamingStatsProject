from SteamUser import *
from Global import *
import pickle

class UserFile:

    steam_user = SteamUser()

    def __init__(self, steam_user = SteamUser()):
        self.steam_user = steam_user

    def create_user_file(self):
        try:
            file_handler = open(USER_FILE_NAME, "wb")
            pickle.dump(self.steam_user, file_handler)
            file_handler.close()
        except Exception as e:
            print(USER_FILE_EXCEPTION)
            print(e)

    def create_library_file(self, game_list):
        try:
            file_handler = open(LIBRARY_FILE_NAME, "wb")
            pickle.dump(game_list, file_handler)
            file_handler.close()
        except Exception as e:
            print(LIBRARY_FILE_EXCEPTION)
            print(e)