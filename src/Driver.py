# Program that gives detailed stats/ratings about a user's Steam library
# Author: Daniel Harrington

from os import path
from SteamUI import *
from LibraryUI import *
from Global import *
import multiprocessing
import ctypes
from ErrorDialog import *
import logging as log


def main():
    log.info("Driver main started")

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon(WIN_ICON))
    master = QtWidgets.QMainWindow()
    master.setWindowIcon(QIcon(WIN_ICON))
    tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(WIN_ICON), app)
    tray_icon.show()
    app_icon = QtGui.QIcon()
    app_icon.addFile(WIN_ICON, QtCore.QSize(256,256))

    myappid = "dharringtondev.GamingStatsProject" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    #if the files don't exist for user info and the game library, we're taking the user to put
    #their info in again
    if not os.path.exists(USER_FILE_NAME) and not os.path.exists(LIBRARY_FILE_NAME):
        try:
            log.info("Loading SteamUI")
            SteamUI(master)
        except Exception as e:
            log.error(STEAM_UI_EXCEPTION)
            log.error(e)
            ErrorDialog(STEAM_EXCEPTION)
    else:
        try:
            log.info("Loading LibraryUI")
            LibraryUI(master)
        except Exception as e:
            log.error(LIBRARY_UI_EXCEPTION)
            log.error(e)
            ErrorDialog(LIBRARY_UI_EXCEPTION)

    master.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    with open(LOG_FILE_NAME, "w"):
        pass
    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)
    if sys.platform.startswith("win"):
        multiprocessing.freeze_support()
    main()