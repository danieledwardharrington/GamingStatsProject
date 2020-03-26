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


if not os.path.exists(USER_FILE_NAME) and not os.path.exists(LIBRARY_FILE_NAME):
    steamGUI = SteamInfoGUI()
else:
    libraryGUI = LibraryGUI()