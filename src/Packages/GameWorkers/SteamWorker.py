from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from .SteamBot import SteamBot
import concurrent.futures
import logging as log
from ..Vars.Global import *

class SteamWorker(QObject):
    
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    listed = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal(bool)
    ready = QtCore.pyqtSignal(bool)
    increment = QtCore.pyqtSignal(bool)
    result_list = []

    def steam_work(self, game_list):
        log.info("steam_work called")
        self.ready.emit(True)
        log.debug("Steam work true emit")
        steam_bot = SteamBot()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for result in executor.map(steam_bot.set_genre, game_list):
                self.result_list.append(result)
                self.increment.emit(True)
        for i in self.result_list:
            log.debug(type(i))
            log.debug(str(i))

        self.listed.emit(self.result_list)
        self.finished.emit(True)