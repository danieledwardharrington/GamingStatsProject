from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from SteamBot import *
import concurrent.futures
import logging as log

class SteamWorker(QObject):
    
    log.basicConfig(level = log.DEBUG)

    listed = QtCore.pyqtSignal(list)
    finished = QtCore.pyqtSignal(bool)
    ready = QtCore.pyqtSignal(bool)
    increment = QtCore.pyqtSignal(bool)
    steam_bot = SteamBot()
    result_list = []

    def steam_work(self, game_list):
        self.ready.emit(True)
        print("Steam work true emit")
        self.steam_bot = SteamBot()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            for result in executor.map(self.steam_bot.set_genre, game_list):
                self.result_list.append(result)
                self.increment.emit(True)
        for i in self.result_list:
            print(type(i))
            print(str(i))

        self.listed.emit(self.result_list)
        self.finished.emit(True)