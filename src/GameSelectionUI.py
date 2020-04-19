from PyQt5 import QtCore, QtGui, QtWidgets
from Global import *
from SteamUI import *
from BlizzardUI import *
import logging as log

class GameSelectionUI(QObject):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, master):
        super().__init__()
        self.master = master
        self.setupUi(master)

    def setupUi(self, import_info_window):
        import_info_window.setObjectName("import_info_window")
        import_info_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(import_info_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_info_label = QtWidgets.QLabel(self.centralwidget)
        self.add_info_label.setMinimumSize(QtCore.QSize(0, 50))
        self.add_info_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(LARGE_FONT_POINT)
        self.add_info_label.setFont(font)
        self.add_info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add_info_label.setObjectName("add_info_label")
        self.verticalLayout.addWidget(self.add_info_label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.cod_button = QtWidgets.QPushButton(self.centralwidget)
        self.cod_button.setMinimumSize(QtCore.QSize(200, 40))
        self.cod_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.cod_button.setFont(font)
        self.cod_button.setObjectName("cod_button")
        self.gridLayout.addWidget(self.cod_button, 5, 0, 1, 1)
        self.blizzard_button = QtWidgets.QPushButton(self.centralwidget)
        self.blizzard_button.setMinimumSize(QtCore.QSize(200, 40))
        self.blizzard_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.blizzard_button.setFont(font)
        self.blizzard_button.setObjectName("blizzard_button")
        self.gridLayout.addWidget(self.blizzard_button, 2, 0, 1, 1)
        self.steam_button = QtWidgets.QPushButton(self.centralwidget)
        self.steam_button.setMinimumSize(QtCore.QSize(200, 40))
        self.steam_button.setMaximumSize(QtCore.QSize(200, 40))
        self.steam_button.clicked.connect(lambda: self._go_to_steam_ui())
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.steam_button.setFont(font)
        self.steam_button.setObjectName("steam_button")
        self.gridLayout.addWidget(self.steam_button, 1, 0, 1, 1)
        self.dota_button = QtWidgets.QPushButton(self.centralwidget)
        self.dota_button.setMinimumSize(QtCore.QSize(200, 40))
        self.dota_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.dota_button.setFont(font)
        self.dota_button.setObjectName("dota_button")
        self.gridLayout.addWidget(self.dota_button, 4, 0, 1, 1)
        self.league_button = QtWidgets.QPushButton(self.centralwidget)
        self.league_button.setMinimumSize(QtCore.QSize(200, 40))
        self.league_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.league_button.setFont(font)
        self.league_button.setObjectName("league_button")
        self.gridLayout.addWidget(self.league_button, 1, 1, 1, 1)
        self.csgo_button = QtWidgets.QPushButton(self.centralwidget)
        self.csgo_button.setMinimumSize(QtCore.QSize(200, 40))
        self.csgo_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.csgo_button.setFont(font)
        self.csgo_button.setObjectName("csgo_button")
        self.gridLayout.addWidget(self.csgo_button, 2, 1, 1, 1)
        self.fortnite_button = QtWidgets.QPushButton(self.centralwidget)
        self.fortnite_button.setMinimumSize(QtCore.QSize(200, 40))
        self.fortnite_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.fortnite_button.setFont(font)
        self.fortnite_button.setObjectName("fortnite_button")
        self.gridLayout.addWidget(self.fortnite_button, 4, 1, 1, 1)
        self.pubg_button = QtWidgets.QPushButton(self.centralwidget)
        self.pubg_button.setMinimumSize(QtCore.QSize(200, 40))
        self.pubg_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.pubg_button.setFont(font)
        self.pubg_button.setObjectName("pubg_button")
        self.gridLayout.addWidget(self.pubg_button, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.delete_lib_layout = QtWidgets.QHBoxLayout()
        self.delete_lib_layout.setObjectName("delete_lib_layout")
        self.delete_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_info_button.setMinimumSize(QtCore.QSize(200, 40))
        self.delete_info_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.delete_info_button.setFont(font)
        self.delete_info_button.setObjectName("delete_info_button")
        self.delete_lib_layout.addWidget(self.delete_info_button)
        self.go_to_lib_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_to_lib_button.setMinimumSize(QtCore.QSize(200, 40))
        self.go_to_lib_button.setMaximumSize(QtCore.QSize(200, 40))
        self.go_to_lib_button.clicked.connect(lambda: self._go_to_lib_ui(import_info_window))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        self.go_to_lib_button.setFont(font)
        self.go_to_lib_button.setObjectName("go_to_lib_button")
        self.delete_lib_layout.addWidget(self.go_to_lib_button)
        self.verticalLayout.addLayout(self.delete_lib_layout)
        import_info_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(import_info_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        import_info_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(import_info_window)
        self.statusbar.setObjectName("statusbar")
        import_info_window.setStatusBar(self.statusbar)

        self.retranslateUi(import_info_window)
        QtCore.QMetaObject.connectSlotsByName(import_info_window)

    def retranslateUi(self, import_info_window):
        _translate = QtCore.QCoreApplication.translate
        import_info_window.setWindowTitle(_translate("import_info_window", "MainWindow"))
        self.add_info_label.setText(_translate("import_info_window", "Import Game Information"))
        self.cod_button.setText(_translate("import_info_window", "Call of Duty: MW"))
        self.blizzard_button.setText(_translate("import_info_window", "Blizzard Games"))
        self.steam_button.setText(_translate("import_info_window", "Steam Library"))
        self.dota_button.setText(_translate("import_info_window", "Dota 2"))
        self.league_button.setText(_translate("import_info_window", "League of Legends"))
        self.csgo_button.setText(_translate("import_info_window", "CS: GO"))
        self.fortnite_button.setText(_translate("import_info_window", "Fortnite"))
        self.pubg_button.setText(_translate("import_info_window", "PUBG"))
        self.delete_info_button.setText(_translate("import_info_window", "Delete Information"))
        self.go_to_lib_button.setText(_translate("import_info_window", "Go to Library"))

    def _go_to_steam_ui(self):
        steam_dialog = QtWidgets.QDialog
        SteamUI(steam_dialog)

    def _go_to_lib_ui(self, master):
        LibraryUI(master)

    def _go_to_blizz_ui(self):
        BlizzardUI()