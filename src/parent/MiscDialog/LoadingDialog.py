from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QObject
from Global import *
import logging as log


class LoadingDialog(QObject):

    log.basicConfig(filename = LOG_FILE_NAME, level = log.DEBUG, format = LOG_FORMAT)

    progress = 0
    increments = 0

    def __init__(self):
        super().__init__()
        log.info("Loading dialog init")
        self.loading_dialog = QtWidgets.QDialog()
        self.setup_Ui(self.loading_dialog)
        self.loading_dialog.setWindowIcon(QIcon(WIN_ICON))
        self.loading_dialog.setWindowFlags(self.loading_dialog.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

    def setup_Ui(self, loading_dialog):
        loading_dialog.setObjectName("loading_dialog")
        loading_dialog.resize(400, 150)
        self.progress_dialog_vert_layout = QtWidgets.QVBoxLayout(loading_dialog)
        self.progress_dialog_vert_layout.setObjectName("progress_dialog_vert_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.progress_dialog_vert_layout.addItem(spacerItem)
        self.label_horz_layout = QtWidgets.QHBoxLayout()
        self.label_horz_layout.setObjectName("label_horz_layout")
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.label_horz_layout.addItem(spacerItem1)
        self.loading_label = QtWidgets.QLabel(loading_dialog)
        self.loading_label.setMinimumSize(QtCore.QSize(150, 0))
        self.loading_label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setPointSize(10)
        self.loading_label.setFont(font)
        self.loading_label.setWordWrap(True)
        self.loading_label.setObjectName("loading_label")
        self.label_horz_layout.addWidget(self.loading_label)
        spacerItem2 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.label_horz_layout.addItem(spacerItem2)
        self.progress_dialog_vert_layout.addLayout(self.label_horz_layout)
        self.bar_horz_layout = QtWidgets.QHBoxLayout()
        self.bar_horz_layout.setObjectName("bar_horz_layout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bar_horz_layout.addItem(spacerItem3)
        self.loading_progressbar = QtWidgets.QProgressBar(loading_dialog)
        self.loading_progressbar.setMinimumSize(QtCore.QSize(300, 0))
        self.loading_progressbar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.loading_progressbar.setProperty("value", 0)
        self.loading_progressbar.setObjectName("loading_progressbar")
        self.bar_horz_layout.addWidget(self.loading_progressbar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bar_horz_layout.addItem(spacerItem4)
        self.progress_dialog_vert_layout.addLayout(self.bar_horz_layout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.progress_dialog_vert_layout.addItem(spacerItem5)

        self.retranslateUi(loading_dialog)
        QtCore.QMetaObject.connectSlotsByName(loading_dialog)

    def retranslateUi(self, loading_dialog):
        _translate = QtCore.QCoreApplication.translate
        loading_dialog.setWindowTitle(_translate("loading_dialog", "Compiling Steam Library"))
        self.loading_label.setText(_translate("loading_dialog", "Loading..."))

    def set_increments(self, increments):
        log.info("Set increments called, amount is " + str(increments))
        self.increments = increments

    def increment_bar(self, ready):
        log.info("Increment bar called")
        if ready:
            log.info("Increment bar ready")
            if self.progress < (100 - self.increments) and self.increments > 0:
                self.progress += self.increments
                self.setProgressValue(self.progress)

    def get_progress(self):
        return self.progress

    def show_dialog(self):
        log.info("Show dialog called")
        self.loading_dialog.show()
        self.loading_dialog.exec_()        

    def setProgressValue(self, value):
        log.info("Set progress value called, value is " + str(value))
        self.loading_progressbar.setValue(value)

    def last_increment(self, ready):
        log.info("Last increment called")
        if ready:
            self.progress += self.increments
            self.setProgressValue(self.progress)
            self.loading_label.setText("Finished!")