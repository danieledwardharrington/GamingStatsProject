from .OAuth2BlizzABC import OAuth2BlizzABC
import logging as log
import os
import urllib.request
from ..Vars.Global import *
import requests
import json
from requests.auth import HTTPBasicAuth
from ..GameUser.UserImpl import UserImpl
from ..MiscDialog.ErrorDialog import ErrorDialog

class OAuth2Blizz(OAuth2BlizzABC):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, user):
        super().__init__()
        log.info("OAuth2Blizz init called")
        self.client_id = None
        self.client_secret = None
        self.region = user.region

    def get_token(self):
        if self._check_connection():
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
            return response
        else:
            log.error(NO_NETWORK)
            ErrorDialog(NO_NETWORK)
            return None

    @classmethod
    def _check_connection(cls):
        log.info("Checking internet connection")
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            log.info("Internet connection test successful")
            return True
        except Exception as e:
            log.error(e)
            log.info("Internet connection test failed")
            return False

