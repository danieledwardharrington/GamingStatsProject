# Program that gives detailed stats/ratings about a user's Steam library
# Author: Daniel Harrington

import requests
from os import *
import json
from SteamInfoGUI import *
from LibraryGUI import *
from Global import *
import multiprocessing


def main():
    #if the files don't exist for user info and the game library, we're taking the user to put
    #their info in again
    if not os.path.exists(USER_FILE_NAME) and not os.path.exists(LIBRARY_FILE_NAME):
        print("Loading steam info gui")
        app = QtWidgets.QApplication(sys.argv)
        master = QtWidgets.QMainWindow()
        master.setWindowIcon(QIcon("images/gspDesktop2.ico"))
        ui = SteamUI()
        ui.setup_Ui(master)
        master.show()
        sys.exit(app.exec_())
    else:
        print("Loading library gui")
        LibraryGUI()
        print("Library gui loaded")

if __name__ == '__main__':
    if sys.platform.startswith("win"):
        multiprocessing.freeze_support()
    main()