from PyQt5 import QtCore, QtGui, QtWidgets
from Global import *
import webbrowser
from SteamUser import *
import time
import urllib.request
from Game import *
from UserFile import *
from SteamBot import *
from LibraryUI import *
import concurrent.futures
from operator import attrgetter
import sys
from AboutUI import *
from SteamWorker import *
from LoadingDialog import *
from SteamWorker import *
import logging as log

class SteamUI(QObject):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)
    
    result_list = []
    game_list = []
    steam_user = SteamUser()

    genres_requested = QtCore.pyqtSignal(list)
    increment_request = QtCore.pyqtSignal(bool)
    increment_amount = QtCore.pyqtSignal(float)
    last_increment_request = QtCore.pyqtSignal(bool)

    def __init__(self, master):
        super().__init__()
        log.info("SteamUI init called")
        self.master = master
        self.steam_worker = SteamWorker()
        self.steam_thread = QtCore.QThread()
        self.steam_worker.moveToThread(self.steam_thread)
        self.steam_thread.start()
        self.setup_Ui(self.master, self.steam_worker)
        self.steam_worker.increment.connect(self._request_progress)
        self.loading_dialog = LoadingDialog()
        self.loading_thread = QtCore.QThread()
        self.loading_dialog.moveToThread(self.loading_thread)
        self.last_increment_request.connect(self.loading_dialog.last_increment)
        self.loading_thread.start()

    def setup_Ui(self, master, steam_worker):
        master.setObjectName("master")
        master.resize(600, 500)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        master.setFont(font)
        self.centralwidget = QtWidgets.QWidget(master)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_vert_layout = QtWidgets.QVBoxLayout()
        self.label_vert_layout.setObjectName("label_vert_layout")
        self.steam_id_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steam_id_label.sizePolicy().hasHeightForWidth())
        self.steam_id_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.steam_id_label.setFont(font)
        self.steam_id_label.setObjectName("steam_id_label")
        self.label_vert_layout.addWidget(self.steam_id_label)
        self.steam_api_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.steam_api_label.sizePolicy().hasHeightForWidth())
        self.steam_api_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.steam_api_label.setFont(font)
        self.steam_api_label.setScaledContents(False)
        self.steam_api_label.setObjectName("steam_api_label")
        self.label_vert_layout.addWidget(self.steam_api_label)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.label_vert_layout)
        self.entry_vert_layout = QtWidgets.QVBoxLayout()
        self.entry_vert_layout.setObjectName("entry_vert_layout")
        self.api_key_entry = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.api_key_entry.sizePolicy().hasHeightForWidth())
        self.api_key_entry.setSizePolicy(sizePolicy)
        self.api_key_entry.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.api_key_entry.setFont(font)
        self.api_key_entry.setObjectName("api_key_entry")
        self.entry_vert_layout.addWidget(self.api_key_entry)
        self.steam_id_entry = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.api_key_entry.sizePolicy().hasHeightForWidth())
        self.steam_id_entry.setSizePolicy(sizePolicy)
        self.steam_id_entry.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.steam_id_entry.setFont(font)
        self.steam_id_entry.setObjectName("steam_id_entry")
        self.entry_vert_layout.addWidget(self.steam_id_entry)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.entry_vert_layout)
        self.button_horz_layout = QtWidgets.QHBoxLayout()
        self.button_horz_layout.setObjectName("button_horz_layout")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)
        self.submit_button.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(XSMALL_FONT_POINT)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(lambda: self._get_input(self.api_key_entry, self.steam_id_entry, master, steam_worker))
        self.button_horz_layout.addWidget(self.submit_button)
        self.repo_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repo_button.sizePolicy().hasHeightForWidth())
        self.repo_button.setSizePolicy(sizePolicy)
        self.repo_button.setMinimumSize(QtCore.QSize(0, 0))
        self.repo_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.repo_button.clicked.connect(lambda: self._send_to_repo())
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.repo_button.setFont(font)
        self.repo_button.setObjectName("repo_button")
        self.button_horz_layout.addWidget(self.repo_button)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.button_horz_layout)
        master.setCentralWidget(self.centralwidget)
        self.main_menubar = QtWidgets.QMenuBar(master)
        self.main_menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.main_menubar.setObjectName("main_menubar")
        self.menu_file = QtWidgets.QMenu(self.main_menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.main_menubar)
        self.menu_help.setObjectName("menu_help")
        master.setMenuBar(self.main_menubar)
        self.statusbar = QtWidgets.QStatusBar(master)
        self.statusbar.setObjectName("statusbar")
        master.setStatusBar(self.statusbar)
        self.action_exit = QtWidgets.QAction(master)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.setShortcut("Ctrl+Q")
        self.action_exit.setStatusTip("Exit the app")
        self.action_exit.triggered.connect(lambda: sys.exit())
        self.action_about = QtWidgets.QAction(master)
        self.action_about.setObjectName("action_about")
        self.action_about.triggered.connect(lambda: AboutUI())
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.main_menubar.addAction(self.menu_file.menuAction())
        self.main_menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(master)
        QtCore.QMetaObject.connectSlotsByName(master)

        print("SteamUI loaded")

    def retranslateUi(self, master):
        _translate = QtCore.QCoreApplication.translate
        master.setWindowTitle(_translate("master", "Gaming Stats Project - Steam User Info"))
        self.steam_id_label.setText(_translate("master", "Steam API Key"))
        self.steam_api_label.setText(_translate("master", "SteamID64 Number"))
        self.submit_button.setToolTip(_translate("master", "<html><head/><body><p>Submit info</p></body></html>"))
        self.submit_button.setText(_translate("master", "Submit"))
        self.repo_button.setToolTip(_translate("master", "<html><head/><body><p>Visit repo</p></body></html>"))
        self.repo_button.setText(_translate("master", "Questions? Visit the repo"))
        self.menu_file.setTitle(_translate("master", "File"))
        self.menu_help.setTitle(_translate("master", "Help"))
        self.action_exit.setText(_translate("master", "Exit"))
        self.action_about.setText(_translate("master", "About"))


    def _send_to_repo(self):
        try:
            webbrowser.open_new_tab(REPO_URL)
        except Exception as e:
            print(BROWSER_EXCEPTION)
            print(e)

    def _get_input(self, key_entry, id_entry, root, steam_worker):
        log.info("Get info called")
        self.submit_button.setEnabled(False)
        self.statusbar.showMessage("Please wait...", 6000)

        steam_worker.listed.connect(self._result_to_list)
        steam_worker.finished.connect(self._on_finished)
        steam_worker.ready.connect(self._show_loading)
        self.genres_requested.connect(steam_worker.steam_work)
        self.increment_amount.connect(self.loading_dialog.set_increments)
        self.increment_request.connect(self.loading_dialog.increment_bar)

        user_id_number = id_entry.text().strip()
        user_api_key = key_entry.text().strip()

        self.steam_user = SteamUser(user_id_number, user_api_key)
        log.info("Steam user ID: " + user_id_number)
        log.info("Steam user API key: " + user_api_key)

        if self._check_connection():
            
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.steam_user.steam_user_api + "&include_appinfo=true&include_played_free_games=true&steamid=" + self.steam_user.steam_user_id + "&format=json")
            
            #checking for good response from Steam
            if(ownedGamesReq.status_code == 200):
                self.start = time.time()
                print("-----------------------------")
                print("Job start: " + str(self.start))
                log.info("Job start: " + str(self.start))
                print("-----------------------------")
                #if all good, starting everything and saving user info and library files
                log.info(vars(ownedGamesReq))
                ownedGamesRes = ownedGamesReq.json()

                for game in ownedGamesRes["response"]["games"]:
                    if game["playtime_forever"] > 0:
                        game_minutes = game["playtime_forever"]
                        game_name = game["name"]
                        game_app_id = game["appid"]
                        game_genre = ""
                        new_game = Game(game_name, game_genre, game_app_id, game_minutes)
                        self.game_list.append(new_game)
                log.info("Game list done")

                increments = len(self.game_list) / 100
                self.increment_amount.emit(increments)
                self.genres_requested.emit(self.game_list)

            else:
                log.error(STEAM_EXCEPTION)
                log.error("Code: " + str(ownedGamesReq.status_code))
                self.submit_button.setEnabled(True)
                ErrorDialog(STEAM_EXCEPTION)
        else:
            log.error(NO_NETWORK)
            self.submit_button.setEnabled(True)
            ErrorDialog(NO_NETWORK)

    def _check_connection(self):
        host = "http://google.com"
        try:
            urllib.request.urlopen(host)
            return True
        except Exception as e:
            log.error(e)
            return False

    def _result_to_list(self, emit_list):
        self.result_list = emit_list

    def _on_finished(self, finished):
        log.info("On finished called")
        if finished:
                #Sorting the list alphabetically, omitting "the " or "The " from the beginning of titles   
                self.game_list.sort(key = attrgetter("sort_name"), reverse = False)

                #basically just assigning the genres from the futures result to the actual games in the games_list
                for game in self.game_list:
                    for genre in self.result_list:
                        if genre.startswith(str(game.steam_app_id)):
                            game.genre = genre.replace(str(game.steam_app_id), "")

                print("-----------------------------")
                end = time.time()
                print("Job end: " + str(end))
                print("Job took: " + str(end - self.start))
                log.info("Job end: " + str(end))
                log.info("Job took: " + str(end - self.start))
                print("-----------------------------")

                try:
                    try:
                        from UserFile import UserFile
                        #saving user files once everything has been done successfully
                        log.info("Saving user files")
                        user_info_file = UserFile(self.steam_user)
                        user_info_file.create_user_file()   
                        user_info_file.create_library_file(self.game_list)
                        log.info("User files saved")
                    except Exception as e:
                        log.error(USER_FILE_EXCEPTION)
                        log.error(e)
                        ErrorDialog(USER_FILE_EXCEPTION)

                    log.info("Loading LibraryUI")
                    self.statusbar.clearMessage()
                    self.last_increment_request.emit(True)
                    self.steam_thread.quit()
                    self.loading_thread.quit()
                    LibraryUI(self.master)
                except Exception as e:
                    log.error(LIBRARY_UI_EXCEPTION)
                    log.error(e)
                    ErrorDialog(LIBRARY_UI_EXCEPTION)

    def _show_loading(self, ready):
        if ready:
            log.info("Show loading ready")
            self.loading_dialog.show_dialog()

    def _request_progress(self, ready):
        log.info("Request progress called")
        if ready:
            self.increment_request.emit(True)
