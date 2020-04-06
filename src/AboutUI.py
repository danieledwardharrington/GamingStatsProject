from Global import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class AboutUI(object):

    def __init__(self):
        about_dialog = QtWidgets.QDialog()
        self.setup_Ui(about_dialog)
        about_dialog.show()
        about_dialog.exec_()


    def setup_Ui(self, about_dialog):
        about_dialog.setObjectName("about_dialog")
        about_dialog.resize(600, 500)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        about_dialog.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(about_dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.about_vert_layout = QtWidgets.QVBoxLayout()
        self.about_vert_layout.setObjectName("about_vert_layout")
        self.about_label = QtWidgets.QLabel(about_dialog)
        self.about_label.setMinimumSize(QtCore.QSize(1, 1))
        self.about_label.setAlignment(QtCore.Qt.AlignCenter)
        self.about_label.setWordWrap(True)
        self.about_label.setObjectName("about_label")
        self.about_vert_layout.addWidget(self.about_label)
        self.verticalLayout_3.addLayout(self.about_vert_layout)
        self.link_vert_layout = QtWidgets.QVBoxLayout()
        self.link_vert_layout.setObjectName("link_vert_layout")
        self.gform_label = QtWidgets.QLabel(about_dialog)
        self.gform_label.setMinimumSize(QtCore.QSize(1, 1))
        self.gform_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gform_label.setWordWrap(True)
        self.gform_label.setOpenExternalLinks(True)
        self.gform_label.setObjectName("gform_label")
        self.link_vert_layout.addWidget(self.gform_label)
        self.gform_label.linkActivated.connect(lambda: self._send_to_form)
        self.verticalLayout_3.addLayout(self.link_vert_layout)

        self.retranslateUi(about_dialog)
        QtCore.QMetaObject.connectSlotsByName(about_dialog)

    def retranslateUi(self, about_dialog):
        _translate = QtCore.QCoreApplication.translate
        about_dialog.setWindowTitle(_translate("about_dialog", "Gaming Stats Project - About"))
        self.about_label.setText(_translate("about_dialog", "This app was developed using the Steam Web API. The genres for all games are scraped from each game\'s respective Steam page (genre will be blank if the game is no longer on Steam)."))
        self.gform_label.setToolTip(_translate("about_dialog", "Fill out a feedback form"))
        self.gform_label.setText(_translate("about_dialog", "<html><head/><body><p><a href=https://docs.google.com/forms/d/e/1FAIpQLSdZsLvup2XdG2JxSSInDUPRUxjP-2KcxSmKVMHRHgaTpwNbWA/viewform?usp=sf_link <span style=\" text-decoration: underline; color:#0000ff;\">Have feedback? Click here</span></p></a></body></html>"))

    def _send_to_form(self):
        QDesktopServices.openUrl(QUrl(GOOGLE_FORM_URL))