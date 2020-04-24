from OAuth2BlizzABC import OAuth2BlizzABC
import logging as log
import os
import urllib.request
from Vars.Global import LOG_FILE_NAME, LOG_FORMAT, BLIZZ_BASE_URL, BLIZZ_TOKEN_URL
import requests

class OAuth2Blizz(OAuth2BlizzABC):

    #log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)
    
    def get_token(self):
        if self.is_token_invalid():
            log.debug("Is token invalid if block")
            self.client_credentials = os.getenv("BLIZZ_CLINET_ID") + os.getenv("BLIZZ_CLIENT_SECRET")

            if self._check_connection():
               blizz_req = requests.post(BLIZZ_TOKEN_URL, self.client_credentials)

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