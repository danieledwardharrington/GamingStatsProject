from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Global import *
import logging as log

class ErrorDialog(object):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    def __init__(self, exception_type):
        super().__init__()
        log.info("Error dialog init")
        self.error_dialog = QtWidgets.QDialog()
        self.setup_Ui(self.error_dialog)
        self.error_dialog.setWindowIcon(QIcon(WIN_ICON))
        self.error_dialog.setWindowFlags(self.error_dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self._set_dialog_text(exception_type)
        self.error_dialog.show()
        self.error_dialog.exec_()

    def setup_Ui(self, error_dialog):
        error_dialog.setObjectName("error_dialog")
        error_dialog.resize(400, 150)
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(NORM_FONT_POINT)
        error_dialog.setFont(font)
        self.error_label_horz_layout = QtWidgets.QHBoxLayout(error_dialog)
        self.error_label_horz_layout.setObjectName("error_label_horz_layout")
        self.error_label = QtWidgets.QLabel(error_dialog)
        self.error_label.setMinimumSize(QtCore.QSize(300, 0))
        self.error_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        self.error_label_horz_layout.addWidget(self.error_label)

        self.retranslateUi(error_dialog)
        QtCore.QMetaObject.connectSlotsByName(error_dialog)

    def retranslateUi(self, error_dialog):
        _translate = QtCore.QCoreApplication.translate
        error_dialog.setWindowTitle(_translate("error_dialog", ERROR_TITLE))
        self.error_label.setText(_translate("error_dialog", "Placeholder"))

    def _set_dialog_text(self, exception_type):
        log.info("Error dialog set text called")
        if exception_type == NO_NETWORK:
            self.error_label.setText(NO_NETWORK)
        elif exception_type == LIBRARY_FILE_EXCEPTION:
            self.error_label.setText(LIBRARY_FILE_POPUP)
        elif exception_type == STEAM_EXCEPTION:
            self.error_label.setText(STEAM_POPUP)
        elif exception_type == USER_FILE_EXCEPTION:
            self.error_label.setText(USER_FILE_POPUP)
        elif exception_type == LIBRARY_UI_EXCEPTION:
            self.error_label.setText(LIBRARY_UI_POPUP)
        elif exception_type == BROWSER_EXCEPTION:
            self.error_label.setText(BROWSER_POPUP)
        elif exception_type == EDIT_EXCEPTION:
            self.error_label.setText(EDIT_POPUP)
        elif exception_type == SUMMARY_EXCEPTION:
            self.error_label.setText(SUMMARY_POPUP)
        elif exception_type == STEAM_UI_EXCEPTION:
            self.error_label.setText(STEAM_UI_POPUP)
        elif exception_type == NO_GAME_EXCEPTION:
            self.error_label.setText(NO_GAME_POPUP)
        elif exception_type == DELETE_USER_EXCEPTION:
            self.error_label.setText(DELETE_USER_POPUP)
        else:
            self.error_label.setText(UNKNOWN_POPUP)
        