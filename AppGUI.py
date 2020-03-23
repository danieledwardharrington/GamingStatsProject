import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Gaming Stats")
root.geometry("1200x700")

key_label = Label(root, text = "Enter your Steam api key", font = ("Helvetica", 14), anchor = W, width = 25, pady = 10)
key_label.grid(row = 0, column = 0)
key_entry = Entry(root, width = 25, font = ("Helvetica", 14))
key_entry.grid(row = 0, column = 1)
id_label = Label(root, text = "Enter your Steam ID (number)", font = ("Helvetica", 14), anchor = W, width = 25, pady = 10)
id_label.grid(row = 1, column = 0)
id_entry = Entry(root, width = 25, font = ("Helvetica", 14))
id_entry.grid(row = 1, column = 1)

submit_button = Button(root, text = "SUBMIT", borderwidth = 5, width = 34, font = ("Helvetica", 12))
submit_button.grid(row = 2, column = 0)

instructions_button = Button(root, text = "Need API key/Don't know SteamID number?", borderwidth = 5, width = 34, font = ("Helvetica", 12))
instructions_button.grid(row = 3, column = 0)


root.mainloop()