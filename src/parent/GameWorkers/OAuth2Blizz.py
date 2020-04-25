from .OAuth2BlizzABC import OAuth2BlizzABC
import logging as log
import os
import urllib.request
from ..Vars.Global import LOG_FILE_NAME, LOG_FORMAT, BLIZZ_BASE_URL, BLIZZ_TOKEN_URL
import requests
import json
import requests
from requests.auth import HTTPBasicAuth
from ..GameUser import BlizzardUser

class OAuth2Blizz(OAuth2BlizzABC):

    # log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def get_token(self):
        if self.is_token_invalid():
            #will need to pickle load for blizzard user here
            log.debug("Is token invalid if block")
            self.client_id = os.environ("BLIZZ_CLIENT_ID")
            self.client_secret = os.environ("BLIZZ_CLIENT_SECRET")
            url = "https://%s.battle.net/oauth/token" % region
            body = {"grant_type": 'client_credentials'}
            auth = HTTPBasicAuth(self.client_id, self.client_secret)

            response = requests.post(url, data=body, auth=auth)
            response_json = response.json

    def is_token_invalid(self):
        pass

    def _check_connection(self):
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            return True
        except Exception as e:
            log.error(e)
            return False
