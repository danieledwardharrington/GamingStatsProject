class UserFile:

    user_api = ""
    user_id = ""

    def __init__(self, user_api, user_id):
        self.user_api = user_api
        self.user_id = user_id

    def create_user_file(self):
        try:
            with open("userFile.txt", "w") as file_handler:
                file_handler.write(self.user_api + "\n")
                file_handler.write(self.user_id)
                print("File created")
                print("Data written")
        except:
            print("Error creating file")
            #TODO("Add pop-up for user")