import os

#URL for GitHub repo, sending the user there for instructions on obtaining API key and SteamID64
REPO_URL = "https://github.com/danieledwardharrington/GamingStatsProject"

#URL for Steam
STEAM_APP_URL = "https://store.steampowered.com/app/"
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdZsLvup2XdG2JxSSInDUPRUxjP-2KcxSmKVMHRHgaTpwNbWA/viewform?usp=sf_link"

#Fonts
XLARGE_FONT = ("Helvetica", 16)
LARGE_FONT = ("Helvetica", 14)
NORM_FONT = ("Helvetica", 12)
SMALL_FONT = ("Helvetica", 10)
XSMALL_FONT = ("Helvetica", 8)

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

#Stuff for Steam
STEAM_SEARCH_BOX_XPATH = "/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[9]/div[1]/form/div/input"
STEAM_SEARCH_BUTTON_XPATH = "/html/body/div[1]/div[7]/div[4]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[9]/div[1]/form/div/a"

#FIle names
USER_FILE_NAME = "usr/userInfo.dat"
LIBRARY_FILE_NAME = "usr/userLibrary.dat"