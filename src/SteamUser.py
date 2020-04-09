import logging as log

class SteamUser:

    log.basicConfig(level = log.DEBUG)

    steam_user_id = ""
    steam_user_api = ""

    def __init__(self, user_id = "", user_api = ""):
        self.steam_user_api = user_api
        self.steam_user_id = user_id