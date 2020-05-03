import logging as log
from .UserABC import UserABC
from ..Vars.Global import LOG_FILE_NAME, LOG_FORMAT

class UserImpl(UserABC):
    
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self):
        log.info("Steam user init called")

    def set_steam_info(self, user_id, user_api):
        self.steam_id = user_id
        self.steam_api_key = user_api

    def set_blizz_info(self, real_id, region, games):
        self.blizz_real_id = real_id
        self.blizz_region = region
        self.blizz_games = games