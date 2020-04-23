import logging as log
from . import UserABC
from ..Vars.Global import LOG_FILE_NAME, LOG_FORMAT

class SteamUser(UserABC):
    
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    steam_user_id = ""
    steam_user_api = ""

    def __init__(self, user_id = "", user_api = ""):
        log.info("Steam user init called")
        self.steam_user_api = user_api
        self.steam_user_id = user_id