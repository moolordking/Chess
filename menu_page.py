
from tkinter import *
from tkinter import font
import settings_handler as sh
import random as r

from game_page import *

def load_game(root):
    root.destroy()
    side = 1
    if sh.get_settings(3) == "random":
        side = int(r.random()*2)
    elif sh.get_settings(3) == "white":
        side = 0
    create_game_gui(side)

def create_gui():
    # create window
    root = Tk()
    root.title("Menu")
    root.geometry("640x400+600+200")
    root.configure(background=get_colour(0))
    root.iconbitmap('favicon.ico')
    # display header
    header_message = Label(root, text="Chess")
    header_message.config(font=(get_font(), 40), fg=get_colour(1), bg=get_colour(0))
    header_message.grid(row=0, column=0, columnspan=2, sticky="W", padx=240, pady=30)

    # display start buttons
    button_font = font.Font(family=get_font(), size=13, weight="bold")

    start_button = Button(root, text="PLAY", width=26, height=2, command=lambda: load_game(root))
    start_button.config(fg=get_colour(4), bg=get_colour(1), borderwidth=0)
    start_button['font'] = button_font
    start_button.grid(row=2, column=0, columnspan=2, pady=50)

    start_button = Button(root, text="Settings", width=15, height=1, command=lambda: settings_load(root))
    start_button.config(font=(get_font(), 15),fg=get_colour(0), bg=get_colour(3), borderwidth=0)
    start_button.grid(row=3, column=0, columnspan=2, pady=70)

    root.mainloop()

def settings_load(root):
    sh.settings_gui(root)
    create_gui()

if __name__ == "__main__":
    create_gui()