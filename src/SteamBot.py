from Global import *
import os
from time import sleep
import bs4
import urllib.request
from Game import *

class SteamBot:

    def __init__(self, game):
        pass
        sauce = urllib.request.urlopen(STEAM_APP_URL + game.steam_app_id)