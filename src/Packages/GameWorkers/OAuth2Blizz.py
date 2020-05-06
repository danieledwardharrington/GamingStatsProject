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
import webbrowser

class OAuth2Blizz(OAuth2BlizzABC):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, user = UserImpl()):
        super().__init__()
        log.info("OAuth2Blizz init called")
        self.client_id = None
        self.client_secret = None
        self.region = user.blizz_region

    def get_auth_code(self):
        if self._check_connection():
            self.client_id = os.getenv("BLIZZ_CLIENT_ID")
            print(f"Client ID: {self.client_id}")
            self.client_secret = os.getenv("BLIZZ_CLIENT_SECRET")
            print(f"Client secret: {self.client_secret}")
            self.region = "us"
            state = "abcd1234"

            re = requests.get(f"{BLIZZ_AUTH_URL}?client_id={self.client_id}&response_type=code&redirect_uri={REPO_URL}&locale={self.region}&scope={SC2_SCOPE}&state={state}")

            headers = re.headers
            print("-------------------------------------------")
            print(f"HEADERS: {headers}")
            print("-------------------------------------------")

            re_url = re.url
            print(re_url)
            code = re_url.split("code=")[-1]
            print(f"Code print: {code}")
            return re
        return None

    def get_token(self):
        if self._check_connection():
            log.debug("Check connection if block")
            self.client_id = os.getenv("BLIZZ_CLIENT_ID")
            print(f"Client ID: {self.client_id}")
            self.client_secret = os.getenv("BLIZZ_CLIENT_SECRET")
            print(f"Client secret: {self.client_secret}")
            self.region = "us"
            state = "abcd1234"

            webbrowser.open_new_tab(f"{BLIZZ_AUTH_URL}?client_id={self.client_id}&response_type=code&redirect_uri={REPO_URL}&locale={self.region}&scope=sc2.profile&state={state}")

            url = f"https://{self.region}.battle.net/oauth/token"
            body = {"grant_type": 'authorization_code'}
            auth = HTTPBasicAuth(self.client_id, self.client_secret)

            response = requests.post(url, data = body, auth = auth)
            res_json = response.json()
            print(f"RESPONSE: {response}")
            print(f"RESPONSE JSON: {res_json}")
            return response
        
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

test = OAuth2Blizz()
test.get_auth_code()
