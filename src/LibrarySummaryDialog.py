from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Global import *
from collections import Counter
from itertools import groupby
from operator import attrgetter
import logging as log

class LibrarySummaryDialog(object):
    
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, game_list):
        log.info("Library summary init called")
        summary_dialog = QtWidgets.QDialog()
        self.setup_Ui(summary_dialog, game_list)
        summary_dialog.setWindowIcon(QIcon(WIN_ICON))
        summary_dialog.setWindowFlags(summary_dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        summary_dialog.show()
        summary_dialog.exec_()

    def setup_Ui(self, summary_dialog, game_list):
        summary_dialog.setObjectName("summary_dialog")
        summary_dialog.resize(700, 500)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        summary_dialog.setFont(font)
        self.summary_dialog_vert_layout = QtWidgets.QVBoxLayout(summary_dialog)
        self.summary_dialog_vert_layout.setObjectName("summary_dialog_vert_layout")
        self.games_labels_horz_layout = QtWidgets.QHBoxLayout()
        self.games_labels_horz_layout.setObjectName("games_labels_horz_layout")
        self.most_played_games_label = QtWidgets.QLabel(summary_dialog)
        self.most_played_games_label.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.most_played_games_label.setFont(font)
        self.most_played_games_label.setWordWrap(True)
        self.most_played_games_label.setObjectName("most_played_games_label")
        self.games_labels_horz_layout.addWidget(self.most_played_games_label)
        self.highest_rated_label = QtWidgets.QLabel(summary_dialog)
        self.highest_rated_label.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.highest_rated_label.setFont(font)
        self.highest_rated_label.setWordWrap(True)
        self.highest_rated_label.setObjectName("highest_rated_label")
        self.games_labels_horz_layout.addWidget(self.highest_rated_label)
        self.summary_dialog_vert_layout.addLayout(self.games_labels_horz_layout)
        self.games_horz_layout = QtWidgets.QHBoxLayout()
        self.games_horz_layout.setObjectName("games_horz_layout")
        self.most_played_game_list = QtWidgets.QListWidget(summary_dialog)
        self.most_played_game_list.setMinimumSize(QtCore.QSize(250, 0))
        self.most_played_game_list.setObjectName("most_played_game_list")
        self.games_horz_layout.addWidget(self.most_played_game_list)
        self.highest_rated_games_list = QtWidgets.QListWidget(summary_dialog)
        self.highest_rated_games_list.setMinimumSize(QtCore.QSize(250, 0))
        self.highest_rated_games_list.setObjectName("highest_rated_games_list")
        self.games_horz_layout.addWidget(self.highest_rated_games_list)
        self.summary_dialog_vert_layout.addLayout(self.games_horz_layout)
        self.genres_label_horz_layout = QtWidgets.QHBoxLayout()
        self.genres_label_horz_layout.setObjectName("genres_label_horz_layout")
        self.most_played_genres_label = QtWidgets.QLabel(summary_dialog)
        self.most_played_genres_label.setMinimumSize(QtCore.QSize(200, 0))
        self.most_played_genres_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.most_played_genres_label.setFont(font)
        self.most_played_genres_label.setWordWrap(True)
        self.most_played_genres_label.setObjectName("most_played_genres_label")
        self.genres_label_horz_layout.addWidget(self.most_played_genres_label)
        self.most_prevalent_label = QtWidgets.QLabel(summary_dialog)
        self.most_prevalent_label.setMinimumSize(QtCore.QSize(200, 0))
        self.most_prevalent_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.most_prevalent_label.setFont(font)
        self.most_prevalent_label.setWordWrap(True)
        self.most_prevalent_label.setObjectName("most_prevalent_label")
        self.genres_label_horz_layout.addWidget(self.most_prevalent_label)
        self.summary_dialog_vert_layout.addLayout(self.genres_label_horz_layout)
        self.genres_horz_layout = QtWidgets.QHBoxLayout()
        self.genres_horz_layout.setObjectName("genres_horz_layout")
        self.most_played_genres_list = QtWidgets.QListWidget(summary_dialog)
        self.most_played_genres_list.setMinimumSize(QtCore.QSize(250, 0))
        self.most_played_genres_list.setObjectName("most_played_genres_list")
        self.genres_horz_layout.addWidget(self.most_played_genres_list)
        self.most_prevalent_genres_list = QtWidgets.QListWidget(summary_dialog)
        self.most_prevalent_genres_list.setMinimumSize(QtCore.QSize(250, 0))
        self.most_prevalent_genres_list.setObjectName("most_prevalent_genres_list")
        self.genres_horz_layout.addWidget(self.most_prevalent_genres_list)
        self.summary_dialog_vert_layout.addLayout(self.genres_horz_layout)

        self._populate_lists(game_list)

        self.retranslateUi(summary_dialog)
        QtCore.QMetaObject.connectSlotsByName(summary_dialog)

    def retranslateUi(self, summary_dialog):
        _translate = QtCore.QCoreApplication.translate
        summary_dialog.setWindowTitle(_translate("summary_dialog", "Library Summary"))
        self.most_played_games_label.setText(_translate("summary_dialog", "Most Played Games"))
        self.highest_rated_label.setText(_translate("summary_dialog", "Highest Rated Games"))
        self.most_played_genres_label.setText(_translate("summary_dialog", "Most Played Genres"))
        self.most_prevalent_label.setText(_translate("summary_dialog", "Most Prevalent Genres"))

    def _populate_lists(self, game_list):
        log.ingo("Summary populate lists called")
        most_played_games = self._calculate_most_played_games(game_list)
        highest_rated_games = self._calculate_highest_rated_games(game_list)
        most_played_genres = self._calculate_most_played_genres(game_list)
        most_prevalent_genres = self._calculate_most_prevalent_genres(game_list)

        index = 0
        for game in most_played_games:
            self.most_played_game_list.insertItem(index, game)
            index += 1
            log.info("Game inserted to most played: " + game.name)
        
        index = 0
        for game in highest_rated_games:
            self.highest_rated_games_list.insertItem(index, game)
            index += 1
            log.info("Game inserted to highest rated: " + game.name)

        index = 0
        for genre in most_played_genres:
            self.most_played_genres_list.insertItem(index, genre)
            index += 1
            log.info("Genre inserted to most played: " + genre)

        index = 0
        for genre in most_prevalent_genres:
            self.most_prevalent_genres_list.insertItem(index, genre)
            index += 1
            log.info("Genre inserted to most prevalent: " + genre)

        log.info("Populate lists complete")

    def _calculate_most_played_games(self, game_list):
        log.info("Calculate most played called")
        log.info("Sorting game_list by minutes played (descending)")
        game_list.sort(key = attrgetter("minutes_played"), reverse = True)

        log.info("Sorting complete")
        log.info("Creating new list and adding first five elements of game_list to it")
        top_ten = []
        for i in range(10):
            top_ten.append(game_list[i].name)

        log.info("Top list completed - most played games")
        return top_ten

    def _calculate_highest_rated_games(self, game_list):
        log.info("Calculate highest rated called")
        log.info("Sorting game_list by rating (descending)")
        game_list.sort(key = attrgetter("rating"), reverse = True)

        log.info("Sorting complete")
        log.info("Creating new list to hold five highest rated games")
        top_ten = []
        for i in range(10):
            top_ten.append(game_list[i].name)
        log.info("Top list completed - highest rated games")
        return top_ten

    def _calculate_most_played_genres(self, game_list):
        log.info("Calculate most played genres called")
        log.info("Sorting game_list by minutes played (descending)")
        game_list.sort(key = attrgetter("minutes_played"), reverse = True)

        #creating smaller list of games to work with their genres
        small_game_list = []
        for i in range(10):
            small_game_list.append(game_list[i])

        genre_list = []
        top_ten = []
        for game in small_game_list:
            game_genres = [game.genre.split(", ")]
            genre_list.extend(game_genres)
        genre_list = list(filter(None, genre_list))
        flat_genres = []
        for sublist in genre_list:
            for item in sublist:
                flat_genres.append(item)
        flat_genres = list(filter(None, flat_genres))

        log.info("Flat genre list completed")
        for genre in flat_genres:
            log.info(genre)

        freqs = Counter(flat_genres)
        log.info(freqs)

        count = freqs.most_common(10)
        for i in range(10):
            top_ten.append(count[i][0])
        log.info(top_ten)

        log.info("Top list completed - most played genres")
        
        return top_ten

    def _calculate_most_prevalent_genres(self, game_list):
        log.info("Calculate most prevalent called")
        log.info("Creating list of all genres in library (with dupes)")
        genre_list = []
        top_ten = []
        for game in game_list:
            game_genres = [game.genre.split(", ")]
            genre_list.extend(game_genres)
        genre_list = list(filter(None, genre_list))
        flat_genres = []
        for sublist in genre_list:
            for item in sublist:
                flat_genres.append(item)
        flat_genres = list(filter(None, flat_genres))

        log.info("Flat genre list completed")
        for genre in flat_genres:
            log.info(genre)

        freqs = Counter(flat_genres)
        log.info(freqs)

        count = freqs.most_common(10)
        for i in range(10):
            top_ten.append(count[i][0])
        log.info(top_ten)

        log.info("Top list completed - most prevalent genres")
        
        return top_ten