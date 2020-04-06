import os

#URL for GitHub repo, sending the user there for instructions on obtaining API key and SteamID64
REPO_URL = "https://github.com/danieledwardharrington/GamingStatsProject"

#URLs
STEAM_APP_URL = "https://store.steampowered.com/app/"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdZsLvup2XdG2JxSSInDUPRUxjP-2KcxSmKVMHRHgaTpwNbWA/viewform?usp=sf_link"

#Fonts
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

#Exception strings
BROWSER_EXCEPTION = "Exception opening browser"
BROWSER_POPUP = "Error opening browser"

NO_NETWORK = "No network connection"

STEAM_EXCEPTION = "Exception getting user information from Steam"
STEAM_POPUP = "Error getting your information from Steam"

USER_FILE_EXCEPTION = "Exception creating user file"
USER_FILE_POPUP = "Error saving user information"

LIBRARY_FILE_EXCEPTION = "Exception creating library file"
LIBRARY_FILE_POPUP = "Error saving game information"

LIBRARY_UI_EXCEPTION = "Exception loading library UI"

#FIle names
USER_FILE_NAME = "usr/userInfo.dat"
LIBRARY_FILE_NAME = "usr/userLibrary.dat"
WIN_ICON = "images/gspDesktop2.ico"