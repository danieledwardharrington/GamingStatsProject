from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from SteamBot import *
import concurrent.futures

class SteamWorker(QObject):
    
    listed = QtCore.pyqtSignal(list)

    def steam_work(self, game_list):
        steam_bot = SteamBot()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            result = executor.map(steam_bot.set_genre, game_list)
            result_list = list(result)
        for i  in result_list:
            print(type(i))
            print(str(i))

        self.listed.emit(result_list)