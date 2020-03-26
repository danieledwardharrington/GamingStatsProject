from PopupWindow import *

import pickle

class UserFile:

    user_api = ""
    user_id = ""

    def __init__(self, user_api, user_id):
        self.user_api = user_api
        self.user_id = user_id

    def create_user_file(self):
        try:
            file_handler = open(USER_FILE_NAME, "w+")
            file_handler.write(self.user_api + "\n")
            file_handler.write(self.user_id)
            file_handler.close()
        except:
            print(USER_FILE_EXCEPTION)
            file_popup = PopupWindow(USER_FILE_POPUP)

    def create_library_file(self, gameList):
        try:
            file_handler = open(LIBRARY_FILE_NAME, "w+")
            pickle.dump(gameList, file_handler)
            file_handler.close()
        except:
            print(LIBRARY_FILE_EXCEPTION)
            library_popup = PopupWindow(LIBRARY_FILE_POPUP)