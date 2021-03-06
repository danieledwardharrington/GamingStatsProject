from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Global import *
from UserFile import *
from LibraryUI import *
from ErrorDialog import *
import logging as log

class EditGameUI(object):

    log.basicConfig(level = log.DEBUG)

    def __init__(self, game_to_edit, game_list, lib_window, steam_thread, loading_thread):
        super().__init__()
        log.info("EditGameUI init called")
        edit_dialog = QtWidgets.QDialog()
        edit_dialog.setWindowFlags(edit_dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        edit_dialog.setWindowIcon(QIcon(WIN_ICON))
        self.steam_thread = steam_thread
        self.loading_thread = loading_thread
        self.setup_Ui(edit_dialog, game_to_edit, game_list, lib_window)
        log.info("EditGameUI ui setup")
        edit_dialog.show()
        edit_dialog.exec_()

    def setup_Ui(self, edit_game_dialog, game_to_edit, game_list, lib_window):
        edit_game_dialog.setObjectName("edit_game_dialog")
        edit_game_dialog.resize(500, 400)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        edit_game_dialog.setFont(font)
        self.edit_grid_layout = QtWidgets.QGridLayout(edit_game_dialog)
        self.edit_grid_layout.setObjectName("edit_grid_layout")
        self.genre_horz_layout = QtWidgets.QHBoxLayout()
        self.genre_horz_layout.setObjectName("genre_horz_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.genre_horz_layout.addItem(spacerItem)
        self.genre_label = QtWidgets.QLabel(edit_game_dialog)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(12)
        self.genre_label.setFont(font)
        self.genre_label.setObjectName("genre_label")
        self.genre_horz_layout.addWidget(self.genre_label)
        self.genre_entry = QtWidgets.QLineEdit(edit_game_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genre_entry.sizePolicy().hasHeightForWidth())
        self.genre_entry.setSizePolicy(sizePolicy)
        self.genre_entry.setMinimumSize(QtCore.QSize(300, 0))
        self.genre_entry.setMaximumSize(QtCore.QSize(300, 16777215))
        self.genre_entry.setText(game_to_edit.genre)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(12)
        self.genre_entry.setFont(font)
        self.genre_entry.setObjectName("genre_entry")
        self.genre_horz_layout.addWidget(self.genre_entry, 0, QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.genre_horz_layout.addItem(spacerItem1)
        self.edit_grid_layout.addLayout(self.genre_horz_layout, 0, 0, 1, 1)
        self.rating_horz_layout = QtWidgets.QHBoxLayout()
        self.rating_horz_layout.setObjectName("rating_horz_layout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rating_horz_layout.addItem(spacerItem2)
        self.rating_label = QtWidgets.QLabel(edit_game_dialog)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(12)
        self.rating_label.setFont(font)
        self.rating_label.setObjectName("rating_label")
        self.rating_horz_layout.addWidget(self.rating_label)
        self.rating_entry = QtWidgets.QLineEdit(edit_game_dialog)
        self.rating_entry.setMinimumSize(QtCore.QSize(300, 0))
        self.rating_entry.setMaximumSize(QtCore.QSize(300, 16777215))
        self.rating_entry.setText(str(game_to_edit.rating))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(12)
        self.rating_entry.setFont(font)
        self.rating_entry.setObjectName("rating_entry")
        self.rating_horz_layout.addWidget(self.rating_entry)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rating_horz_layout.addItem(spacerItem3)
        self.edit_grid_layout.addLayout(self.rating_horz_layout, 1, 0, 1, 1)
        self.button_horz_layout = QtWidgets.QHBoxLayout()
        self.button_horz_layout.setContentsMargins(0, -1, -1, -1)
        self.button_horz_layout.setObjectName("button_horz_layout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_horz_layout.addItem(spacerItem4)
        self.save_button = QtWidgets.QPushButton(edit_game_dialog)
        self.save_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.save_button.setToolTip("Save changes")
        self.save_button.clicked.connect(lambda: self._save_edit(game_to_edit, game_list, edit_game_dialog, lib_window))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(10)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.button_horz_layout.addWidget(self.save_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.cancel_button = QtWidgets.QPushButton(edit_game_dialog)
        self.cancel_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setToolTip("Cancel changes")
        self.cancel_button.clicked.connect(lambda: edit_game_dialog.reject())
        self.button_horz_layout.addWidget(self.cancel_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_horz_layout.addItem(spacerItem5)
        self.edit_grid_layout.addLayout(self.button_horz_layout, 2, 0, 1, 1)
        self.genre_entry.setCursorPosition(0)
        self.rating_entry.setCursorPosition(0)

        self.retranslateUi(edit_game_dialog, game_to_edit)
        QtCore.QMetaObject.connectSlotsByName(edit_game_dialog)

    def retranslateUi(self, edit_game_dialog, game_to_edit):
        _translate = QtCore.QCoreApplication.translate
        game_name = game_to_edit.name
        edit_game_dialog.setWindowTitle(_translate("edit_game_dialog", "Gaming Stats Project - " + game_name))
        self.genre_label.setText(_translate("edit_game_dialog", "Genre "))
        self.rating_label.setText(_translate("edit_game_dialog", "Rating"))
        self.save_button.setText(_translate("edit_game_dialog", "Save"))
        self.cancel_button.setText(_translate("edit_game_dialog", "Cancel"))

    def _save_edit(self, game, game_list, edit_game_dialog, lib_window):
        log.info("Save edit called")
        self.steam_thread.quit()
        self.loading_thread.quit()
        new_genre = self.genre_entry.text().strip()
        new_rating_str = self.rating_entry.text().strip()
        new_rating = round(float(new_rating_str), 1)

        game.genre = new_genre
        game.rating = new_rating

        try:
            from UserFile import UserFile
            new_lib_file = UserFile()
            new_lib_file.create_library_file(game_list)
            log.info("Save edit successful")
        except Exception as e:
            log.info(LIBRARY_FILE_EXCEPTION)
            log.info(e)
            ErrorDialog(LIBRARY_FILE_EXCEPTION)

        try:
            from LibraryUI import LibraryUI
            LibraryUI(lib_window)
            edit_game_dialog.accept()
        except Exception as e:
            log.info(LIBRARY_UI_EXCEPTION)
            log.info(e)
            ErrorDialog(LIBRARY_UI_EXCEPTION) 