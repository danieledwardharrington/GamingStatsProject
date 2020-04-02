# Program that gives detailed stats/ratings about a user's Steam library
# Author: Daniel Harrington

import requests
from os import *
import json
from SteamInfoGUI import *
from LibraryGUI import *
from Global import *


def main():
    #if the files don't exist for user info and the game library, we're taking the user to put
    #their info in again
    if not os.path.exists(USER_FILE_NAME) and not os.path.exists(LIBRARY_FILE_NAME):
        print("Loading steam info gui")
        SteamInfoGUI()
        print("Steam info gui loaded")
    else:
        print("Loading library gui")
        LibraryGUI()
        print("Library gui loaded")

if __name__ == '__main__':
    main()