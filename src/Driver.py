# Program that gives detailed stats/ratings about a user's Steam library
# Author: Daniel Harrington

from os import *
from LibraryGUI import *
from SteamUI import *
from LibraryUI import *
from Global import *
import multiprocessing


def main():

    app = QtWidgets.QApplication(sys.argv)
    master = QtWidgets.QMainWindow()
    master.setWindowIcon(QIcon(WIN_ICON))

    #if the files don't exist for user info and the game library, we're taking the user to put
    #their info in again
    if not os.path.exists(USER_FILE_NAME) and not os.path.exists(LIBRARY_FILE_NAME):
        print("Loading steamUI")
        SteamUI(master)
    else:
        print("Loading LibraryUI")
        LibraryUI(master)

    master.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if sys.platform.startswith("win"):
        multiprocessing.freeze_support()
    main()