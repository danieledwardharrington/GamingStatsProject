from Global import *
import os
from time import sleep
import bs4
import urllib.request
from Game import *
import requests
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
import logging as log

class SteamBot:

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self):
        log.info("Steam bot created")

    def set_genre(self, game):
        steam_cookies = {'birthtime': '283993201', 'mature_content': '1'}
        sauce = requests.get(STEAM_APP_URL + str(game.steam_app_id), cookies = steam_cookies)
        soup = bs4.BeautifulSoup(sauce.content, "lxml")
        log.info("Steam bot set genre")
        genre = ""
        for a in soup.find_all("a", class_ = "app_tag"):
            if genre == "":
                genre = str(a.text.strip())
            else:
                genre = genre + ", " + str(a.text.strip())

        #I'm adding the unique app ID of the game to the beginning of the string here so that later, I can easily assign the genre to the actual game in the game_list
        return_str = str(game.steam_app_id) + genre
        log.info("Return string: " + return_str)
        return return_str