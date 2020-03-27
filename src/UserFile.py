from PopupWindow import *
from SteamUser import *
import pickle

class UserFile:

    user_api = ""
    user_id = ""

    def __init__(self, user_api = "", user_id = ""):
        self.user_api = user_api
        self.user_id = user_id

    def create_user_file(self):
        try:
            user = SteamUser(self.user_id, self.user_api)
            file_handler = open(USER_FILE_NAME, "w+")
            pickle.dump(user, file_handler)
            file_handler.close()
        except:
            print(USER_FILE_EXCEPTION)
            file_popup = PopupWindow(USER_FILE_POPUP)

    def create_library_file(self, game_list):
        try:
            file_handler = open(LIBRARY_FILE_NAME, "w+")
            pickle.dump(game_list, file_handler)
            file_handler.close()
        except:
            print(LIBRARY_FILE_EXCEPTION)
            library_popup = PopupWindow(LIBRARY_FILE_POPUP)