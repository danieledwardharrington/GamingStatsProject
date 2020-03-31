from Global import *
import os
from time import sleep
import bs4
import urllib.request
from Game import *
import requests

class SteamBot:

    def __init__(self, game):
        steam_cookies = {'birthtime': '283993201', 'mature_content': '1'}
        sauce = requests.get(STEAM_APP_URL + str(game.steam_app_id), cookies = steam_cookies)
        soup = bs4.BeautifulSoup(sauce.text, "lxml")

        for a in soup.find_all("a", class_ = "app_tag"):
            if game.genre == "":
                game.genre = str(a.text.strip())
            else:
                game.genre = game.genre + ", " + str(a.text.strip())