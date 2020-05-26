from .OAuth2BlizzABC import OAuth2BlizzABC
import logging as log
import os
import urllib.request
from ..Vars.Global import *
import requests
import json
from requests.auth import HTTPBasicAuth
from ..GameUser.UserImpl import UserImpl
#from ..MiscDialog.ErrorDialog import ErrorDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5 import QtWidgets
import sys

class FinalMeta(type(OAuth2BlizzABC), type(QObject)):
    pass

class OAuth2Blizz(OAuth2BlizzABC, QObject, metaclass=FinalMeta):

    #log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    changed_url = None

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
            
            app = QtWidgets.QApplication(sys.argv)
            web = QWebEngineView()
            web.urlChanged.connect(self._set_new_url)
            web.load(QUrl(f"{BLIZZ_AUTH_URL}?client_id={self.client_id}&response_type=code&redirect_uri={REPO_URL}&locale={self.region}&scope=sc2.profile&state={state}"))
            web.show()

            re_url = web.url()

            print("***************************************")
            print("***************************************")
            print("***************************************")
            print(self.changed_url)
            print("***************************************")
            print("***************************************")
            print("***************************************")
            sys.exit(app.exec_())
            code = re_url.split("code=")[-1]
            print(f"Code print: {code}")
            return re_url
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

            web = QWebEngineView()
            web.load(QUrl(f"{BLIZZ_AUTH_URL}?client_id={self.client_id}&response_type=code&redirect_uri={REPO_URL}&locale={self.region}&scope=sc2.profile&state={state}"))

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

    def _set_new_url(self, new_url):
        self.changed_url = new_url
        print(f"QUrl: {self.changed_url}")
        human_url = self.changed_url.toDisplayString()
        print(f"Human URL: {human_url}")

test = OAuth2Blizz()
test.get_auth_code()
