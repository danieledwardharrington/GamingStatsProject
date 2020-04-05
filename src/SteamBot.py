from Global import *
import os
from time import sleep
import bs4
import urllib.request
from Game import *
import requests

class SteamBot:

    def __init__(self):
        print("Steam bot created")

    def set_genre(self, game):
        steam_cookies = {'birthtime': '283993201', 'mature_content': '1'}
        sauce = requests.get(STEAM_APP_URL + str(game.steam_app_id), cookies = steam_cookies)
        soup = bs4.BeautifulSoup(sauce.content, "lxml")

        genre = ""
        for a in soup.find_all("a", class_ = "app_tag"):
            if genre == "":
                genre = str(a.text.strip())
            else:
                genre = genre + ", " + str(a.text.strip())

        #I'm adding the name of the game to the beginning of the string here so that later, I can easily assign the genre to the actual game in the game_list
        return_str = game.name + genre
        return return_str