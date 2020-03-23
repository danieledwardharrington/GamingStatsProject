import requests
from steamwebapi import profiles
from steamwebapi.api import ISteamUser, ISteamUserStats, IPlayerService
import os

api_key = os.environ.get("STEAM_API_KEY")
steam_id = "76561198069544896"

req = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + api_key + "&include_appinfo=true" + "&steamid=" + steam_id + "&format=json")