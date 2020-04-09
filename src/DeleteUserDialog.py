from PyQt5 import QtCore, QtGui, QtWidgets
import os
from Global import *
from PyQt5.QtGui import QIcon
import logging as log

class DeleteUserDialog(object):

    log.basicConfig(level = log.DEBUG)

    def __init__(self, master):
        super().__init__()
        delete_dialog = QtWidgets.QDialog()
        self.setup_Ui(delete_dialog, master)
        delete_dialog.setWindowIcon(QIcon(WIN_ICON))
        delete_dialog.setWindowFlags(delete_dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        delete_dialog.show()
        delete_dialog.exec_()

    def setup_Ui(self, confirm_delete_dialog, master):
        confirm_delete_dialog.setObjectName("confirm_delete_dialog")
        confirm_delete_dialog.resize(300, 150)
        self.confirm_dialog_vert_layout = QtWidgets.QVBoxLayout(confirm_delete_dialog)
        self.confirm_dialog_vert_layout.setObjectName("confirm_dialog_vert_layout")
        self.confirm_layout = QtWidgets.QVBoxLayout()
        self.confirm_layout.setObjectName("confirm_layout")
        self.confirm_delete_label = QtWidgets.QLabel(confirm_delete_dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.confirm_delete_label.setFont(font)
        self.confirm_delete_label.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_delete_label.setWordWrap(True)
        self.confirm_delete_label.setObjectName("confirm_delete_label")
        self.confirm_layout.addWidget(self.confirm_delete_label)
        self.confirm_dialog_vert_layout.addLayout(self.confirm_layout)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        self.yes_button = QtWidgets.QPushButton(confirm_delete_dialog)
        self.yes_button.setMinimumSize(QtCore.QSize(80, 0))
        self.yes_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.yes_button.clicked.connect(lambda: self._confirmed(confirm_delete_dialog, master))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.yes_button.setFont(font)
        self.yes_button.setObjectName("yes_button")
        self.button_layout.addWidget(self.yes_button)
        self.no_button = QtWidgets.QPushButton(confirm_delete_dialog)
        self.no_button.setMinimumSize(QtCore.QSize(80, 0))
        self.no_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.no_button.clicked.connect(lambda: confirm_delete_dialog.reject())
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.no_button.setFont(font)
        self.no_button.setObjectName("no_button")
        self.button_layout.addWidget(self.no_button)
        self.confirm_dialog_vert_layout.addLayout(self.button_layout)

        self.retranslateUi(confirm_delete_dialog)
        QtCore.QMetaObject.connectSlotsByName(confirm_delete_dialog)

    def retranslateUi(self, confirm_delete_dialog):
        _translate = QtCore.QCoreApplication.translate
        confirm_delete_dialog.setWindowTitle(_translate("confirm_delete_dialog", "Delete User"))
        self.confirm_delete_label.setText(_translate("confirm_delete_dialog", "Are you sure? The user information and library files will be deleted."))
        self.yes_button.setText(_translate("confirm_delete_dialog", "Yes"))
        self.no_button.setText(_translate("confirm_delete_dialog", "No"))

    def _confirmed(self, confirm_delete_dialog, master):
        os.remove(USER_FILE_NAME)
        os.remove(LIBRARY_FILE_NAME)

        from SteamUI import SteamUI
        SteamUI(master)
        confirm_delete_dialog.accept()
