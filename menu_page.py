
from tkinter import *
from tkinter import font
# module for colours and graphics - including fonts
from colours_and_graphics import *

from game_page import *

def load_game(root):
    root.destroy()
    create_game_gui()

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

    # display start button
    start_button = Button(root, text="BEGIN", width=26, height=2, command=lambda: load_game(root))
    start_button.config(fg=get_colour(0), bg=get_colour(3), borderwidth=0)
    start_button_font = font.Font(family=get_font(), size=13, weight="bold")
    start_button['font'] = start_button_font
    start_button.grid(row=4, column=0, columnspan=2, padx=10, pady=50)

    root.mainloop()

if __name__ == "__main__":
    create_gui()