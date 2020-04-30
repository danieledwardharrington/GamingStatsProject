from .UserABC import UserABC
import logging as log
from ..Vars.Global import LOG_FILE_NAME, LOG_FORMAT

class BlizzardUser(UserABC):
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, real_id, region, selected_games):
        log.info("BlizzardUser init called")
        super().__init__()
        self.real_id = real_id
        self.region = region
        self.selected_games = selected_games
