from ..Vars.Global import *
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView
import concurrent.futures
import time
from operator import attrgetter
from ..GameUser import UserFile, SteamUser
import urllib.request
from ..GameWorkers import SteamGame, SteamBot, SteamWorker
import sys
from . import EditGameUI, LibrarySummaryDialog
from ..MiscDialog import AboutDialog, DeleteUserDialog, LoadingDialog, ErrorDialog
import logging as log
import requests

class LibraryUI(QObject):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)
    
    game_list = []
    new_game_list = []
    result_list = []
    updated_game_list = []

    genres_requested = QtCore.pyqtSignal(list)
    increment_request = QtCore.pyqtSignal(bool)
    increment_amount = QtCore.pyqtSignal(float)
    last_increment_request = QtCore.pyqtSignal(bool)

    def __init__(self, master):
        super().__init__()
        log.info("LibraryUI init called")
        self._load_data()
        self.master = master
        self.steam_worker = SteamWorker()
        self.setup_Ui(self.master, self.steam_worker)
        self.steam_user = SteamUser()
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

    def setup_Ui(self, library_window, steam_worker):
        library_window.setObjectName("library_window")
        library_window.resize(538, 748)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        library_window.setFont(font)
        self.parent_vert_layout = QtWidgets.QWidget(library_window)
        self.parent_vert_layout.setObjectName("parent_vert_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.parent_vert_layout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_horz_layout = QtWidgets.QHBoxLayout()
        self.table_horz_layout.setObjectName("table_horz_layout")
        self.game_lib_table = QtWidgets.QTableWidget(self.parent_vert_layout)
        self.game_lib_table.setColumnCount(4)
        self.game_lib_table.setObjectName("game_lib_table")
        self.game_lib_table.setRowCount(0)
        self.game_lib_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_horz_layout.addWidget(self.game_lib_table)
        self.verticalLayout.addLayout(self.table_horz_layout)
        self.update_delete_horz_layout = QtWidgets.QHBoxLayout()
        self.update_delete_horz_layout.setObjectName("update_delete_horz_layout")
        self.update_library_button = QtWidgets.QPushButton(self.parent_vert_layout)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.update_library_button.setFont(font)
        self.update_library_button.setObjectName("update_library_button")
        self.update_library_button.clicked.connect(lambda: self._update_library(library_window, steam_worker))
        self.update_delete_horz_layout.addWidget(self.update_library_button)
        self.delete_info_button = QtWidgets.QPushButton(self.parent_vert_layout)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.delete_info_button.setFont(font)
        self.delete_info_button.setObjectName("delete_info_button")
        self.delete_info_button.clicked.connect(lambda: self._confirm_delete(library_window))
        self.update_delete_horz_layout.addWidget(self.delete_info_button)
        self.verticalLayout.addLayout(self.update_delete_horz_layout)
        self.edit_summary_horz_layout = QtWidgets.QHBoxLayout()
        self.edit_summary_horz_layout.setObjectName("edit_summary_horz_layout")
        self.edit_game_button = QtWidgets.QPushButton(self.parent_vert_layout)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.edit_game_button.setFont(font)
        self.edit_game_button.setObjectName("edit_game_button")
        self.edit_game_button.clicked.connect(lambda: self._edit_game(library_window))
        self.edit_summary_horz_layout.addWidget(self.edit_game_button)
        self.lib_summary_button = QtWidgets.QPushButton(self.parent_vert_layout)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.lib_summary_button.setFont(font)
        self.lib_summary_button.setObjectName("lib_summary_button")
        self.lib_summary_button.clicked.connect(lambda: self._show_summary())
        self.edit_summary_horz_layout.addWidget(self.lib_summary_button)
        self.verticalLayout.addLayout(self.edit_summary_horz_layout)
        library_window.setCentralWidget(self.parent_vert_layout)
        self.library_menu_bar = QtWidgets.QMenuBar(library_window)
        self.library_menu_bar.setGeometry(QtCore.QRect(0, 0, 538, 21))
        self.library_menu_bar.setObjectName("library_menu_bar")
        self.menu_file = QtWidgets.QMenu(self.library_menu_bar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.library_menu_bar)
        self.menu_help.setObjectName("menu_help")
        library_window.setMenuBar(self.library_menu_bar)
        self.library_statusbar = QtWidgets.QStatusBar(library_window)
        self.library_statusbar.setObjectName("library_statusbar")
        library_window.setStatusBar(self.library_statusbar)
        self.action_exit = QtWidgets.QAction(library_window)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.action_exit.setFont(font)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.setShortcut("Ctrl+Q")
        self.action_exit.setStatusTip("Exit the app")
        self.action_exit.triggered.connect(lambda: sys.exit())
        self.action_about = QtWidgets.QAction(library_window)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        self.action_about.setFont(font)
        self.action_about.setObjectName("action_about")
        self.action_about.triggered.connect(lambda: AboutUI())
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.library_menu_bar.addAction(self.menu_file.menuAction())
        self.library_menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(library_window)
        QtCore.QMetaObject.connectSlotsByName(library_window)

        self._populate_table(self.game_lib_table)

        log.info("LibraryUI loaded")

    def retranslateUi(self, library_window):
        _translate = QtCore.QCoreApplication.translate
        library_window.setWindowTitle(_translate("library_window", "Gaming Stats Project - Library"))
        self.update_library_button.setToolTip(_translate("library_window", "Update the library to include new games"))
        self.update_library_button.setText(_translate("library_window", "Update library"))
        self.delete_info_button.setToolTip(_translate("library_window", "Delete the current user and library information"))
        self.delete_info_button.setText(_translate("library_window", "Delete user info"))
        self.edit_game_button.setToolTip(_translate("library_window", "Edit the game\'s rating and genre"))
        self.edit_game_button.setText(_translate("library_window", "Edit rating/genre"))
        self.lib_summary_button.setToolTip(_translate("library_window", "View a brief summary of your library"))
        self.lib_summary_button.setText(_translate("library_window", "Library Summary"))
        self.menu_file.setTitle(_translate("library_window", "File"))
        self.menu_help.setTitle(_translate("library_window", "Help"))
        self.action_exit.setText(_translate("library_window", "Exit"))
        self.action_about.setText(_translate("library_window", "About"))

    #loading data from the file
    def _load_data(self):
        log.info("Load data called")
        try:
            pickle_in = open(LIBRARY_FILE_NAME, "rb")
            self.game_list = pickle.load(pickle_in)
            log.info("Load data successful") 
        except Exception as e:
            log.error(LIBRARY_FILE_EXCEPTION)
            log.error(e)
            ErrorDialog(LIBRARY_FILE_EXCEPTION)
    
    def _edit_game(self, lib_window):
        log.info("Edit game called")
        item_index = self.game_lib_table.currentIndex()
        game_data = self.game_lib_table.model().data(item_index)

        if item_index.column() == 0:
            game_to_edit = SteamGame()
            game_name = game_data
            for game in self.game_list:
                if game_name == game.name:
                    game_to_edit = game
            log.info("Game to edit created: " + game_to_edit.name)
            try:
                EditGameUI(game_to_edit, self.game_list, lib_window, self.steam_thread, self.loading_thread)
            except Exception as e:
                log.error(EDIT_EXCEPTION)
                log.error(e)
                ErrorDialog(EDIT_POPUP)
        else:
            ErrorDialog(NO_GAME_EXCEPTION)

    def _update_library(self, root, steam_worker):
        log.info("Update library called")
        self.library_statusbar.showMessage("Please wait...", 6000)
        self.update_library_button.setEnabled(False)
        self.delete_info_button.setEnabled(False)
        self.lib_summary_button.setEnabled(False)
        self.edit_game_button.setEnabled(False)

        steam_worker.listed.connect(self._result_to_list)
        steam_worker.finished.connect(self._on_finished)
        steam_worker.ready.connect(self._show_loading)
        self.genres_requested.connect(steam_worker.steam_work)
        self.increment_amount.connect(self.loading_dialog.set_increments)
        self.increment_request.connect(self.loading_dialog.increment_bar)
        
        pickle_in = open(USER_FILE_NAME, "rb")
        self.steam_user = pickle.load(pickle_in)

        log.info("Steam user ID: " + self.steam_user.steam_user_id)
        log.info("Steam user API key: " + self.steam_user.steam_user_api)

        if self._check_connection():
            
            ownedGamesReq = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + self.steam_user.steam_user_api + "&include_appinfo=true&include_played_free_games=true&steamid=" + self.steam_user.steam_user_id + "&format=json")
            log.info(type(ownedGamesReq))
            
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

                name_list = []
                log.info("Populating new game list")
                for game in ownedGamesRes["response"]["games"]:
                    if game["playtime_forever"] > 0:
                        game_minutes = game["playtime_forever"]
                        game_name = game["name"]
                        game_app_id = game["appid"]
                        game_genre = ""
                        new_game = SteamGame(game_name, game_genre, game_app_id, game_minutes)
                        for item in self.game_list:
                            name_list.append(item.name)
                        if game_name not in name_list: 
                            self.new_game_list.append(new_game)
                log.info("New game list done")

                increments = len(self.game_list) / 100
                log.info("Increments: " + str(increments))
                self.increment_amount.emit(increments)
                self.genres_requested.emit(self.game_list)

                #basically just assigning the genres from the futures result to the actual games in the games_list
                for game in self.new_game_list:
                    for genre in self.result_list:
                        if game.name in genre:
                            game.genre = genre.replace(game.name, "")
  

            else:
                self.update_library_button.setEnabled(True)
                self.delete_info_button.setEnabled(True)
                self.lib_summary_button.setEnabled(True)
                self.edit_game_button.setEnabled(True)
                log.error(STEAM_EXCEPTION)
                log.error("Code: " + str(ownedGamesReq.status_code))
                ErrorDialog(STEAM_EXCEPTION)
        else:
            self.update_library_button.setEnabled(True)
            self.delete_info_button.setEnabled(True)
            self.lib_summary_button.setEnabled(True)
            self.edit_game_button.setEnabled(True)
            log.error(NO_NETWORK)
            ErrorDialog(NO_NETWORK)

    def _show_summary(self):
        log.info("Show summary called")
        try:
            LibrarySummaryDialog(self.game_list)
        except Exception as e:
            log.error(SUMMARY_EXCEPTION)
            log.error(e)
            ErrorDialog(SUMMARY_EXCEPTION)

    def _populate_table(self, library_table):
        log.info("Populate table called")
        library_table.setRowCount(len(self.game_list))
        header = library_table.horizontalHeader()
        header.setSectionsClickable(True)

        library_table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        library_table.setHorizontalHeaderItem(1, QTableWidgetItem("Rating"))
        library_table.setHorizontalHeaderItem(2, QTableWidgetItem("Hours Played"))
        library_table.setHorizontalHeaderItem(3, QTableWidgetItem("Minutes Played"))

        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        row = 0
        for game in self.game_list:
            name_item = QtWidgets.QTableWidgetItem()
            name_item.setText(game.name)
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            library_table.setItem(row, 0, name_item)
            rating_str = "{:10.1f}".format(game.rating)
            rating_item = QtWidgets.QTableWidgetItem()
            rating_item.setText(rating_str)
            rating_item.setFlags(rating_item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEditable)
            library_table.setItem(row, 1, rating_item)
            hours_str = "{:10.1f}".format(game.hours_played)
            hours_item = QtWidgets.QTableWidgetItem()
            hours_item.setText(hours_str)
            hours_item.setFlags(hours_item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEditable)
            library_table.setItem(row, 2, hours_item)
            minutes_str = "{:10.0f}".format(game.minutes_played)
            minutes_item = QtWidgets.QTableWidgetItem()
            minutes_item.setText(minutes_str)
            minutes_item.setFlags(minutes_item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEditable)
            library_table.setItem(row, 3, minutes_item)
            
            row += 1

        library_table.setSortingEnabled(True)

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

    def _confirm_delete(self, master):
        try:
            DeleteUserDialog(master)
            self.steam_thread.quit()
            self.loading_thread.quit()
        except Exception as e:
            log.error(DELETE_USER_EXCEPTION)
            log.error(e)
            ErrorDialog(DELETE_USER_EXCEPTION)

    def _on_finished(self, finished):
        log.info("On finished called")
        if finished:
                #Sorting the list alphabetically, omitting "the " or "The " from the beginning of titles
                self.updated_game_list = self.game_list + self.new_game_list   
                self.updated_game_list.sort(key = attrgetter("sort_name"), reverse = False)

                for game in self.new_game_list:
                    print(game.name)
                    print(game.steam_app_id)
                    print(game.genre)

                print("-----------------------------")
                end = time.time()
                print("Job end: " + str(end))
                print("Job took: " + str(end - self.start))
                log.info("Job end: " + str(end))
                log.info("Job took: " + str(end - self.start))
                print("-----------------------------")

                try:
                    try:
                        from ..GameUser import UserFile
                        #saving user files once everything has been done successfully
                        log.info("Saving user files")
                        user_info_file = UserFile(self.steam_user)  
                        user_info_file.create_library_file(self.updated_game_list)
                        log.info("User files saved")
                    except Exception as e:
                        log.error(USER_FILE_EXCEPTION)
                        log.error(e)
                        ErrorDialog(USER_FILE_EXCEPTION)

                    self.last_increment_request.emit(True)
                    self.steam_thread.quit()
                    self.loading_thread.quit()
                    self.library_statusbar.clearMessage()
                    log.info("Loading LibraryUI")
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