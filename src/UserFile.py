from PopupWindow import *

class UserFile:

    user_api = ""
    user_id = ""

    def __init__(self, user_api, user_id):
        self.user_api = user_api
        self.user_id = user_id

    def create_user_file(self):
        try:
            file_handler = open("userFile.txt", "w+")
            file_handler.write(self.user_api + "\n")
            file_handler.write(self.user_id)
            file_handler.close()
        except:
            print("Error creating file")
            file_popup = PopupWindow(FILE_POPUP)