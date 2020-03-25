import requests
from steamwebapi import profiles
from steamwebapi.api import ISteamUser, ISteamUserStats, IPlayerService
import os
import json
from AppGUI import AppGUI
from Global import *



api_key = os.environ.get("STEAM_API_KEY")
steam_id = "76561198069544896"

app = AppGUI()
ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + USER_API_KEY + "&include_appinfo=true" + "&steamid=" + USER_STEAM_ID + "&format=json")
print(ownedGamesReq)
#ownedGamesJsonObj = json.loads(ownedGamesReq)