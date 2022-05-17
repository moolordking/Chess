
from tkinter import *
from tkinter import font
# module for colours and graphics - including fonts
from colours_and_graphics import *

from game_page import *

def load_game(root, side):
    root.destroy()
    create_game_gui(side)

def create_gui():
    # create window
    root = Tk()
    root.title("Menu")
    root.geometry("640x400+600+200")
    root.configure(background=get_colour(0))
    # display header
    header_message = Label(root, text="Chess")
    header_message.config(font=(get_font(), 40), fg=get_colour(1), bg=get_colour(0))
    header_message.grid(row=0, column=0, columnspan=2, sticky="W", padx=240, pady=30)

    # display start buttons
    button_font = font.Font(family=get_font(), size=13, weight="bold")

    start_button = Button(root, text="Play as White", width=26, height=2, command=lambda: load_game(root, 0))
    start_button.config(fg=get_colour(4), bg=get_colour(1), borderwidth=0)
    start_button['font'] = button_font
    start_button.grid(row=2, column=0, padx=10, pady=50)

    other_start_button = Button(root, text="Play as Black", width=26, height=2, command=lambda: load_game(root, 1))
    other_start_button.config(fg=get_colour(1), bg=get_colour(4), borderwidth=0)
    other_start_button_font = font.Font(family=get_font(), size=13, weight="bold")
    other_start_button['font'] = button_font
    other_start_button.grid(row=2, column=1, padx=10, pady=50)

    root.mainloop()

if __name__ == "__main__":
    create_gui()