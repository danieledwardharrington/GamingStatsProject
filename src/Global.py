import os

#URL for GitHub repo, sending the user there for instructions on obtaining API key and SteamID64
REPO_URL = "https://github.com/danieledwardharrington/GamingStatsProject"

#My info for testing
api_key = os.environ.get("STEAM_API_KEY")
steam_id = "76561198069544896"

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

FILE_EXCEPTION = "Exception creating file"
FILE_POPUP = "Error saving user information"