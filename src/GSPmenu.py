import tkinter
from tkinter import *
from AboutWindow import *

class GSPmenu(Menu):
    
    def __init__(self, master=None, cnf = {}, **kw):
        super().__init__(master=master, cnf = {}, **kw)

        gsp_menu = Menu(master)
        master.config(menu = gsp_menu)

        file_menu = Menu(gsp_menu)
        file_menu.add_command(label = "Exit", command = master.destroy)

        gsp_menu.add_cascade(label = "File", menu = file_menu)

        help_menu = Menu(gsp_menu)
        help_menu.add_command(label = "About", command = self._show_about)

        gsp_menu.add_cascade(label = "Help", menu = help_menu)

    def _show_about(self):
        AboutWindow()