from .OAuth2BlizzABC import OAuth2BlizzABC
import logging as log
import os
import urllib.request
from ..Vars.Global import LOG_FILE_NAME, LOG_FORMAT, BLIZZ_BASE_URL, BLIZZ_TOKEN_URL
import requests
import json
from requests.auth import HTTPBasicAuth
from ..GameUser.BlizzardUser import BlizzardUser

class OAuth2Blizz(OAuth2BlizzABC):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self):
        super().__init__()
        log.info("OAuth2Blizz init called")
        self.client_id = None
        self.client_secret = None
        self.region = None

    def get_token(self):
        if self._check_connection():
            #will need to pickle load for blizzard user here
            log.debug("Check connection if block")
            self.client_id = os.getenv("BLIZZ_CLIENT_ID")
            print(f"Client ID: {self.client_id}")
            self.client_secret = os.getenv("BLIZZ_CLIENT_SECRET")
            print(f"Client secret: {self.client_secret}")
            self.region = "us"
            url = f"https://{self.region}.battle.net/oauth/token"
            body = {"grant_type": 'client_credentials'}
            auth = HTTPBasicAuth(self.client_id, self.client_secret)

            response = requests.post(url, data = body, auth = auth)
            response_json = response.json
            print(f"reponse_json: {response_json}")

    def _check_connection(self):
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            return True
        except Exception as e:
            log.error(e)
            return False

test = OAuth2Blizz()
test.get_token()
