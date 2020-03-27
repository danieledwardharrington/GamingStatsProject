# Program that gives detailed stats/ratings about a user's Steam library
# Author: Daniel Harrington

import requests
from steamwebapi import profiles
from steamwebapi.api import ISteamUser, ISteamUserStats, IPlayerService
from os import *
import json
from SteamInfoGUI import SteamInfoGUI
from LibraryGUI import *
from Global import *

#if the files don't exist for user info and the game library, we're taking the user to put
#their info in again
if not os.path.exists(USER_FILE_NAME) and not os.path.exists(LIBRARY_FILE_NAME):
    steamGUI = SteamInfoGUI()
else:
    libraryGUI = LibraryGUI()