import os

# URL for GitHub repo, sending the user there for instructions on obtaining API key and SteamID64
REPO_URL = "https://github.com/danieledwardharrington/GamingStatsProject"

# URLs
STEAM_APP_URL = "https://store.steampowered.com/app/"

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdZsLvup2XdG2JxSSInDUPRUxjP-2KcxSmKVMHRHgaTpwNbWA/viewform?usp=sf_link"
GOOGLE_FORM_URL_STYLED = "<html><head/><body><p><a href=https://docs.google.com/forms/d/e/1FAIpQLSdZsLvup2XdG2JxSSInDUPRUxjP-2KcxSmKVMHRHgaTpwNbWA/viewform?usp=sf_link <span style=\" text-decoration: underline; color:#0000ff;\">Have feedback? Click here</span></p></a></body></html>"

BLIZZ_BASE_URL = "https://us.api.blizzard.com"
BLIZZ_TOKEN_URL = "https://us.battle.net/oauth/token"
BLIZZ_AUTH_URL = "https://us.battle.net/oauth/authorize"

# Fonts
FONT_NAME = "Segoe UI"
XSMALL_FONT_POINT = 8
SMALL_FONT_POINT = 10
NORM_FONT_POINT = 12
LARGE_FONT_POINT = 14
XLARGE_FONT_POINT = 16
XLARGE_FONT = ("Segoe UI", 16)
LARGE_FONT = ("Segoe UI", 14)
NORM_FONT = ("Segoe UI", 12)
SMALL_FONT = ("Segoe UI", 10)
XSMALL_FONT = ("Segoe UI", 8)

# Exception strings
BROWSER_EXCEPTION = "Exception opening browser"
BROWSER_POPUP = "Error opening browser"

DELETE_USER_EXCEPTION = "Exception loading delete user dialog."
DELETE_USER_POPUP = "Error loading delete user confirmation."

NO_NETWORK = "No network connection"

STEAM_EXCEPTION = "Exception getting user information from Steam"
STEAM_POPUP = "Error getting your information from Steam"

USER_FILE_EXCEPTION = "Exception creating user file"
USER_FILE_POPUP = "Error saving user information"

LIBRARY_FILE_EXCEPTION = "Exception creating library file"
LIBRARY_FILE_POPUP = "Error saving game information"

LIBRARY_UI_EXCEPTION = "Exception loading library UI"
LIBRARY_UI_POPUP = "Error loading library window"

SUMMARY_EXCEPTION = "Exception compiling library summary"
SUMMARY_POPUP = "Error loading library summary"

EDIT_EXCEPTION = "Exception loading edit game window"
EDIT_POPUP = "Error loading edit game window"

STEAM_UI_EXCEPTION = "Exception opening SteamUI"
STEAM_UI_POPUP = "Error loading Steam information window"

UNKNOWN_EXCEPTION = "Unknown exception"
UNKNOWN_POPUP = "Unknown error"

ERROR_TITLE = "Error!"

NO_GAME_EXCEPTION = "No game selected."
NO_GAME_POPUP = "No game selected. Click the game name and try again."

# FIle names
USER_FILE_NAME = "usr/steamUserInfo.dat"
LIBRARY_FILE_NAME = "usr/steamUserLibrary.dat"

BLIZZ_USER_FILE_NAME = "usr/blizzUserInfo.dat"

WIN_ICON = "images/gspDesktop2.ico"
LOG_FILE_NAME = "log/gspLog.log"

# Log format
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"

# About string
ABOUT_STRING = "This app was developed using the Steam Web API. The genres for all games are scraped from each game\'s respective Steam page (genre will be blank if the game is no longer on Steam). Only games that have been played for at least one minute are included. All ratings are set to 0.0 until changed by the user and are rounded to nearest tenth."
                