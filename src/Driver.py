import requests
from steamwebapi import profiles
from steamwebapi.api import ISteamUser, ISteamUserStats, IPlayerService
from os import *
import json
from SteamInfoGUI import SteamInfoGUI
from LibraryGUI import *
from Global import *


if not os.path.exists("userInfo.txt"):
    steamGUI = SteamInfoGUI()
else:
    libraryGUI = LibraryGUI()