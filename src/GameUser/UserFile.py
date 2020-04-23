from . import SteamUser
from ..Vars.Global import *
import pickle
import logging as log

class UserFile:

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    steam_user = SteamUser()

    def __init__(self, steam_user = SteamUser()):
        log.info("Steam user init called")
        self.steam_user = steam_user

    def create_user_file(self):
        log.info("Create user file called")
        try:
            log.debug("Trying to create user file")
            file_handler = open(USER_FILE_NAME, "wb")
            pickle.dump(self.steam_user, file_handler)
            file_handler.close()
            log.debug("User file creation succeeded")
        except Exception as e:
            log.error(USER_FILE_EXCEPTION)
            log.error(e)

    def create_library_file(self, game_list):
        log.info("Create library file called")
        try:
            log.debug("Trying to create library file")
            file_handler = open(LIBRARY_FILE_NAME, "wb")
            pickle.dump(game_list, file_handler)
            file_handler.close()
            log.debug("Library file creation succeeded")
        except Exception as e:
            log.error(LIBRARY_FILE_EXCEPTION)
            log.error(e)