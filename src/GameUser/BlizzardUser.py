import GameUser.UserABC
import logging as log
from Global import LOG_FILE_NAME, LOG_FORMAT

class BlizzardUser(UserABC):
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, real_id):
        super().__init__()
        self.real_id = real_id
